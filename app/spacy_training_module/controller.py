from flask import Blueprint, request

from .data_prep import csv_to_spacy
from .training import train_model

spacy_training_controller = Blueprint('spacytraining', __name__, url_prefix='/spacytraining')

@spacy_training_controller.route('/trigger', methods=['POST'])
def trigger_training():
    training_data, labels = csv_to_spacy()
    train_model(training_data, labels)
    return 'Training Complete'