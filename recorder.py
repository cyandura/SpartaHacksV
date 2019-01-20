# @author: Kyle Droulard
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



# TODO: Implement a method for translating text to doc
def saveas(ftype, strout, ffile):
    ffile = ffile.replace(".flac", " ")
    if ftype == ".txt":
        ffile += ".txt"
        outfile = open(ffile, 'w')
        outfile.write(strout + "\n")
        print("converted as txt file")
    else:
        pdf = PDF()
        pdf.alias_nb_pages()
        pdf.add_page()
        pdf.set_font('arial', '', 12.0)
        pdf.ln(10)
        pdf.multi_cell(0, 50, strout)
        pdf.ln()
        ffile += ".pdf"
        pdf.output(ffile, 'F')
        print('converted as pdf file')


print("type 1 to convert a file 2 to record a file: ")
choice = int(input())
if choice == 1:
    print("What is the file name: ")
    sfile =input()
    ffile= sfile
    sfile += ".flac"
    print(convert(sfile))
    print("what type of file would you like to save it as: ")
    ftype=input()
    saveas(ftype, convert(sfile), sfile)
if choice == 2:
    print("Enter an amount of seconds you would like to record for: ")
    rtime = int(input())
    print("Enter a name for your file: ")
    newfname = input()
    record(rtime, newfname)
    sfile = newfname
    newfname+=".flac"
    print(convert(newfname))
    print("what type of file would you like to save it as: ")
    ftype = input()
    saveas(ftype, convert(newfname), sfile)

