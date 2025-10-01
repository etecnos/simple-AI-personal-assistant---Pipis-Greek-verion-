

import speech_recognition as sr
import speak

r = sr.Recognizer()
#Variables for better recognition, change at will
r.pause_threshold = 2
r.non_speaking_duration = 0.8
r.energy_threshold =250

#VOICE RECOGNITION
def start(mic):
    speak.speak_text("Μιλήστε")
    while True:
        with sr.Microphone(device_index=mic) as source:
            try:
                audio = r.listen(source)
                act_text = r.recognize_google(audio, language="el-GR").lower().strip()
                if str(act_text) == "stop" or str(act_text) =="στοπ" :
                    return "stop"
                break






            except sr.UnknownValueError:
                print("❓ Δεν κατάλαβα...")
                continue

            except sr.RequestError:
                print("⚠️ Πρόβλημα με την υπηρεσία Google.")
                continue
    #Return text to main.py
    return act_text
