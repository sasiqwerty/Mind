---
aliases: 
tags: 
date created: Friday, August 11th 2023, 7:40:30 pm
date modified: Friday, August 11th 2023, 8:04:51 pm
---
- [Speech Recognition in Python using Google Speech API - GeeksforGeeks](https://www.geeksforgeeks.org/speech-recognition-in-python-using-google-speech-api/)  
- [SpeechRecognition · PyPI](https://pypi.org/project/SpeechRecognition/) #api #lib

```python
import speech_recognition as sr
# Create a recognizer object
recognizer = sr.Recognizer()
# Open the audio file
with sr.AudioFile("record.wav") as source:
    # Listen to the audio file
    audio_data = recognizer.record(source)
    # Recognize the audio data
    text = recognizer.recognize_google(audio_data)
print("The text is: " + text)
```

There is file size limitation and it requires an active connection but I have a feeling that If I find the library that breaks down the file into chunks and reads them individually I can get a good result.
