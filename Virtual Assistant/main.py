import openai
import sounddevice as sd
import speech_recognition as sr
openai_api_key=''
assistant_name='Jarvis'
r=sr.Recognizer()

print(f"{assistant_name}: Hello! How can I assist you today?")

while True:
    with sr.Microphone() as source:
        print("Listening....")
        audio=r.listen(source)
    input=r.recnogizer_google(audio)
    print(f"User imput is : {input}")
    response=openai.Completion.create(engine='text-davinvi-003', prompt=f"User:{input}\n{assistant_name}")
    max_token=100

    