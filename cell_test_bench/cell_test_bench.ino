#define SAMPLING_FREQUENCY 5 // in Hz
#define T1 1 // in s
#define T2 60 // in s

int SWITCH_PIN = 2;
int TRIGGER_PIN = 3;
int BATTERY_PIN = 1;
int RESISTOR_PIN = 3;
int valB, valR;
int count;
double res_voltage, bat_voltage;

void setup() {
  // put your setup code here, to run once:
  pinMode(SWITCH_PIN, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(TRIGGER_PIN, OUTPUT);
  Serial.begin(9600);
}


void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(SWITCH_PIN) == HIGH) {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(200);
    digitalWrite(LED_BUILTIN, LOW);    

    digitalWrite(TRIGGER_PIN, HIGH);
    delay(200);
    digitalWrite(TRIGGER_PIN, LOW);    

    Serial.println("START");

    for (int i = 0; i < T1 * SAMPLING_FREQUENCY; i++) {
      valB = analogRead(BATTERY_PIN);
      valR = analogRead(RESISTOR_PIN);
      bat_voltage = ((double)valB / (double)1023) * 5.0;
      res_voltage = ((double)valR / (double)1023) * 5.0;
      Serial.println(bat_voltage);
      Serial.println(res_voltage);
      delay(1000 / SAMPLING_FREQUENCY);
    }

    for (int i = 0; i < T2 * SAMPLING_FREQUENCY; i++) {
      valB = analogRead(BATTERY_PIN);
      valR = analogRead(RESISTOR_PIN);
      bat_voltage = ((double)valB / (double)1023) * 5.0;
      res_voltage = ((double)valR / (double)1023) * 5.0;
      Serial.println(bat_voltage);
      Serial.println(res_voltage);
      delay(1000 / SAMPLING_FREQUENCY);
    }
    Serial.println("DONE");
  }
}
