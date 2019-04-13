from flask import abort, Blueprint, jsonify, render_template, request, redirect, url_for
from werkzeug import secure_filename
import os

from ..models import Podcasts

podcast = Blueprint('podcast', __name__)
podcast_path = "./podcasts"

@podcast.route('/data', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        if 'id' not in request.args:
            all_Podcasts = Podcasts.objects()
            return jsonify(all_Podcasts)
        podcasts = Podcasts.objects(id=request.args['id'])
        return jsonify(podcasts)
        
        
    f = request.files['podcast']
    
    print(request.form)
    form = request.form
    podcast = Podcasts(title=form['title'], 
                        host=form['host'], 
                        description=form['description'])
    podcast.save()
    path = os.path.join(podcast_path, secure_filename(str(podcast.id) + ".mp3"))
    print(f"Saved to {path}")
    f.save(path)
    return 'file uploaded successfully'

@podcast.route('/suggestions')
def suggestions():
    if 'id' not in request.args:
        abort(400)
    dummy_data = {'suggestions': 
    [{'start_time': 13793, 
    'end_time': 25000,
    'transcript': "Why would you do this to me Miss Edision? Because I am the devil"}, 
    {'start_time': 49000, 
    'end_time': 77777,
    'transcript': "Knowing what to read and what to listen to, what kind of questions to ask that’ll be engaging and that they’ll give good answers to. How to follow up on a question if you get an unexpected answer. I’m kind of a control freak, I’m like, “Okay, here’s exactly what’s in the beginning. You know I’m going to ask question a, b, c, d, e, f and this is how it’s going to go.” and you know you ask a question and they start giving you answers all over the map and suddenly your perfect plan is thrown into disarray. Just having the composure and the ability to calm down and be like, “Okay, it’s okay.” Just listening to what they’re saying and have a normal conversation was difficult at first. Other things, like I don’t know of you’d call this a skill, but just being comfortable in my own skin. Not cringing at the sound of my own voice."}
    ]}
    return jsonify(dummy_data)
