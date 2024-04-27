from win32com.client import Dispatch

speaker=Dispatch('SAPI.SpVoice')
speaker.Speak("你是宇宙第一大傻逼")
del speaker