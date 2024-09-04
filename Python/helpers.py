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
            if is_word_too_large(word, self.maxCharacters - 1) == True:
                splitLargeWord = split_large_word(word, self.maxCharacters - 2)
                stringArray.append(splitLargeWord[0]) #-- <this bit right here is where it all gets hecked up. I just need to refine when it happens (which should be later)
                while is_word_too_large(splitLargeWord[1], self.maxCharacters - 1) == True:
                    splitLargeWord = split_large_word(splitLargeWord[1], self.maxCharacters - 2)
                    stringArray.append(splitLargeWord[0])
                word = splitLargeWord[1]
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

#-- As you can see, the logic works flawlessly when it's a standalone word. However, as part of a sentence it becomes a tangled up mess.
#-- I'm fairly sure it won't take me long to implement a fix for this particular situation but I've got to use more of my brain than I feel like using at this point.
#-- Ergo this little note I'm leaving for myself.
#-- TODO: delete after figuring it out. This section used only for testing
if __name__ == "__main__":
    bigWord = "Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenu-akitanatahu"  
    text = Text(bigWord)                                #-- prints: Taumatawhakatangihan-                                                                     
    for i in text.word_wrap:                            #---------: gakoauauotamateaturi-                                                                     
        print(f"{i:22}: {len(i)}")                      #---------: pukakapikimaungahoro-                                                                     
                                                        #---------: nukupokaiwhenu-akita-                                                                     
                                                        #---------: natahu
    
    bleh = Text("When in the Course of human events, it becomes necessary for one people to dissolve the antidisestablishmentarianism bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation. We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.")
    for i,v in enumerate(bleh.word_wrap):               #-- prints: When in the Course
        print(f"{i:>3}", f"{v:23}", f"{len(v):>2}")     #---------: of human events, it
                                                        #---------: becomes necessary
                                                        #---------: for one people to
                                                        #---------: antidisestablishment- <- wrong
                                                        #---------: dissolve the
                                                        #---------: arianism bands which  <- wrong
                                                        #---------: have connected them
                                                        #---------: with another, and to
                                                        #---------: assume among the
                                                        #---------: powers of the earth,
                                                        #---------: the separate and
                                                        #---------: equal station to
                                                        #---------: which the Laws of
                                                        #---------: Nature and of
                                                        #---------: Nature's God entitle
                                                        #---------: them, a decent
                                                        #---------: respect to the
                                                        #---------: opinions of mankind
                                                        #---------: requires that they
                                                        #---------: should declare the
                                                        #---------: causes which impel
                                                        #---------: them to the
                                                        #---------: separation. We hold
                                                        #---------: these truths to be
                                                        #---------: self-evident, that
                                                        #---------: all men are created
                                                        #---------: equal, that they are
                                                        #---------: endowed by their
                                                        #---------: Creator with certain
                                                        #---------: unalienable Rights,
                                                        #---------: that among these are
                                                        #---------: Life, Liberty and
                                                        #---------: the pursuit of
                                                        #---------: Happiness.
        






