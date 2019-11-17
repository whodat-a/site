from flask import render_template
from app import app, pages

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/projects')
def projects():
    projects = [p for p in pages if "project" in p.meta.get('tags', [])]
    return render_template('projects.html', pages=projects)

@app.route('/writing')
def writing():
    posts = [p for p in pages if "writing" in p.meta.get('tags', [])]
    return render_template('writing.html', pages=posts)


@app.route('/<path:path>/')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)
