char serialData;
int pin = 13;

int data = 0;
int analogPin = A2;

void setup() {
  pinMode(pin, OUTPUT);
  pinMode(analogPin, INPUT);
  Serial.begin(9600);
  digitalWrite(pin, LOW);
  
}

void loop() {
  data = analogRead(analogPin);
  Serial.println(data);
  
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
