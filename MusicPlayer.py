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
    
    if not mp3_files:
        print("No .mp3 files found!")

    while True:
        print("***** MP3 Player *****")
        print("My song list:")

        for index, song in enumerate(mp3_files, start = 1):
            print(f"{index}. {song}")
        
        choice_input = input("\nEnter the song  # to play (or 'Q' to quit): ")

        if choice_input.upper() == "Q":
            print("Bye!")
            break

if __name__ == "__main__":
    main()