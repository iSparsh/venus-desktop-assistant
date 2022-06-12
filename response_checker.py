# importing files as modules
import speechrec # speech synthesis and recognition functions
import features # all features of the bot
def response_checker(text):
    '''
    perform all basic functions of the bot by matching input or requests with appropriate functions
    text -> speechrec.get_audio()
    return -> _
    '''
    try:
        # primary search function
        if 'search' in text.lower() or 'play' in text:
            features.search_web(text)
            return

        # introduction functions
        elif "who are you" in text or "define yourself" in text or "what is your name" in text:
            speak = '''Hello, I am Venus, your Desktop Assistant.
My name stands for "Very Efficient and Novel User Speech system". 
You can command me to perform various tasks such as opening applications, 
searching the web etcetera.'''
            speechrec.speaktext(speak)
            return

        elif text in ["hello", "hi", "hey", "hay", "Haider", "hai", "hi there", "hello there"]:
            speak = "Hello there"
            speechrec.speak_text(speak)
            return

        elif "who made you" in text or "created you" in text:
            speak = "I have been created by Sparsh Mishra"
            speechrec.speaktext(speak)
            return

        elif text == "how are you":
            speak = "I am fine, what about you?"
            speechrec.speak_text(speak)
            return

        # app searching and opening
        elif 'open' in text:
            features.open_application(text.lower())
            return
        
        # weather
        elif 'weather' in text:
            features.get_weather(text)
            return

        # time
        elif 'time' in text:
            features.get_time()
            return
        
        elif 'date' in text:
            features.get_date()

        # random things
        elif 'random' in text:
            features.get_random(text)
            return
        
        elif 'heads' in text or 'tails' in text \
            or 'flip coin' in text or 'flip a coin' in text:
            features.flip_coin()
            return

        # function out of scope
        else:
            speechrec.speaktext("I don't think I understand, however, I can search the web for you. Do you want to continue?")
            ans = speechrec.get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                features.search_web(text)
            else:
                return
    except:
        speechrec.speak_text("I had trouble understanding your instruction.")
