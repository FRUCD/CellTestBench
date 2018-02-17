#define SAMPLING_FREQUENCY 5 // in Hz
#define T1 1 // in s
#define T2 60 // in s

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial.println("START");
    for (int i = 0; i < T1 * SAMPLING_FREQUENCY; i++) {
      Serial.println(1000 + i);
      Serial.println(2000 + i);
    }

    for (int i = 0; i < T2 * SAMPLING_FREQUENCY; i++) {
      Serial.println(3000 + i);
      Serial.println(4000 + i);
    }
    Serial.println("DONE");

}

void loop() {
  // put your main code here, to run repeatedly:

}
