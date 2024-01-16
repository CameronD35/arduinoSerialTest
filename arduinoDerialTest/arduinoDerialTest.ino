int number = 0;

void setup() {
  // put your setup code here, to run once:
	Serial.begin(9600);
}

void loop() {
	Serial.print(number++);
	Serial.print(": ");
  Serial.println(98);
	delay(500);
}
