import comtypes.client
speak = comtypes.client.CreateObject("SAPI.SpVoice")
filestream = comtypes.client.CreateObject("SAPI.spFileStream")
filestream.open("out.wav", 3, False)
speak.AudioOutputStream = filestream
speak.Speak("test")
filestream.close()