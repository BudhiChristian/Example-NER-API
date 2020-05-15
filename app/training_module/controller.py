from flask import Blueprint, request

from .data_prep import csv_to_spacy
from .training import train_model

training_controller = Blueprint('training', __name__, url_prefix='/training')

@training_controller.route('/trigger', methods=['POST'])
def trigger_training():
    training_data, labels = csv_to_spacy()
    train_model(training_data, labels)
    return 'hello world'