import glob
import importlib
import traceback
from timeit import default_timer as timer

from flask import Flask
from flask_cors import CORS, cross_origin


def run_module(path):
    module = importlib.import_module(path)
    importlib.reload(module)
    solution = module.solution

    start = timer()
    output = solution()
    end = timer()

    return output, (end - start) * 1000


def create_app():
    app = Flask(__name__, static_url_path="/src", static_folder="src")
    CORS(app, resources={r"/src/*": {"origins": "*"}})

    app.config.from_pyfile("settings.py")
    REPOSITORY_LINK = app.config.get("REPOSITORY_LINK")

    @app.route("/challenges")
    @cross_origin()
    def challenges():
        def get_challenge_info(id):
            return {
                "name": id,
                "input_path": f"src/{id}/input.txt",
                "repository_url": f"{REPOSITORY_LINK}/{id}",
            }

        return [
            get_challenge_info(challenge.split("/")[-1])
            for challenge in glob.glob("src/reto*")
        ]

    @app.route("/challenge/<id>")
    @cross_origin()
    def resolve(id):
        log = ""
        execution_return = "success"
        output = ""
        elapsed_time = 0

        try:
            output, elapsed_time = run_module(f"src.{id}.main")
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
