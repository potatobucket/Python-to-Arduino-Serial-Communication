"""Helper functions and classes for serial communication with Arduino."""

from PIL import Image

#-- Text handling --------------------------------------------------------------------------
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

def create_new_string_with_padded_spaces(stringArray: list, lineSize: int):
    """
Creates a string of all the lines in the word wrap but padded out with enough spaces to match the line length.
    """
    newString: str = ""
    for line in stringArray:
        if len(line) < lineSize:
            line += " " * (lineSize - len(line))
        newString += line
    return newString

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
        # return create_new_string_with_padded_spaces(stringArray, self.maxCharacters - 1)
    
    def __repr__(self):
        return f"Text({self.text})"
    
    def __str__(self):
        return f"{self.text}"
#-------------------------------------------------------------------------------------------

#-- Image handling -------------------------------------------------------------------------
def we_have_ascii_art_at_home(bitList: bytes, width: int, filename: str = "poor_mans_ascii"):
    """Generates a .txt file of the saddest ASCII art you've ever seen in your life."""
    smallString: str = ""
    bigString: str = ""
    for bit in bitList:
        smallString += bin(bit)[2:].zfill(8)
        if len(smallString) == width:
            bigString += f"{smallString}\n"
            smallString = ""
        with open(f"{filename}.txt", "w") as asciiArtAtHome:
            asciiArtAtHome.write(bigString)

class Picture:
    """Image to be pushed to the Adafruit 128x64 OLED screen through the Arduino serial communication."""
    def __init__(self, imagePath: str, maxWidth: int = 128, maxHeight: int = 64):
        self.imagePath = imagePath
        self.maxWidth = maxWidth
        self.maxHeight = maxHeight

    @property
    def convert_to_bitmap(self):
        """Converts the image to a series of bytes that can be read by the Adafruit 128x64 OLED screen."""
        with Image.open(self.imagePath) as image:
            width, height = image.size
            if image.mode != "RGBA":
                image = image.convert("RGBA")
            if width > self.maxWidth:
                widthRatio = self.maxWidth / width
                newHeight = int(widthRatio * height)
                image = image.resize((self.maxWidth, newHeight))
            if height > self.maxHeight:
                heightRatio = self.maxHeight / height
                newWidth = int(heightRatio * width)
                image = image.resize((newWidth, self.maxHeight))
            width, height = image.size
            outgoingImage = Image.new("RGBA", (self.maxWidth, self.maxHeight), (0, 0, 0, 0))
            outgoingWidth, outgoingHeight = outgoingImage.size
            imageX = (outgoingWidth - width) // 2
            imageY = (outgoingHeight - height) // 2
            outgoingImage.paste(image, (imageX, imageY))
            outgoingImage = outgoingImage.convert("1")
            outgoingData = [str(x // 255) for x in outgoingImage.getdata()]
            outgoingData = "".join(outgoingData)
            outgoingData = int(outgoingData, 2).to_bytes(1024)
            outgoingImage.close()
        return outgoingData

    def __repr__(self):
        return f"Picture({self.imagePath})"
    
    def __str__(self):
        return f"A picture with the filepath {self.imagePath}."
#-------------------------------------------------------------------------------------------
