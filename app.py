# -*- coding: utf-8 -*-

from flask import Flask
from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
freezer = Freezer(app)

# import sys
#
# from flask import Flask, render_template
# from flask_flatpages import FlatPages
# from flask_frozen import Freezer
#
# DEBUG = False
# # FLATPAGES_AUTO_RELOAD = DEBUG
# FLATPAGES_EXTENSION = '.md'
#
# app = Flask(__name__)
# app.config.from_object(__name__)
# pages = FlatPages(app)
# freezer = Freezer(app)
#
# @app.route('/')
# def index():
#     return render_template('home.html')
#
# @app.route('/map')
# def map():
#     return render_template('map.html')
#
# @app.route('/projects')
# def projects():
#     projects = [p for p in pages if "project" in p.meta.get('tags', [])]
#     return render_template('projects.html', pages=projects)
#
# @app.route('/writing')
# def writing():
#     posts = [p for p in pages if "writing" in p.meta.get('tags', [])]
#     return render_template('writing.html', pages=posts)
#
#
# @app.route('/<path:path>/')
# def page(path):
#     page = pages.get_or_404(path)
#     return render_template('page.html', page=page)
#
# if __name__ == '__main__':
#     if len(sys.argv) > 1 and sys.argv[1] == "build":
#         freezer.freeze()
#     else:
#         app.run(port=8000)
