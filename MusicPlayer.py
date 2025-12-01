import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

def main():
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("Audio Initialization Failed! ", e)
        return
    
    folder = "MP3"

    # Checks if playlist folder is in right directory
    if not os.path.isdir(folder):
        print(f"Folder '{folder}' not found")

if __name__ == "__main__":
    main()