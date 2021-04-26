int relayPin = 6;

void setup() {
 pinMode(relayPin, OUTPUT);
 digitalWrite(relayPin, LOW);
}

void loop() {
 delay(2000);
 digitalWrite(relayPin, HIGH);
 delay(200);
 digitalWrite(relayPin, LOW);
 delay(200);

}
