from flask import Blueprint, request

from .tagger import tag_text, refresh

spacy_tagging_controller = Blueprint('spacytagging', __name__, url_prefix='/spacytagging')

@spacy_tagging_controller.route('/tag', methods=['GET'])
def tag():
    res = tag_text("Thousands of demonstrators have marched through London to protest the war in Iraq and demand the withdrawal of British troops from that country .")
    return res