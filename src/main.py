# Standard library imports
from pathlib import Path

# External dependencies
import keyboard

# Src file imports
import scrapper

PROJECT_DIR = Path.cwd().parent
DATA_DIR = PROJECT_DIR.joinpath('parse_data')


def main():
    print("Press esc to exit!")     # Show user how to stop the program


    # Main program loop - Waits for website link to be provided and then scrapes
    while True:
        # Terminate program if esc key is pressed
        if keyboard.read_key() == "esc":
            break
        else:
            # Get the link from the user when they start the program
            scrapper.website_link = input("Enter the link of the website you want to scrape: ")
            
            scrapper.scrape()


        
        



# Program entry point
if __name__ == "__main__":
    main()