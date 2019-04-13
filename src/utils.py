from werkzeug import secure_filename
import os

podcast_path = "./podcasts"

def podcastPath(podcast_id, absolute=False):
    cur_podcast_path = podcast_path
    if absolute:
        cur_podcast_path = '.'+cur_podcast_path
        print(cur_podcast_path)
        
    path = os.path.join(cur_podcast_path, secure_filename(str(podcast_id) + ".mp3"))
    print(path)
    return path