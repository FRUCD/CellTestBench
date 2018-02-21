// Records ADC values and applies a basic FIR filter (finite impulse response)

#define SAMPLING_FREQUENCY 5 // in Hz
#define T1 1 // in s
#define T2 60 // in s
const int NUM_SAMPLES = 100;

int SWITCH_PIN = 2;
int TRIGGER_PIN = 3;
int BATTERY_PIN = 3;
int RESISTOR_PIN = 1;
double valB, valR;
int count;
double res_voltage, bat_voltage;
const double CORRECTION_FACTOR = 2;//1.80806;

void setup() {
  // put your setup code here, to run once:
  pinMode(SWITCH_PIN, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(TRIGGER_PIN, OUTPUT);
  Serial.begin(9600);
  Serial.print("i");
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
      unsigned int avgB = 0, avgR= 0;
      for (int j = 0; j < NUM_SAMPLES; j++) {
        avgB += analogRead(BATTERY_PIN);
        avgR += analogRead(RESISTOR_PIN);
      }
      valB = (double)avgB / (double)NUM_SAMPLES;
      valR = (double)avgR / (double)NUM_SAMPLES;
      bat_voltage = valB * .0049;
      res_voltage = valR * .0049; 
      double current = ((res_voltage - bat_voltage) * CORRECTION_FACTOR) / .527778;
      Serial.print(valB);
      Serial.print("\t");
      Serial.print(current);
      Serial.println(); // Ends the line
      
      delay(1000 / SAMPLING_FREQUENCY);
    }

    for (int i = 0; i < T2 * SAMPLING_FREQUENCY; i++) {
      unsigned int avgB = 0, avgR= 0;
      for (int j = 0; j < NUM_SAMPLES; j++) {
        avgB += analogRead(BATTERY_PIN);
        avgR += analogRead(RESISTOR_PIN);
      }
      valB = (double)avgB / (double)NUM_SAMPLES;
      valR = (double)avgR / (double)NUM_SAMPLES;
      bat_voltage = valB * .0049; 
      res_voltage = valR * .0049; 
      double current = ((res_voltage - bat_voltage) * CORRECTION_FACTOR) / .527778;
      Serial.print(valB);//bat_voltage * CORRECTION_FACTOR);
      //Serial.print(bat_voltage * CORRECTION_FACTOR);
      Serial.print("\t");
      Serial.print(current);
      Serial.println(); // Ends the line
      
      delay(1000 / SAMPLING_FREQUENCY);
    }
    Serial.println("DONE");

  }
}
