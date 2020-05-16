import yaml

with open('./config.yml', 'r') as yml_file:
    config = yaml.load(yml_file, Loader=yaml.FullLoader)

from flask import Flask, json
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

from .spacy_training_module import spacy_training_controller
from .spacy_tagging_module import spacy_tagging_controller

app.register_blueprint(spacy_training_controller)
app.register_blueprint(spacy_tagging_controller)

@app.route('/env', methods=['GET'])
def view_config():
    return config

@app.errorhandler(HTTPException)
def general_error(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description
    })
    response.content_type = "application/json"
    return response