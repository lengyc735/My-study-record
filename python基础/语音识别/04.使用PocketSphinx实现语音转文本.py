import speech_recognition as sr

audio_file = '03.demo_audio.wav'
r = sr.Recognizer()
# 打开语音文件
with sr.AudioFile(audio_file)as source:
    audio = r.record(source)

# 将语音转换问文本
# print('文本内容：', r.recognize_google(audio)
print('文本内容：', r.recognize_google(audio, language='zh-CN'))