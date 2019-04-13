from flask import abort, Blueprint, jsonify, render_template, request, redirect, send_file, url_for
import secrets 
import boto3
from pydub import AudioSegment
from io import BytesIO
import os

from ..models import Soundbites, Episodes
soundbite = Blueprint('soundbite', __name__)
s3 = boto3.client('s3')

@soundbite.route('/search', methods = ['GET', 'POST'])
def search():
    print(request.get_json())
    return "hello"

@soundbite.route('/data', methods = ['GET', 'POST'])
def data():
    if request.method == 'GET':
        if 'id' in request.args:
            soundbite = Soundbites.objects(id=request.args['id']).first()
            soundbite.presignAudio()
            return jsonify(soundbite)
        elif 'episode_id' in request.args:
            episode_soundbite = Soundbites.objects(episode=request.args['episode_id'])
            for soundbite in episode_soundbite:
                soundbite.presignAudio()
            return jsonify(episode_soundbite)
        else:
            all_soundbites = Soundbites.objects()
            for soundbite in all_soundbites:
                soundbite.presignAudio()
            return jsonify(all_soundbites)

    # f = request.files['audio']
    # key = secrets.token_hex(nbytes=16)
    # s3.upload_fileobj(f, 'yc-signal-soundbite-audio', key)
    r_data = request.get_json()
    print("R_DATA", r_data)
    episode = Episodes.objects(id=r_data['episode']).first()
    
    #Create Clip
    s3.download_file("yc-signal-episode-audio", episode.s3_audio_key, "temp.mp3")
    episode_audio = AudioSegment.from_mp3("temp.mp3")

    s = int(r_data['start_time'])
    e = int(r_data['end_time'])
    soundbite_audio = episode_audio[s:e]
    soundbite_audio.export("./temp2.mp3", format="mp3")
    length = len(soundbite_audio)
    
    key = secrets.token_hex(nbytes=16)
    s3.upload_file('temp2.mp3', 'yc-signal-soundbite-audio', key)
    soundbite = Soundbites(title=r_data['title'], 
                        episode=r_data['episode'],
                        podcast=episode.podcast,
                        length=length,
                        s3_audio_key=key)
    soundbite.presignAudio()
    soundbite.save()
    return jsonify(soundbite)


