import pyttsx3
from PyPDF2 import PdfReader
from art import art_3d_diag
import warnings  # to ignore warnings which affect the aesthetic nature of output

# ignore warnings
warnings.filterwarnings("ignore")

# Engine Creation
speaker = pyttsx3.init()

# PDF Reader object instantiation
reader = PdfReader('Python-for-Data-Analysis.pdf')

# Abstract
print(art_3d_diag)
print('''
BOOK TITLE: Python-for-Data-Analysis🐍
This simple script is going to read the contents of this book to you👌.
This is made possible with the libraries: "pyttsx3" and "PyPDF2".\n\n
Before I begin reading, please choose your preferences for the following properties❤️🎶\n''')


# Functions needed

def set_rate():
    rate = speaker.getProperty('rate')
    should_change_rate = input(
        f'(Property 1)\nCurrent rate is {rate} words per minute.\nWould you like to change it?(Y/N): ').upper()
    if should_change_rate == 'Y':
        speaker.setProperty('rate', int(input('Enter desired rate: ')))
        print(f'Rate set to {rate}\n')
    elif should_change_rate == 'N':
        print(f'Rate set to default({rate})\n')
    else:
        print(f'Incorrect Input, rate set to default({rate})\n')


def set_volume():
    volume = int(speaker.getProperty('volume')) * 100
    should_change_volume = input(
        f'(Property 2)\nCurrent volume is {volume} [Min: 0, Max: 100].\nWould you like to change it?('
        f'Y/N): ').upper()
    if should_change_volume.upper() == 'Y':
        volume = int(input('Enter desired volume level: '))
        if 0 < volume <= 100:
            speaker.setProperty('volume', volume / 100)
            print(f'Volume set to ({volume})\n')
        else:
            print('Invalid input or Out of Range or Zero.\n Volume set to default\n')
    elif should_change_volume == 'N':
        print(f'Volume set to default({volume})\n')
    else:
        print(f'Incorrect Input, volume set to default({volume})\n')


def set_voice():
    voices = speaker.getProperty('voices')
    desired_voice = input('(Property 3)\nMale or Female? Which voice do you prefer: ').upper()
    for voice in voices:
        if desired_voice == 'MALE':
            speaker.setProperty('voice', voice.id)
            break
        elif desired_voice == 'FEMALE':
            speaker.setProperty('voice', voice.id)
        else:
            print('Invalid input. Default voice being used.')


# set rate(words per minute)
set_rate()

# set volume
set_volume()

# pick a voice(Male or Female)
set_voice()

# Read pdf
all_pages = reader.pages
pages_to_read = all_pages[16:len(all_pages)]
for page in pages_to_read:
    text = page.extract_text()
    speaker.say(text)

speaker.runAndWait()
