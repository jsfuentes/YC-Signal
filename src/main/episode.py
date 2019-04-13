from flask import abort, Blueprint, jsonify, render_template, request, redirect, send_file, url_for
import secrets 
import boto3

from ..models import Episodes

episode = Blueprint('episode', __name__)
s3 = boto3.client('s3')
    
@episode.route('/data', methods = ['GET', 'POST'])
def data():
    if request.method == 'GET':
        if 'id' not in request.args:
            all_Episodes = Episodes.objects()
            for episode in all_Episodes:
                episode.presignAudio()
            return jsonify(all_Episodes)
        episode = Episodes.objects(id=request.args['id']).first()
        episode.presignAudio()
        return jsonify(episode)
        
    f = request.files['audio']
    form = request.form
    key = secrets.token_hex(nbytes=16)
    episode = Episodes(title=form['title'], 
                        podcast=form['podcast'], 
                        s3_audio_key = key)
    s3.upload_fileobj(f, 'yc-signal-episode-audio', key)
    episode.presignAudio()
    episode.save()
    return jsonify(episode)

@episode.route('/suggest')
def suggest():
    print("Suggesting", request.args)
    if 'id' not in request.args:
        abort(400)
    dummy_data = {'suggestions': 
    [{'start_time': 4000, 
    'end_time': 8000,
    'transcript': "Why would you do this to me Miss Edision? Because I am the devil"}, 
    {'start_time': 8500, 
    'end_time': 13000,
    'transcript': "Knowing what to read and what to listen to, what kind of questions to ask that’ll be engaging and that they’ll give good answers to. How to follow up on a question if you get an unexpected answer. I’m kind of a control freak, I’m like, “Okay, here’s exactly what’s in the beginning. You know I’m going to ask question a, b, c, d, e, f and this is how it’s going to go.” and you know you ask a question and they start giving you answers all over the map and suddenly your perfect plan is thrown into disarray. Just having the composure and the ability to calm down and be like, “Okay, it’s okay.” Just listening to what they’re saying and have a normal conversation was difficult at first. Other things, like I don’t know of you’d call this a skill, but just being comfortable in my own skin. Not cringing at the sound of my own voice."}
    ]}
    return jsonify(dummy_data)
