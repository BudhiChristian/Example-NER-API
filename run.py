from gevent.pywsgi import WSGIServer
from app import config, app

if __name__ == '__main__':
    run_config = config['runConfigurations']
    http_server = WSGIServer((run_config['host'], run_config['port']), app)
    print('Running on port {}'.format(run_config['port']))
    http_server.serve_forever()
