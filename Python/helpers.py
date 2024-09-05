"""Helper functions and classes for serial communication with Arduino."""

def is_word_too_large(word: str, maxSize: int):
    """Checks if each word is longer or shorter than the max number of characters per line."""
    return True if len(word) > maxSize else False

def split_large_word(largeWord: str, splitLength: int):
    """
Splits a word larger than the allowed number of characters by the split length and automatically appends a hypen at the end of the first split chunk.
Returns a touple of the first part of the word (frontChunk + a hyphen) and the remaining letters of the word (backChunk).
    """
    frontChunk:str = largeWord[:splitLength]
    backChunk: str = largeWord[splitLength:]
    return f"{frontChunk}-", backChunk

def parse_large_word_to_one_line(wordToTest: str, lengthToCheck: int, splitArray: list):
    """Breaks up words that are larger than one line to as many lines as it needs."""
    splitLargeWordFront, splitLargeWordBack = split_large_word(wordToTest, lengthToCheck - 1)
    splitArray.append(splitLargeWordFront)
    while is_word_too_large(splitLargeWordBack, lengthToCheck) == True:
        splitLargeWordFront, splitLargeWordBack = split_large_word(splitLargeWordBack, lengthToCheck - 1)
        splitArray.append(splitLargeWordFront)
    return splitLargeWordBack

def reset_chunk(string: str, size: int):
    """Resets the stringChunk to an empty string (\"\") and the chunkSize to zero (0)."""
    string = ""
    size = 0
    return string, size

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
            splitWords: list = []
            if is_word_too_large(word, self.maxCharacters - 2) == True:
                word = parse_large_word_to_one_line(word, self.maxCharacters - 1, splitWords)
                if len(stringChunk) > 0:
                    stringArray.append(stringChunk)
                    stringChunk = ""
                for thing in splitWords:
                    stringArray.append(thing)
            chunkSize = len(stringChunk)
            if chunkSize + len(word) < self.maxCharacters:
                stringChunk += word
            elif index < len(splitString) - 1:
                stringArray.append(stringChunk)
                if len(splitWords) > 0:
                    for thing in splitWords:
                        stringArray.append(thing)
                    splitWords.clear()
                stringChunk, chunkSize = reset_chunk(stringChunk, chunkSize)
                stringChunk += word
            else:
                stringArray.append(stringChunk)
                stringChunk, chunkSize = reset_chunk(stringChunk, chunkSize)
                stringChunk += word
        stringArray.append(stringChunk)
        return stringArray
    
    def __repr__(self):
        return f"Text({self.text})"
    
    def __str__(self):
        return f"{self.text}"
