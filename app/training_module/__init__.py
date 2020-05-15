from app import config

csv_location = config['trainingDetails']['csvLocation']
spacy_model_location = config['trainingDetails']['spacyModelLocation']

epochs = config['trainingDetails']['epochs']
batch_size = config['trainingDetails']['batchSize']
progress_size = config['trainingDetails']['progressDisplay']

from .controller import training_controller