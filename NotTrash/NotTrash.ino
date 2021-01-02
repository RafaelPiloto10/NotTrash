int redPin = 5;
int greenPin = 6;
int bluePin = 7;

void setup() {
  Serial.begin(9600); //configure serial to talk to computer
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  setColor(255, 255, 255);
}

void loop() {
  if (Serial.available() > 0) {
    char in = (char) Serial.read();
    if (in == 'R') {
      setColor(0, 0, 255);
      delay(5000);
    } else if (in == 'O') {
      setColor(0, 255, 0);
      delay(5000);
    } else if (in == 'L') {
      setColor(255, 0, 0);
      delay(5000);
    } else {
      setColor(255, 255, 255);
    }
  }
  setColor(255, 255, 255);


}
void setColor(int redValue, int greenValue, int blueValue) {
  analogWrite(redPin, redValue);
  analogWrite(greenPin, greenValue);
  analogWrite(bluePin, blueValue);
}
