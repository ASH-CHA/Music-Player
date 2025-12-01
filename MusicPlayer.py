import os
import pygame

def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Audio Initialization Failed! ", e)
        return

if _name_ == "_main_":
    main()