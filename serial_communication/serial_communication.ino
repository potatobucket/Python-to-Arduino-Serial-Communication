//-- Libraries
#include <Wire.h>
#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>

//-- Definitions and Variable Declaration
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define SCREEN_ADDRESS 0x3D
#define OLED_RESET 13

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire1, OLED_RESET);

const int COLOR = 1;

String affirmative = "Job's done!"
String marquee;

/* -- Older stuff and/or stuff that didn't (doesn't?) work
 char* marquee;
 int x;
 String response = "And all the clouds that lour'd upon our house in the deep bosom of the ocean buried.";
*/

//-- Functions (may create custom header to hold)
void display_text_OLED(String string){
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println(string);
  display.display();
};

void push_to_display(String whatToPush){
  marquee = Serial.readString();
  display_text_OLED(whatToPush);
  respond(affirmative);
};

void respond(String response){
  Serial.print(response);
};


//-- The stuff that does the things
void setup() {
  Serial.begin(115200);
  display.begin();
  Serial.setTimeout(1);
  display.clearDisplay();
}

void  loop() {
  while (!Serial.available());
  marquee = Serial.readString();
  push_to_display(marquee);
}
