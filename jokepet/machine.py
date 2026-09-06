import cowsay #for cow or any orthe animal you want to display
import pyjokes #for jokes
import pyttsx3 #for saying out loud
#here we have downloaded the 3 modules that we needed

#variable machine that holds what to say
machine = pyttsx3.init()

#variable joke for fetching n the joke
joke = pyjokes.get_joke()
cowsay.cow(joke)#picking animal

#giving the machine joke to say
machine.say(joke)
machine.runAndWait()