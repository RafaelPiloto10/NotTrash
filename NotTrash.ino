int redPin= 7;
int greenPin = 6;
int bluePin = 5;
int light = 0;
boolean bright = true;
boolean last_seen = true;
void setup() {
  Serial.begin(9600); //configure serial to talk to computer
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}
void loop() {
  
  light = analogRead(A0); // read and save value from PR
  
  if (light > 50){
    bright = true;
  }
  else{
    bright = false;
  }

  if (bright != last_seen){
    Serial.println("switched");
    last_seen = bright;
  }
  else{
    light = analogRead(A0); // read and save value from PR
  }
    
}
void setColor(int redValue, int greenValue, int blueValue) {
  analogWrite(redPin, redValue);
  analogWrite(greenPin, greenValue);
  analogWrite(bluePin, blueValue);
}
