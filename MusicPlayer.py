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
        return
    
    # Test if file is mp3
    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]
    print(mp3_files)

if __name__ == "__main__":
    main()