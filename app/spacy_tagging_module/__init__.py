from app import config

modeLocation = config['trainingDetails']['spacyModelLocation']

from .tagger import refresh as __refresh
__refresh()

from .controller import spacy_tagging_controller