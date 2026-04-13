from machine import ADC, Pin
from neopixel import Neopixel
import utime

# --- Sensor setup ---
sensor = ADC(Pin(27))  # Force sensor på GP27

# --- NeoPixel setup ---
num_pixels = 5
pixels = Neopixel(num_pixels, 0, 28, "RGB")  # Data på GP28

def set_color(color):
    for i in range(num_pixels):
        pixels.set_pixel(i, color)
    pixels.show()

# --- Farver ---
colors = {
    "none": (0, 0, 0),        # Slukket
    "low": (0, 0, 255),       # Blå
    "medium": (0, 255, 0),    # Grøn
    "high": (255, 255, 0),    # Gul
    "very_high": (255, 0, 0)  # Rød
}

# --- Thresholds (skal justeres!) ---
# Print raw_value først og tilpas disse bagefter
t1 = 5000
t2 = 15000
t3 = 30000
t4 = 50000

# --- Main loop ---
while True:
    raw_value = sensor.read_u16()
    voltage = raw_value * 3.3 / 65535

    print("Raw:", raw_value, "Voltage:", round(voltage, 2), "V")

    # --- Bestem farve ud fra tryk ---
    if raw_value < t1:
        set_color(colors["none"])
    elif raw_value < t2:
        set_color(colors["low"])
    elif raw_value < t3:
        set_color(colors["medium"])
    elif raw_value < t4:
        set_color(colors["high"])
    else:
        set_color(colors["very_high"])

    utime.sleep(0.1)
