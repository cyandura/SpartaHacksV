import io
import os
import sounddevice as sd
import scipy.io.wavfile as wav
import soundfile as sf
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# 9999<fs
fs = 16000
duration = 20
myrecording = sd.rec(duration * fs, samplerate=fs, channels=1, dtype='float64')
print("Recording Audio")
sd.wait()
print("Audio Recording Complete, Play Audio")
sd.play(myrecording, fs)
sd.wait()
print("Play Audio Complete")

wav.write('test.wav', fs, myrecording)
print("checkpoint2")
data, samplerate = sf.read('test.wav')

print("checkpoint4")
sf.write('new.flac', data, samplerate)
print("checkpoint1")

# Instantiates a client
client = speech.SpeechClient()


# Loads the audio into memory
with io.open("./new.flac", 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
    sample_rate_hertz=samplerate,
    language_code='en-US')

# Detects speech in the audio file
print("before")
response = client.recognize(config, audio)
print("after")
for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))


