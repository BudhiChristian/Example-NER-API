from flask import Blueprint, request

from .data_prep import csv_to_spacy

training_controller = Blueprint('training', __name__, url_prefix='/training')

@training_controller.route('/trigger', methods=['POST'])
def trigger_training():
    training_data = csv_to_spacy()
    return 'hello world'