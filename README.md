# Android-Things
A cool parking sensor

  Project Description
Imagine a tiny smart helper that watches the space around it, ready to light up the moment something gets too close.
That’s what this project is all about—a little system that notices when someone or something comes near and responds with a simple light.
Built around a Raspberry Pi, it quietly keeps an eye out, like a digital guard dog with a flashlight.
It’s the kind of thing you could use to make your front door more interactive, add a fun feature to a display,
or even help with parking in tight spaces. It’s simple, reliable, and full of potential. And the best part?
It’s a great way to dive into the world of building smart things with just a few easy-to-find parts.

  Schema
```
Raspberry Pi 5             HC-SR04 Sensor             LEDs + Resistors
+-------------------------+      +------------+       +------------------------+
| Pin 2  (5V) O---------->|----->| VCC        |       |                        |
| Pin 6  (GND)O---------->|----->| GND        |       |                        |
|                         |      |            |       |                        |
| Pin 11 (GPIO17) O------>|----->| Trig       |       |                        |
| Pin 13 (GPIO27) O<------|<-----| Echo       |       |                        |
|                         |      +------------+       |                        |
| Pin 22 (GPIO25) O------>|------------------------->[R1]--->|>|(LED1)--+      |
|                         |                           330ohm            |      |
| Pin 18 (GPIO24) O------>|------------------------->[R2]--->|>|(LED2)--+      |
|                         |                           330ohm            |      |
| Pin 16 (GPIO23) O------>|------------------------->[R3]--->|>|(LED3)--+      |
|                         |                           330ohm            |      |
| Pin 15 (GPIO22) O------>|------------------------->[R4]--->|>|(LED4)--+      |
|                         |                           330ohm            |      |
|                         |                                             |      |
| Pin 9  (GND) O----------|<--------------------------------------------+------|--(Common GND for LEDs)
| ...                     |                                             |
+-------------------------+                                             +------+
```

Ultrasonic Proximity Detection System – Quick Component Guide
(Updated: April 14, 2025)

Here’s a quick overview of all the parts used in the project, along with useful links and model info for easy sourcing or research.

🧰 Hardware Components
🔌 Raspberry Pi 5
• Model: Raspberry Pi 5 (Model B)
• 📘 Product Page (https://www.raspberrypi.com/products/raspberry-pi-5/)

📡 Ultrasonic Sensor
• Model: HC-SR04
• 📄 Datasheet (SparkFun) (https://cdn.sparkfun.com/datasheets/Sensors/Proximity/HCSR04.pdf)
• ℹ️ Alternative Info (Cytron) (https://www.cytron.io/search?search=hc+sr04+ultrasonic+ranging+module)

💡 LEDs
• Model: Standard 5mm Through-Hole (any color)
• 💡 LED Basics (https://learn.sparkfun.com/tutorials/light-emitting-diodes-leds/all)

🔩 Resistors
• Model: 330Ω, 1/4 Watt, Axial Lead (5% tolerance)
• 🧪 Resistor Basics (https://learn.sparkfun.com/tutorials/resistors/all)

🧱 Breadboard
• Model: Standard Solderless Breadboard (400-830 point)
• 📘 Breadboard Tutorial (https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all)

🔗 Jumper Wires
• Model: Dupont-style (Male–Male, Male–Female, Female–Female, ~10–20cm)
• 🧰 Example Jumper Wires (https://www.adafruit.com/category/105)

💻 Software Components
🧠 Operating System
• Name: Raspberry Pi OS (based on Debian Bookworm or newer) https://www.raspberrypi.com/software/operating-systems/
• 🖥️ OS Download

🐍 Programming Language
• Name: Python 3 (https://www.python.org/)
• 📘 Python Homepage

🔌 GPIO Control Library
• Main Library: gpiozero
• 📘 gpiozero Docs (https://gpiozero.readthedocs.io/en/stable/)
• Backend Libraries:
• lgpio → ℹ️ lgpio Info (https://abyz.me.uk/lg/py_lgpio.html)
• RPi.GPIO → 🔗 RPi.GPIO PyPI (https://pypi.org/project/RPi.GPIO/)

💡 Note: Some components—like resistors and LEDs—don’t have strict model numbers, so the links are to general guides or examples. Specs may vary slightly between vendors.

🚧 Build & Setup Guide
🔧 Step 1: Gather Your Components
Raspberry Pi 5 (with OS installed and internet access)

HC-SR04 ultrasonic sensor

5mm LED + 330Ω resistor

Breadboard + jumper wires (M-M, M-F)

1kΩ and 2kΩ resistors (for voltage divider)

USB-C power supply, HDMI monitor, keyboard, and mouse (for setup)

🔌 Step 2: Wiring Setup
HC-SR04 to Pi:

VCC → Pi 5V

GND → Pi GND

TRIG → GPIO pin (e.g., GPIO 23)

ECHO → Voltage divider → GPIO pin (e.g., GPIO 24)

Voltage Divider (ECHO protection):

ECHO → 1kΩ → GPIO

GPIO side of 1kΩ → GND through 2kΩ

LED Circuit:

Long leg (anode) → 330Ω → GPIO (e.g., GPIO 18)

Short leg (cathode) → GND

🖥️ Step 3: Software Configuration
Boot Raspberry Pi OS (latest version)

Open terminal and install libraries:

bash
Copy
Edit
sudo apt update
sudo apt install python3-gpiozero python3
Create your Python file:

bash
Copy
Edit
nano proximity_alert.py
Paste your proximity detection script (using gpiozero or custom RPi.GPIO if needed)

✅ Step 4: Final Check
Ensure all wires are snug and components are placed securely

Save and exit your script with Ctrl + X, Y, then Enter

▶️ Running the Project
🟢 Step 1: Run the Program
In the terminal, run:

bash
Copy
Edit
python3 proximity_alert.py
👀 Step 2: Observe Behavior
If an object comes closer than 50cm, the LED lights up

If not, the LED stays off

🔄 Step 3: Stop & Reset
Use Ctrl + C to stop the script

GPIOs are cleaned up automatically (if handled in code)

🛠️ Tips & Troubleshooting
No LED? Double-check GPIO numbers and resistor connections

Wrong distances? Confirm sensor angle and clean surfaces

Errors? Add print statements to debug in the script
