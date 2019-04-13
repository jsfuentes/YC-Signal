from flask import abort, Blueprint, jsonify, render_template, request, redirect, send_file, url_for
import secrets 
import boto3

from ..models import Soundbites, Episodes
soundbite = Blueprint('soundbite', __name__)
s3 = boto3.client('s3')

@soundbite.route('/data', methods = ['GET', 'POST'])
def data():
    if request.method == 'GET':
        if 'id' not in request.args:
            all_Soundbites = Soundbites.objects()
            for soundbite in all_Soundbites:
                soundbite.presignAudio()
            return jsonify(all_Soundbites)
        soundbite = Soundbites.objects(id=request.args['id']).first()
        soundbite.presignAudio()
        return jsonify(soundbite)

    f = request.files['audio']
    key = secrets.token_hex(nbytes=16)
    s3.upload_fileobj(f, 'yc-signal-soundbite-audio', key)
    form = request.form
    Episodes.objects(id=form.episode).first()
    
    soundbite = Soundbites(title=form['title'], 
                        episode=form['episode'],
                        podcast=form['podcast'],
                        s3_audio_key=key)
    soundbite.save()
    return jsonify(soundbite)


