from flask import abort, Blueprint, jsonify, render_template, request, redirect, send_file, url_for
import secrets 
import boto3
from pydub import AudioSegment
from io import BytesIO

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

    # f = request.files['audio']
    # key = secrets.token_hex(nbytes=16)
    # s3.upload_fileobj(f, 'yc-signal-soundbite-audio', key)
    form = request.form
    episode = Episodes.objects(id=form['episode']).first()
    
    #Create Clip
    ea_stream = BytesIO()
    s3.download_fileobj("yc-signal-episode-audio", episode.s3_audio_key, ea_stream)
    episode_audio = AudioSegment.from_mp3(ea_stream)
    s = int(form['start_time'])
    e = int(form['end_time'])
    print("EA:", len(episode_audio))
    print(s, e)
    soundbite_audio = episode_audio
    print("SBA:", len(soundbite_audio))
    length = len(soundbite_audio)
    soundbite_audio = BytesIO(soundbite_audio.raw_data)
    
    key = secrets.token_hex(nbytes=16)
    s3.upload_fileobj(soundbite_audio, 'yc-signal-soundbite-audio', key)
    soundbite = Soundbites(title=form['title'], 
                        episode=form['episode'],
                        podcast=episode.podcast,
                        length=length,
                        s3_audio_key=key)
    soundbite.presignAudio()
    soundbite.save()
    return jsonify(soundbite)


