Importing the win32com module which is comtypes.client

import comtypes.client
Loading the Module of win32com SAPI

speak = comtypes.client.CreateObject("SAPI.SpVoice")
filestream = comtypes.client.CreateObject("SAPI.spFileStream")

 Now file is streamed
 saving the file in wav form
filestream.open("out.wav", 3, False)
speak.AudioOutputStream = filestream

 make file speak
speak.Speak("test")

Now close the file
filestream.close()