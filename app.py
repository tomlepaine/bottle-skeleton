
import argparse

from bottle import get, run, response, static_file, redirect
from jinja2 import Environment, PackageLoader

import config

parser = argparse.ArgumentParser(prog=config.name,
                                 description=config.description)

parser.add_argument('--port',
                    type=int,
                    default=8080,
                    help='Port where gui is running.')

args = parser.parse_args()

# Setup globals
PORT = args.port

ENV = Environment(loader=PackageLoader(config.package_name,
                                       config.template_dir))


@get('/')
def index():
    redirect('/hello-world')


@get('/hello-world')
def hello_world():
    template = ENV.get_template('hello-world.html')
    page = template.render()
    return page


@get('/page')
def page():
    template = ENV.get_template('not-implemented.html')
    page = template.render()
    return page


@get('/frame/<index:int>.jpeg')
def frame(index):
    response.content_type = "image/jpeg"

    return VIDEO.get_frame(index)


run(host='localhost', port=PORT)
