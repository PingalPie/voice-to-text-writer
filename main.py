import speech_recognition as sr
import pyautogui
# Importing modules required for the program

def takeCommand():
    # This function take microphone input by user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-IN')
        print("User Said: ", query)

    except Exception as e:
        print(e)

        print("Pardon please...")
        return "None"
    return query



def text():
    # This function will print for us
    audio  = takeCommand().lower()
    '''
    This variable will take data from takeCommandd function
    This will also run the takeCommand function'''
    pyautogui.write(audio)
    # This line will write whatever you spoke

text()
# Calling the printing funtion
