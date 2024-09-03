// int x;

String response = "And all the clouds that lour'd upon our house in the deep bosom of the ocean buried.";

void respond(){
  String thing = Serial.readString();
  Serial.print(response);
};

void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
}

void  loop() {
  while (!Serial.available());
  respond();
  // x = Serial.readString().toInt();
  // Serial.print(x + 1);
}
