import pygame
from pynput.keyboard import Key, Listener

sound_file = 'sounds'

sound_key = 'mech.wav'

pygame.init()

def key_press_event(key):

    sound = sound_file+'/'+sound_key

    pygame.mixer.music.load(sound)
    pygame.mixer.music.play(0)


obj = Listener(on_press=key_press_event)
obj.start()
obj.join()
