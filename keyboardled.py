import pyautogui
import time

# Function to convert text to binary
def text_to_binary(file_path):
    binary_data = []
    
    # Open the file and read the data
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    # Process each line in the file
    for line in lines:
        line = line.strip()  # Remove any leading/trailing whitespace
        # Convert each character to binary and join with a space
        binary_line = ' '.join(format(ord(char), '08b') for char in line)
        binary_data.append(binary_line)
        
    # Return the binary data as a single string
    return ' '.join(binary_data)  # Join the list into a single string with spaces

# Mapping of binary to corresponding LED keys
led_keys = {
    '0': 'numlock',     # Use Num Lock for '0'
    '1': 'capslock',    # Use Caps Lock for '1'
}

# Function to blink an LED for 0.1 seconds
def blink_led(led):
    print(f"Blinking {led} for 0.1 sec")  # Debugging print statement
    pyautogui.press(led)  # Toggle the LED (press the key)
    time.sleep(0.1)       # Keep LED on for 0.1 seconds
    pyautogui.press(led)  # Toggle the LED back off
    time.sleep(0.1)       # Small delay before moving to the next bit

# Function to transmit binary string via keyboard LEDs
def transmit_binary(binary_str):
    binary_chunks = binary_str.split()  # Split binary string into chunks
    print(f"Binary chunks: {binary_chunks}")  # Debugging print statement

    for chunk in binary_chunks:
        print(f"Processing chunk: {chunk}")  # Debugging print statement
        for bit in chunk:
            led = led_keys[bit]  # Get corresponding LED for the bit
            print(f"Transmitting bit: {bit}, blinking {led}")  # Debugging print statement
            blink_led(led)       # Blink the corresponding LED for 0.1 sec

        print("Chunk transmission complete.\n")  # Debugging print statement
        time.sleep(0.5)  # Delay between binary chunks (optional)

# Convert the text from the file to binary
binary_string = text_to_binary("data.txt")

# Transmit the binary message
if binary_string:  # Ensure binary_string is not empty
    print("Starting transmission...")
    transmit_binary(binary_string)
    print("Transmission complete.")
else:
    print("No data found to transmit.")
