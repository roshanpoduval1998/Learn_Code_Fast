from pywin32 import client 

speaker = win32com.client.Dispatch("SAPI.SpVoice") 
r = "India is my country"
speaker.Speak(r)
