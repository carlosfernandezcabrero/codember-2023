import glob
import importlib
import traceback
from timeit import default_timer as timer

import requests
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = "/api/v1/docs"
API_URL = "/api/v1/swagger"

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={"app_name": "Code Challenge API"},
)


def run_module(module):
    solution = module.solution
    input = requests.get(module.input_url).text

    start = timer()
    output = solution(input)
    end = timer()

    return output, (end - start) * 1000


def create_app():
    app = Flask(__name__, static_url_path="/api/v1/src", static_folder="src")
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    CORS(app, resources={r"/src/*": {"origins": "*"}})

    @app.route("/api/v1/challenges")
    @cross_origin()
    def challenges():
        def get_challenge_info(id):
            module = importlib.import_module(f"src.{id}.main")
            importlib.reload(module)

            return {
                "name": id,
                "input_path": module.input_url,
                "code": f"src/{id}/main.py",
            }

        return [
            get_challenge_info(challenge.split("/")[-1])
            for challenge in glob.glob("src/reto*")
        ]

    @app.route("/api/v1/challenge/<id>")
    @cross_origin()
    def resolve(id):
        log = ""
        execution_return = "success"
        output = ""
        elapsed_time = 0

        try:
            module = importlib.import_module(f"src.{id}.main")
            importlib.reload(module)

            output, elapsed_time = run_module(module)
        except:
            execution_return = "fail"
            log = traceback.format_exc()

        return {
            "output": output,
            "elapsed_time": f"{elapsed_time:.2f}",
            "execution_return": execution_return,
            "log": log,
        }

    @app.route("/api/v1/swagger")
    @cross_origin()
    def swagger():
        return {
            "openapi": "3.0.3",
            "info": {"title": "Challenges API", "version": "1.0.0"},
            "servers": [{"url": "http://localhost:5000/api/v1"}],
            "paths": {
                "/challenges": {
                    "get": {
                        "summary": "Soluciones a los retos",
                        "description": "Retorna todas las soluciones presentes con el nombre, el link al repositorio deonde se aloja el codigo fuente y el archivo con los datos de entrada.",
                        "responses": {
                            "200": {
                                "description": "Operación exitosa",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "input_path": {
                                                        "type": "string",
                                                        "description": "Url del archivo con los datos de entrada",
                                                        "example": "src/reto1/input.txt",
                                                    },
                                                    "name": {
                                                        "type": "string",
                                                        "description": "Nombre del reto",
                                                        "example": "reto1",
                                                    },
                                                    "repository_url": {
                                                        "type": "string",
                                                        "description": "Url de repositorio donde se aloja el codigo fuente de la solucion.",
                                                        "example": "https://github.com/carlosfernandezcabrero/codember-2023/tree/main/api/src/reto1",
                                                    },
                                                },
                                            },
                                        }
                                    }
                                },
                            }
                        },
                    }
                },
                "/challenge/{reto}": {
                    "get": {
                        "summary": "Resultados del reto",
                        "description": "Retorna los resultados, el tiempo que han tardado y el traceback del error, si se produce una excepción mientras que se ejecutan, de las soluciones.",
                        "parameters": [
                            {
                                "name": "reto",
                                "in": "path",
                                "description": "Id del reto",
                                "required": "true",
                                "schema": {"type": "string"},
                            }
                        ],
                        "responses": {
                            "200": {
                                "description": "Operación exitosa",
                                "content": {
                                    "application/json": {
                                        "schema": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "elapsed_time": {
                                                        "type": "string",
                                                        "description": "Tiempo que tarda en ejecutarse la solución.",
                                                        "example": 0.79,
                                                    },
                                                    "execution_return": {
                                                        "type": "string",
                                                        "description": "Resultado del procesamiento de la peticion.",
                                                        "example": "success",
                                                    },
                                                    "log": {
                                                        "type": "string",
                                                        "description": "Traza de error producida al ejecutar la solución.",
                                                    },
                                                    "output": {
                                                        "type": "string",
                                                        "description": "Solución al reto.",
                                                        "example": "murcielago15leon15jirafa15cebra6elefante15rinoceronte15hipopotamo15ardilla15mapache15zorro15lobo15oso15puma2jaguar14tigre10leopardo10gato12perro12caballo14vaca14toro14cerdo14oveja14cabra14gallina10pato10ganso10pavo10paloma10halcon11aguila11buho11colibri9canario8loro8tucan8pinguino7flamenco7",
                                                    },
                                                },
                                            },
                                        }
                                    }
                                },
                            }
                        },
                    }
                },
            },
        }

    return app
