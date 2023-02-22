import pyperclip
import sys

text = {
    "name": "Hey, I'm Urek Mazino, you can call me Urek",
    "location": "I'm currently on the 130th floor of the Tower",
    "Occupation": "I guide others on viable career path",
}

if len(sys.argv) < 2:
    print("Usage: python mclip.py [keyphrase] - copy phrase text")
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in text:
    pyperclip.copy(text[keyphrase])
    print(f"Text for the keyphrase has been copied to clipboard: {keyphrase}")
else:
    print(f"No text for the keyphrase: {keyphrase}")


