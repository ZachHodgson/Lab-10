const int analogIn1 = A0;
const int analogIn2 = A1;
int analogVal1 = 0;
int analogVal2 = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  analogVal1 = analogRead(analogIn1);
  analogVal2 = analogRead(analogIn2);
  Serial.print(analogVal1);
  Serial.print(" , ");
  Serial.println(analogVal2);
  delay(1000);
}
