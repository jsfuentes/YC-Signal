from werkzeug import secure_filename
import os

podcast_path = "./podcasts"
soundbite_path = "./soundbites"

def podcastPath(id, absolute=False):
    cur_path = cur_path
    if absolute:
        cur_path = '.'+cur_path
        print(cur_path)
        
    path = os.path.join(cur_path, secure_filename(str(id) + ".mp3"))
    return path
    
def soundbitePath(id, absolute=False):
    cur_path = soundbite_path
    if absolute:
        cur_path = '.'+cur_path
        print(cur_path)
        
    path = os.path.join(cur_path, secure_filename(str(id) + ".mp3"))
    return path