import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

CLOUD_API_KEY = "AIzaSyCLH3WOEqDOA7J0hmxk-9h9dTDg2zVhEmU"

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = "./Community.mp3"

# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=16000,
    language_code='en-US',
    enable_word_time_offsets=True)

# Detects speech in the audio file
operation = client.long_running_recognize(config, audio)
print('Waiting for operation to complete...')
print(operation)
result = operation.result()
print(result)
for result in result.results:
    alternative = result.alternatives[0]
    print(u'Transcript: {}'.format(alternative.transcript))
    print('Confidence: {}'.format(alternative.confidence))

    for word_info in alternative.words:
        word = word_info.word
        start_time = word_info.start_time
        end_time = word_info.end_time
        print('Word: {}, start_time: {}, end_time: {}'.format(
            word,
            start_time.seconds + start_time.nanos * 1e-9,
            end_time.seconds + end_time.nanos * 1e-9))