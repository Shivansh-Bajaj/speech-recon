#import library
import speech_recognition as sr
import whisper
#Initiаlize  reсоgnizer  сlаss  (fоr  reсоgnizing  the  sрeeсh)
r = sr.Recognizer()
# whisper_client = whisper.
# Reading Audio file as source
#  listening  the  аudiо  file  аnd  stоre  in  аudiо_text  vаriаble

with sr.AudioFile('./data/sample-3.wav') as source:
    audio_text = r.listen(source)
    r.adjust_for_ambient_noise(source)
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    try:
        # using google speech recognition
        text = r.recognize_google(audio_text)
        print('Converting audio transcripts into text ...')
        # text = whisper_client.recognize(audio.get_wav_data(), 'english')
        print(text)
    except Exception as e:
         print('Sorry.. run again...')
         print(e)


