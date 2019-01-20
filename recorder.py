# @author: Kyle Droulard
import io
import os
import sounddevice as sd
import scipy.io.wavfile as wav
import soundfile as sf
from fpdf import FPDF
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
# Global Variables
# fs = 16000 recomended
fs = 16000
sd.default.samplerate=fs
sd.default.channels=1

class PDF(FPDF):
    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        pgnum = self.page_no()
        pgnum = pgnum.__str__()
        self.cell(0, 10, 'Page ' + pgnum , 0, 0, 'C')


def record(time, newfile):
    myrecording = sd.rec(time * fs)
    print("Recording Audio")
    sd.wait()
    print("Audio Recording Complete, Play Audio")
    sd.play(myrecording, fs)
    sd.wait()
    print("Play Audio Complete")

    newfile+=".wav"
    wav.write(newfile, fs, myrecording)
    data, samplerate = sf.read(newfile)
    newfile = newfile.replace(".wav", ".flac")
    newfile= "./" + newfile
    sf.write(newfile, data, samplerate)


#TODO: Implement a method to transcribe long length files
def convert(fname):
    # Instantiates a client
    client = speech.SpeechClient()

    # Loads the audio into memory
    file= "./"+fname
    with io.open(file, 'rb') as audio_file:
        content = audio_file.read()
        audio = types.RecognitionAudio(content=content)

    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=fs,
        language_code='en-US')

    # Detects speech in the audio file
    response = client.recognize(config, audio)

    resstr = " "
    for result in response.results:
        resstr += format(result.alternatives[0].transcript)
    return resstr


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
