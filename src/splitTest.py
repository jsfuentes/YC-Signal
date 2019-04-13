from pydub import AudioSegment
import requests
from io import BytesIO
import os

# r = requests.get("https://yc-signal-episode-audio.s3.amazonaws.com/0596b6aac12bb933db4d9c780bdc5314?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAITBMTRIC5H6AEKVA%2F20190413%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20190413T135015Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=76f11969a0cb8c70e2c27fd9691d98f749e53689394a804b25f4e41ea5b9cf6c")
# print(r.headers)
# sound = AudioSegment.from_file(BytesIO(r.content))
# 
# halfway_point = len(sound) // 2
# print(len(sound))
# first_half = sound[:halfway_point]
# print(len(first_half))
# 
# 
# # create a new file "first_half.mp3":
# first_half.export("./jj.mp3", format="mp3")

os.system("afplay Endgame.mp3")