import os
from cgi import parse_qs, escape
from wsgiref.simple_server import make_server

def app(env, resp):
    resp('200 OK', [('Content-Type', 'text/html')])
    try:
        request_body_size = int(env.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    try:
        PATH_OF_BLOG = ''
        # os.chdir(PATH_OF_BLOG)
        os.chdir('C:\\Users\\nerche\Documents\\_code\\vueblog')
        res = str(os.listdir(os.getcwd()))
        os.system('git status')
        os.system('git pull')
    except:
        return [b'error!']
    return [b'hello!']

httpd = make_server('', 8899, app)
print('Serving on port 8899...')
httpd.serve_forever()
