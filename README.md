# Nobody -  By Nulli
 Nobody is your own personal assistant.
 
 set-up:
 1. make sure to you install these packages:
 	gtts
 	playsound
 	os
 	json
 	speech_recognition
 	threading
 	array
 	queue
 	datetime
 	pyaudio
 	wave
 	time
 	
 2. execute the set_up.py.
 3. in this version it is no keyword (eventually later) if you want to use this, you must code yourself a trigger that executes the main.py if you want to say a command.
 
 
 own commands:
 you can code your own commands 
 1. put your python script in the extern folder and 
 2. import the nobody_ex library, this library has these features:
 	say("that what you want to say", "the language(the standard language is in your conf)")
 	get_conf() #you get the config of the user
 	stt() #record the next sentence and return it into text
 3. code your application
 4. open the extern.json and register your script in the extern. json is an example.
