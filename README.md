# ELEC-C9821-Design-Thinking-and-Advanced-Prototyping
To run the web application make sure to install Deno on your machine.
Using Shell (macOS and Linux):
    curl -fsSL https://deno.land/x/install/install.sh | sh
Using PowerShell (Windows):
    irm https://deno.land/install.ps1 | iex
Using Scoop (Windows):
    scoop install deno
Using Chocolatey (Windows):
    choco install deno
Using Homebrew (macOS):
    brew install deno
Using MacPorts (macOS): 
    sudo port install deno
Using Nix (macOS and Linux):
    nix-shell -p deno
Build and install from source using Cargo:
    cargo install deno --locked

After downloading Deno, make sure to have a running PostgreSQL database or a equivalent one, and change the credentials in database.js to your own database credentials.
connectionPool = new Pool({
  host: "Your database's host address",
  user: "Your database user",
  database: "Your database name",
  password: "Your database passsword",
  }, CONCURRENT_CONNECTIONS);

After finishing the above steps in terminal, go to the location where app-launch.js are, and run the command:
    deno run --allow-read --allow-write --allow-env --allow-net --unstable app-launch.js
And the application should start running on your localhost at port 7777.

Prerequisites
To use this project, you'll need:

Python 3.6 or higher on both your computer and Raspberry Pi.
A Raspberry Pi with GPIO (General Purpose Input Output) pins.
A LED and resistor to connect to the Raspberry Pi's GPIO pin.
MediaPipe Python library installed on your computer.
OpenCV and Pillow Python libraries installed on your computer.
RPi.GPIO Python library installed on your Raspberry Pi.
Your Raspberry Pi and computer should be on the same network.
Installation
Clone the repository or download the Python scripts.
Install the required Python libraries on your computer:
shell
Copy code
pip install opencv-python mediapipe pillow
Install the required Python libraries on your Raspberry Pi:


pip install RPi.GPIO
Usage
Connect a LED to GPIO 8 (pin 24) of your Raspberry Pi through an appropriate resistor.
Replace 'raspberry_pi_ip' and port in the scripts with the actual IP address and port number of your Raspberry Pi.
Run the Raspberry Pi script on your Raspberry Pi:


python blink.py
python camera.py
Run the computer script on your computer:

python eyes_t.py
The computer script will send a warning message to the Raspberry Pi over the network when the user's eyes are either not visible or closed for over 10 seconds. The Raspberry Pi will then blink the LED connected to its GPIO pin 8.

Note
This system may not be perfect in detecting the status of the user's eyes due to the complex nature of facial landmark detection. It may also be affected by the lighting conditions, the user's distance from the camera, and other factors. The system is meant to serve as a basic demonstration of using computer vision and networking with a Raspberry Pi, and may not be suitable for serious applications without further refinement and testing.
