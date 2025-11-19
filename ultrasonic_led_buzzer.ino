// Pins Ultrasonic
#define TRIG 9
#define ECHO 10

// LEDs
#define LED_ROUGE 7
#define LED_JAUNE 6
#define LED_VERTE 5

// Buzzer
#define BUZZER 8

void setup() {
Serial.begin(9600);

pinMode(TRIG, OUTPUT);
pinMode(ECHO, INPUT);

pinMode(LED_ROUGE, OUTPUT);
pinMode(LED_JAUNE, OUTPUT);
pinMode(LED_VERTE, OUTPUT);

pinMode(BUZZER, OUTPUT);
}

long getDistance() {
digitalWrite(TRIG, LOW);
delayMicroseconds(2);

digitalWrite(TRIG, HIGH);
delayMicroseconds(10);
digitalWrite(TRIG, LOW);

long duration = pulseIn(ECHO, HIGH);
long distance = duration * 0.034 / 2;
return distance;
}

void loop() {
long distance = getDistance();
Serial.print("Distance: ");
Serial.print(distance);
Serial.println(" cm");

if (distance < 15) {
// RED ON
digitalWrite(LED_ROUGE, HIGH);
digitalWrite(LED_JAUNE, LOW);
digitalWrite(LED_VERTE, LOW);

// Buzzer continuous
digitalWrite(BUZZER, HIGH);
}

else if (distance >= 15 && distance <= 30) {
// YELLOW ON
digitalWrite(LED_ROUGE, LOW);
digitalWrite(LED_JAUNE, HIGH);
digitalWrite(LED_VERTE, LOW);

// Buzzer intermittent
digitalWrite(BUZZER, HIGH);
delay(100);
digitalWrite(BUZZER, LOW);
}

else {
// GREEN ON
digitalWrite(LED_ROUGE, LOW);
digitalWrite(LED_JAUNE, LOW);
digitalWrite(LED_VERTE, HIGH);

// Buzzer OFF
digitalWrite(BUZZER, LOW);
}

delay(100);
}