import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    
    # Adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    
    # Capture audio from the microphone
    audio = r.listen(source)
    
    try:
        # Use Google Speech Recognition to convert audio to text
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
        
    except sr.UnknownValueError:
        print("Could not understand audio")
        
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))