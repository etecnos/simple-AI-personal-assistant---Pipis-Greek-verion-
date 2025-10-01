
import speech_recognition as sr

import AI
import activated
import speak
from window import run_window
# Using multiprocessing to run pygame alongside with the main program
from multiprocessing import Process

#Preferd mic
mic = 3


#Process to recognise which mic to use
'''
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(f"Microphone with index {index}: {name}")
'''

r = sr.Recognizer()
active = False

#Possible words to activate the Assistant
wake_words = ["πίπη" , "pipi" , "ππ" , "pp" , "πίπι" , "πιπί" , "πιπή"]

user_text = ""

if __name__ == "__main__":

    # Initialize pygame window (window.py) - optional
    p = Process(target=run_window, args=("Pipis.png",))
    p.start()

    #SPEECH RECOGNITION

    with sr.Microphone(device_index=mic) as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Ο βοηθός είναι έτοιμος. Πες 'πίπη' για να ξεκινήσει.")

        while True:
            try:

                audio = r.listen(source, timeout=5)
                text = r.recognize_google(audio, language="el-GR").lower().strip()
                print("Άκουσα:", text)


                # Activate
                if text.strip() in wake_words and not active:
                    active = True
                    print("Μιλήστε")
                    #user speaks
                    user_text = str(activated.start(mic))
                    print(user_text)
                    if user_text == "stop":
                        active = False
                        continue
                    #Answer loads
                    answer = AI.personal_assistant(user_text)
                    print(answer)
                    #Speaker plays the answer
                    speak.speak_text(answer)
                    active = False

                # Close program
                if "close" in text :
                    print("Ο βοηθός απενεργοποιήθηκε. Κλείνω...")
                    p.terminate()
                    p.join()
                    exit(1)


            #Possible Errors of Speech Recognition
            except sr.WaitTimeoutError:
                if active:
                    print("Δεν άκουσα κάτι, συνεχίζω να περιμένω")
                continue
            except sr.UnknownValueError:
                print("Δεν κατάλαβα, επανέλαβε")
                continue
            except sr.RequestError:
                print("Πρόβλημα με την υπηρεσία Google.")
                continue

    p.terminate()
    p.join()