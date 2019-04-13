from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from werkzeug import secure_filename

soundbite = Blueprint('soundbite', __name__)

@soundbite.route('/')
def index():
    return jsonify({"hi": "there"})

@soundbite.route('/upload', methods = ['GET', 'POST'])
def upload():
    print("FILES", request.files)
    f = request.files['podcast']
    f.save(secure_filename(f.filename))
    return 'file uploaded successfully'
    
@soundbite.route('/text', methods = ['GET'])
def 
