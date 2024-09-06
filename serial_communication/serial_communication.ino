//-- Libraries
#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>
#include <Wire.h>

//-- Definitions and Variable Declaration
#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define SCREEN_ADDRESS 0x3D
#define OLED_RESET 13

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire1, OLED_RESET);

const String AFFIRMATIVE = "Job's done!";
const int COLOR = 1;
const int MAX_CAPACITY = 1024;

String text;
int xCoordinate = 0;
int yCoordinate = 0;

/* -- Older stuff and/or stuff that didn't (doesn't?) work
 char* marquee;
 int x;
 String response = "And all the clouds that lour'd upon our house in the deep bosom of the ocean buried.";
*/

//-- Functions (may create custom header to hold)
unsigned char* gather_bytes(){
  unsigned char *bitmapBytes[MAX_CAPACITY];
};

void display_text_OLED(String string, int x, int y){
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(x, y);
  display.println(string);
  display.display();
};

void display_bitmap_OLED(const unsigned char *BITMAP_IMAGE){
  display.clearDisplay();
  display.drawBitmap(0, 0, BITMAP_IMAGE, SCREEN_WIDTH, SCREEN_HEIGHT, COLOR);
  display.display();
};

void push_text_to_display(String whatToPush){
  display_text_OLED(whatToPush, xCoordinate, yCoordinate);
  respond(AFFIRMATIVE);
};

void push_bitmap_to_display(){
  const unsigned char PROGMEM IMAGE[MAX_CAPACITY] = {};
  // display_bitmap(IMAGE);
  respond(AFFIRMATIVE);
};

void respond(String response){
  Serial.print(response);
};


//-- The stuff that does the things
void setup() {
  Serial.begin(1000000);
  display.begin();
  Serial.setTimeout(1);
  display.clearDisplay();
}

void  loop() {
  if (Serial.available()){
    text = Serial.readString();
    push_text_to_display(text);
  }
  // while (!Serial.available());
  // text = Serial.readString();
  // // Serial.print(text);
  // push_text_to_display(text);
}
