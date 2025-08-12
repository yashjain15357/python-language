import pyttsx3

#this take all the things as a default 
# rate = 200
# volume =1.0
# voices = voices[1]
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()


# Initialize the text-to-speech engine
# setting of the voice
engine = pyttsx3.init()

# Get the available voices
voices = engine.getProperty('voices')

# Set the speech rate to 150 words per minute (default is around 200)
engine.setProperty('rate', 150)

# Set the volume to 70% (value should be between 0.0 and 1.0)
engine.setProperty('volume', 0.7)

# Set the voice to the second voice in the voices list (index 1)
# Note: Make sure there is a second voice available in the list
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)
else:
    print("The specified voice index does not exist.")

# Queue the text to be spoken
engine.say("This is a slower speed, at 70% volume, and using a female voice.")

# Process and run the speech commands
engine.runAndWait()


# import pyttsx3
engine = pyttsx3.init() # object creation

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        # printing current default voice rate
engine.setProperty('rate', 250)     # setting up new voice rate


"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current default volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1 

"""VOICE"""
voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("Hello World! My current speaking rate is ")
engine.say('My current speaking rate is ' + str(rate))
engine.runAndWait()
engine.stop()

"""Saving Voice to a file"""
# On linux make sure that 'espeak' and 'ffmpeg' are installed
engine.save_to_file('Hello World My current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate isMy current speaking rate is', 'test1.mp3')
engine.runAndWait()