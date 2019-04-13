from flask import abort, Blueprint, jsonify, render_template, request, redirect, send_file, url_for
import boto3
import secrets 
import json

from ..models import Podcasts

podcast = Blueprint('podcast', __name__)
s3 = boto3.client('s3')
    
@podcast.route('/data', methods = ['GET', 'POST'])
def data():
    if request.method == 'GET':
        if 'id' not in request.args:
            all_Podcasts = Podcasts.objects()
            for podcast in all_Podcasts:
                podcast.presignPhoto()
            return jsonify(all_Podcasts)
        podcast = Podcasts.objects(id=request.args['id'])
        podcast.presignPhoto()
        return jsonify(podcast)

    f = request.files['photo']
    key = secrets.token_hex(nbytes=16)
    s3.upload_fileobj(f, 'yc-signal-podcast-photo', key)
    print(request.form)
    form = request.form
    podcast = Podcasts(title=form['title'], 
                        host=form['host'], 
                        description=form['description'],
                        s3_photo_key=key)
    podcast.save()
    return jsonify(podcast)
