import datetime
import speak
import webbrowser
import weather
import os




def Action(send) :   
  
    data_btn  = send.lower()

    if "what is your name" in   data_btn :
      speak.speak("my name is virtual AI Codex")  
      return "my name is virtual AI Codex Assistant"

    elif "hello" in data_btn  or "hye" in data_btn  or "hay" in data_btn: 
        speak.speak("Hey sir, How i can  help you !")  
        return "Hey sir, How i can  help you !" 

    elif "how are you" in  data_btn :
            speak.speak("I am doing great these days sir") 
            return "I am doing great these days sir"   

    elif "thanku" in data_btn or "thank" in data_btn:
           speak.speak("its my pleasure sir to stay with you")
           return "its my pleasure sir to stay with you"      

    elif "good morning" in data_btn:
           speak.speak("Good morning sir, i think you might need some help")
           return "Good morning sir, i think you might need some help"   

    elif "time now" in data_btn:
          current_time = datetime.datetime.now()
          Time = (str)(current_time.hour)+ " Hour : ", (str)(current_time.minute) + " Minute" 
          speak.speak(Time)
          return str(Time) 

    elif "shutdown" in data_btn or "quit" in data_btn:
            speak.speak("ok sir")
            return "ok sir"  

    elif "play music" in data_btn or "song" in data_btn:
        webbrowser.open("https://gaana.com/")   
        speak.speak("gaana.com is now ready for you, enjoy your music")                   
        return "gaana.com is now ready for you, enjoy your music"


    elif 'open google' in data_btn or 'google'  in data_btn:
        url = 'https://google.com/'
        webbrowser.get().open(url)
        speak.speak("google open")  
        return "google open"

    elif 'youtube' in data_btn or "open youtube" in  data_btn:
        url = 'https://youtube.com/'
        webbrowser.get().open(url)
        speak.speak("YouTube open") 
        return "YouTube open"    
    
    elif 'weather' in data_btn :
        ans   = weather.Weather()
        speak.speak(ans) 
        return ans

    elif 'music from my laptop' in data_btn:
        url = 'D:\\music' 
        songs = os.listdir(url)
        os.startfile(os.path.join(url, songs[0]))
        speak.speak("songs playing...")
        return "songs playing..." 
    
    elif 'notepad' in data_btn:
        os.system('notepad')
        speak.speak("Open Notepad...")
        return "Open Notepad..."
    
    elif 'vscode' in data_btn:
        os.system('Visual Studio Code')
        speak.speak("Visual Studio Code...")
        return "Visual Studio Code..."
    
    elif 'internshala' in data_btn or 'Internshala' in data_btn:
        url = 'https://internshala.com/'
        webbrowser.get().open(url)
        speak.speak("Open Internshala...")
        return "Open Internshala..."
    
    elif 'github' in data_btn or 'Github'  in data_btn:
        url = 'https://github.com/'
        webbrowser.get().open(url)
        speak.speak("Open Github...")
        return "Open Github..."
    
    elif 'whatsapp' in data_btn:
        url = 'https://web.whatsapp.com/'
        webbrowser.get().open(url)
        speak.speak("Open whatsapp...")
        return "Open whatsapp..."
    
    elif 'facebook' in data_btn:
        url = 'https://www.facebook.com/login/'
        webbrowser.get().open(url)
        speak.speak("Open Facebook...")
        return "Open Facebook..."
    
    elif 'email' in data_btn:
        url = ''
        webbrowser.get().open(url)
        speak.speak("Open Email...")
        return "Open Email..."

    else :
        speak.speak( "i'm able to understand!")
        return "i'm able to understand!"       

