"""Helper functions and classes for serial communication with Arduino."""

def is_word_too_large(word: str, maxSize: int):
    if len(word) > maxSize:
        return True
    else:
        return False

def split_large_word(largeWord: str, splitLength: int):
    frontChunk:str = largeWord[:splitLength]
    backChunk: str = largeWord[splitLength:]
    return f"{frontChunk}-", backChunk

class Text:
    """Text to be pushed to the Adafruit 128x64 OLED screen through the Arduino serial communication."""
    def __init__(self, text: str):
        self.text = text
        self.maxCharacters: int = 22
    
    @property
    def word_wrap(self):
        """Wraps the text to fit the maximum number of characters for the Adafruit 128x64 OLED screen."""
        stringArray: list = []
        splitString: list = self.text.split(" ")
        splitString: list = [f"{word} " for word in splitString[:-1]] + [splitString[-1]]
        stringChunk: str = ""
        chunkSize: int = 0
        for index, word in enumerate(splitString):
            chunkSize = len(stringChunk)
            if chunkSize + len(word) < self.maxCharacters:
                stringChunk += word
            elif index < len(splitString) - 1:
                stringArray.append(stringChunk)
                stringChunk = ""
                chunkSize = 0
                stringChunk += word
            else:
                stringArray.append(stringChunk)
                stringChunk = ""
                chunkSize = 0
                stringChunk += word
        stringArray.append(stringChunk)
        return stringArray
    
    def __repr__(self):
        return f"Text({self.text})"
    
    def __str__(self):
        return f"{self.text}"
