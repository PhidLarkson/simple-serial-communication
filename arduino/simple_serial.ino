// a simple serial communication program to control an LED

// Written on the 6th April 2024 by Prince Larbi

// define the pin for the LED
#define LED_PIN 13

// define the character read from the serial port
char data;

void setup{
  // initialize the serial port
  Serial.begin(9600);
  
  // set the LED pin as an output
  pinMode(LED_PIN, OUTPUT);
}

void loop{
    data = serial.read();

    if (data = '1'){
      digitalWrite(LED_PIN, HIGH);
    }
    else if (data = '0'){
      digitalWrite(LED_PIN, LOW);
    }
    else{
      Serial.println("Invalid input");
    }
}