from helpers import Text


#-- As you can see, the logic works flawlessly.
if __name__ == "__main__":

    #-- It works with one large word by itself.
    bigWord = "Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenu-akitanatahu"  
    text = Text(bigWord)                                #-- prints: Taumatawhakatangihan-                                                                     
    for i, v in enumerate(text.word_wrap):              #---------: gakoauauotamateaturi-                                                                     
        print(f"{i:>3}", f"{v:22}", f"{len(v):>2}")     #---------: pukakapikimaungahoro-                                                                     
                                                        #---------: nukupokaiwhenu-akita-                                                                     
                                                        #---------: natahu
    
    print()

    #-- Or, perhaps, with a long string of text.
    long = Text("When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation. We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.")
    for j, v in enumerate(long.word_wrap):              #-- prints: When in the Course
        print(f"{j:>3}", f"{v:23}", f"{len(v):>2}")     #---------: of human events, it  
                                                        #---------: becomes necessary
                                                        #---------: for one people to
                                                        #---------: dissolve the
                                                        #---------: political bands
                                                        #---------: which have connected
                                                        #---------: them with another,
                                                        #---------: and to assume among
                                                        #---------: the powers of the
                                                        #---------: earth, the separate
                                                        #---------: and equal station to
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

    print()

    last = Text("Or even in the middle of a sentence with words like \"antidisestablishmentarianism,\" \"Pneumonoultramicroscopicsilicovolcanoconiosis\" or even proper nouns like \"Lake Chargoggagoggmanchauggauggagoggchaubunagungamaugg!\"")
    for k, v in enumerate(last.word_wrap):              #-- prints: Or even in the
        print(f"{k:>3}", f"{v:23}", f"{len(v):>2}")     #---------: middle of a sentence
                                                        #---------: with words like
                                                        #---------: "antidisestablishmen-
                                                        #---------: tarianism,"
                                                        #---------: "Pneumonoultramicros-
                                                        #---------: copicsilicovolcanoco-
                                                        #---------: niosis" or even
                                                        #---------: proper nouns like
                                                        #---------: "Lake
                                                        #---------: Chargoggagoggmanchau-
                                                        #---------: ggauggagoggchaubunag-
                                                        #---------: ungamaugg!"
