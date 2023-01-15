'''
import os
import openai

OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

completion_client = openai.CompletionClient()

prompt = "What is the capital of France?"

completions = completion_client.create(
    prompt=prompt,
    engine="text-davinci-002",
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5
)

message = completions.choices[0].text

print(message)

'''

import speech_recognition as sr

# initialize recognizer class
r = sr.Recognizer()
r.

# microphone as source for input.
with sr.Microphone() as source:
    # listen for the first phrase and extract it into audio data
    print("i am listening")
    audio = r.listen(source)
    print("it's done")

# recognize speech using Google Speech Recognition
text = r.recognize_google(audio).__str__()

print(text)



'''
#Passing the text to ChatGPT
import openai
openai.api_key = "YOUR_API_KEY"
completion_client = openai.CompletionClient()
completions = completion_client.create(
    prompt=text,
    engine="text-davinci-002",
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5
)

message = completions.choices[0].text

print(message)
'''