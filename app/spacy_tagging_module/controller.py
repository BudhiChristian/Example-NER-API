from flask import Blueprint, request, abort

from .tagger import tag_text, refresh

spacy_tagging_controller = Blueprint('spacytagging', __name__, url_prefix='/spacytagging')

@spacy_tagging_controller.route('/tag', methods=['GET'])
def tag():
    query = request.args.get('query')
    if query is None or query.strip() == '':
        abort(400, 'parameter "query" required')
    res = tag_text(query)
    return res

@spacy_tagging_controller.route('/refresh', methods=['POST'])
def refresh_spacy_model():
    refresh()
    return 'model refreshed'