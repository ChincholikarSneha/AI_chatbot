import speech_recognition as aa  #convert speech to text 
import pyttsx3 #text-to-speech converion
import pywhatkit  #automates whatsapp msg, yt playing and other tasks
import datetime
import wikipedia


listener = aa.Recognizer()

machine = pyttsx3.init()

voices = machine.getProperty('voices')
print("Available voices:")
for index, voice in enumerate(voices):
    print(f"Voice {index}:")
    print(f" - Name: {voice.name}")
    print(f" - ID: {voice.id}")
    print(f" - Gender: {voice.gender if hasattr(voice, 'gender') else 'N/A'}")
    print(f" - Languages: {voice.languages}")
female_voice_id = None
for voice in voices:
    if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
        female_voice_id = voice.id
        break
if female_voice_id:
    machine.setProperty('voice', female_voice_id)
else:
    print("No female voice found!")
    
machine.say("Hello, I am Zira. How can I help you today?")
machine.runAndWait()
   
def talk(text):
    machine.say(text)
    
    machine.runAndWait()

def input_instruction():
    
    try:
        with aa.Microphone() as origin:
            print("listening...")
            listener.adjust_for_ambient_noise(origin)
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            
            if "Zira" in instruction:
                instruction = instruction.replace('Zira'," ")
                print(f"Instruction: {instruction}")
       
        
    except Exception as e:
        print(f"Error: {e}")
        instruction = ""
        
    return instruction
    
def instructions(instruction):
    
    if "play" in instruction:
        song = instruction.replace('play',"")
        talk("playing" + song)
        pywhatkit.playonyt(song)
        
    elif 'time' in instruction:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time'+ time)
        
    elif 'date' in instruction:
        date = datetime.datetime.now().strftime('%d /%m /%Y')
        talk("today's date " + date)
    
    elif 'hi' in instruction or 'hello' in instruction:
        talk('hi,how can I assist you?')
    
    elif 'how are you' in instruction:
        talk('I am good, how about you')
        
    elif 'who is' in instruction:
        human = instruction.replace('who is'," ")
        info = wikipedia.summary(human, 1)
        print(info)
        talk(info)
        
    else:
        talk('Please repeat')   

def play_zira():
    while True:
        instruction = input_instruction()
        if instruction:
            if "exit" in instruction or "stop" in instruction:
                talk("bye, have a good day!")
                break
            instructions(instruction)
   
        
play_zira()


    
    