import glob
import importlib
import traceback
from timeit import default_timer as timer

import requests
from flask import Flask
from flask_cors import CORS, cross_origin


def run_module(module):
    solution = module.solution
    input = requests.get(module.input_url).text

    start = timer()
    output = solution(input)
    end = timer()

    return output, (end - start) * 1000


def create_app():
    app = Flask(__name__, static_url_path="/src", static_folder="src")
    CORS(app, resources={r"/src/*": {"origins": "*"}})

    @app.route("/challenges")
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

    @app.route("/challenge/<id>")
    @cross_origin()
    def resolve(id):
        module = importlib.import_module(f"src.{id}.main")
        importlib.reload(module)

        log = ""
        execution_return = "success"
        output = ""
        elapsed_time = 0

        try:
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

    return app
