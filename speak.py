
from gtts import gTTS
import io
import pygame


def speak_text(text: str):
    # Voice processing
    tts = gTTS(text, lang="el")
    fp = io.BytesIO()
    tts.write_to_fp(fp)
    fp.seek(0)

    #Voice plays by using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(fp, "mp3")
    pygame.mixer.music.play()

    # Waits till the end of the frase
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

