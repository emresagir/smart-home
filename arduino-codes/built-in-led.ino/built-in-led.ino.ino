char serialData;
int pin = 13;

void setup() {
  pinMode(pin, OUTPUT);
  Serial.begin(9600);
  digitalWrite(pin, LOW);
}

void loop() {
  if (Serial.available() > 0){
    serialData = Serial.read();
    Serial.print(serialData);

    if(serialData =='1'){
      digitalWrite(pin, HIGH);
    }
    else if(serialData == '0'){
      digitalWrite(pin, LOW);
    }
  }
}
