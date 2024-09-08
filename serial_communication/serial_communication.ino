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
int characterSize = 8;
int maxLines = 7;
int maxYCoordinate = 64;
uint8_t bitmapBytes[MAX_CAPACITY];

//-- Functions (may create custom header to hold)
void display_text_OLED(String string, int x, int y){
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

void check_if_text_should_be_cleared(int sizeToClearAt){
  if (yCoordinate + characterSize == sizeToClearAt){
    delay(500);
    display.clearDisplay();
    display.display();
    yCoordinate = 0;
  }
};

void serial_text(){
  text = Serial.readString();
  push_text_to_display(text);
  yCoordinate += characterSize % (characterSize * maxLines);
  check_if_text_should_be_cleared(maxYCoordinate);
};

uint8_t gather_bytes(){
  Serial.readBytes(bitmapBytes, MAX_CAPACITY);
};

void push_bitmap_to_screen(){
  xCoordinate = 0;
  yCoordinate = 0;
  gather_bytes();
  display.clearDisplay();
  display.drawBitmap(xCoordinate, yCoordinate, bitmapBytes, SCREEN_WIDTH, SCREEN_HEIGHT, 2);
  display.display();
  respond(AFFIRMATIVE);
  Serial.flush();
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
  display.display();
}

void  loop() {
  while (!Serial.available());
  // serial_text();
  push_bitmap_to_screen();
}
