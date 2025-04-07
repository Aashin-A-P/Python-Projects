import pyautogui
import time
import sys
from PIL import Image
import mss

def take_screenshot():
    try:
        # Use mss to take a screenshot and save it to a temporary file
        screenshot_path = "/tmp/screenshot.png"
        with mss.mss() as sct:
            sct.shot(output=screenshot_path)
        return Image.open(screenshot_path)
    except Exception as e:
        print(f"Error taking screenshot: {e}")
        print("Ensure you are running an X11 session or have granted screen capture permissions.")
        sys.exit(1)

def listen_and_reply():
    print("Listening for incoming messages...")
    while True:
        try:
            # Wait for a short duration to avoid excessive CPU usage
            time.sleep(1)

            # Take a screenshot of the screen
            screenshot = take_screenshot()

            # Locate the new message indicator (you may need to customize this)
            new_message_location = pyautogui.locateOnScreen('new_message_indicator.png', confidence=0.8)
            if new_message_location:
                print("New message detected!")

                # Click on the new message to open it
                pyautogui.click(new_message_location)

                # Wait for the message to load
                time.sleep(2)

                # Select the last message (you may need to customize this)
                pyautogui.moveTo(500, 500)  # Adjust coordinates as needed
                pyautogui.click()

                # Copy the message
                pyautogui.hotkey('ctrl', 'c')
                time.sleep(1)
                received_message = pyautogui.paste()

                print(f"Received message: {received_message}")

                # Reply with the same message
                pyautogui.typewrite(received_message)
                pyautogui.press('enter')

                print("Replied with the same message.")
        except Exception as e:
            print(f"Error: {e}")
            print("Ensure that the script is configured correctly.")
            sys.exit(1)

if __name__ == "__main__":
    listen_and_reply()
