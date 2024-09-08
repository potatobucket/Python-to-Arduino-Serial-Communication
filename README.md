# Python to Arduino Serial Communication
 Communicating with the Arduino through Python.

 Image conversion logic adapted from work done by [this fine gentleman](https://github.com/trickman01).

 ## TODO:
  - ~~Figure out how to push the text data to the Arduino in a way it likes.~~
    - Figure out how to clear screen inbetween texts (every way I've tried so far has cleared each line as it went)
  - Find out how many different sizes text can be on the OLED screen.
    - Reconfigure the code to automatically set the word wrap based on the size of the text on the OLED screen.
  - Figure out how to send ~1kb of data to push a 128x64 bitmap to the OLED screen via the Arduino.

 ## Examples:
 The bitmap is the image data I plan to push to the OLED screen. The text is a successful test of using serial communication to push text to the screen.
 
 ![A 128x64 pixel bitmap of a potato](<Other/README Images/potato bitmap.png>)
 ![A photo showing text on the OLED screen that says "I typed this on the computer!"](<Other/README Images/OLED text example.jpg>)
