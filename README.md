# Ultrasonic Distance Measurement with LEDs & Buzzer 🚀

This project measures distance using an **HC-SR04 Ultrasonic sensor** and provides visual and sound feedback using **three LEDs (Red, Yellow, Green)** and a **buzzer**.
The system is built using an Arduino/ESP32 microcontroller.

It can be used for:
- Obstacle detection
- Parking assistance
- Smart home proximity sensing
- Safety distance alerts

---

## 🛠️ Components

- **Arduino Uno / ESP32**
- **Ultrasonic Sensor HC-SR04**
- **LED Rouge (Red)**
- **LED Jaune (Yellow)**
- **LED Verte (Green)**
- **Buzzer** (active or passive)
- **Resistor 220Ω** (for each LED)
- Jumper wires
- Breadboard

---
## ⚙️ System Logic

The system responds depending on measured distance:

| Distance (cm) | LED ON    | Buzzer |
|---------------|---------- |--------------|
| **< 15 cm**   | 🔴 Red   | Continuous |
| **15–30 cm**  | 🟡 Yellow| Intermittent |
| **> 30 cm**   | 🟢 Green | Off |

---

## 🧩 Features

- Real-time distance measurement
- Multi-LED visual indicator (Red/Yellow/Green)
- Buzzer alert based on proximity
- Clean modular code
- Suitable for beginners & embedded students

---

## 📷 Demo Video
👉 [Click here to watch the demo](https://youtu.be/8T2ko5rrej0?si=bm6-uwy7ceylWj8C)
---

## 📡 Wiring Diagram
- Ultrasonic Sensor:
    -VCC → 3.3V (or 5V for Arduino)
    -GND → GND
    -TRIG → GPIO 5 ( Pin 9 for Arduino)
    -ECHO → GPIO 18 ( Pin 10 for Arduino)

-LEDs:
    -Red LED → GPIO 14 (with 220Ω resistor) ( Pin 7 for Arduino)
    -Yellow LED → GPIO 27 (with 220Ω resistor) ( Pin 6 for Arduino)
    -Green LED → GPIO 26 (with 220Ω resistor) ( Pin 5 for Arduino)

-Buzzer:
   -Buzzer → GPIO 12 ( Pin 8 for Arduino)

---

## 💻 Code

See the code in the file:
for Arduino  `ultrasonic_led_buzzer.ino`
or 
for ESP32  `ultrasonic.py`

---

## 📈 How It Works

1. The ultrasonic sensor sends a pulse and measures the return time.
2. The microcontroller converts time → distance.
3. According to distance:
- Red LED + buzzer ON
- Yellow LED ON + buzzer blinking
- Green LED ON
4. Results are printed in Serial Monitor.

---

## 📝 Future Improvements

- Add an OLED display
- Add MQTT or WiFi using ESP32
- Add temperature compensation
- Use PWM for buzzer melody

---

## 👩‍💻 Author

**Ala Toumi**
3rd-year Computer Engineering Student
Embedded Systems & IoT enthusiast

---

## 📎 License

MIT License – Free to use and modify.
