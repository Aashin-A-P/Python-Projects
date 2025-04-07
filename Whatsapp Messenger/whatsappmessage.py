import pywhatkit as pwk
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Send a WhatsApp message using Python.")
parser.add_argument("phone_number", type=str, help="Recipient's phone number (with country code).")
parser.add_argument("message", type=str, help="Message to send.")
parser.add_argument("hours", type=int, help="Hour (24-hour format) to send the message.")
parser.add_argument("minutes", type=int, help="Minute to send the message.")
args = parser.parse_args()

# Send the message
pwk.sendwhatmsg(args.phone_number, args.message, args.hours, args.minutes)

print("Message Scheduled Successfully!")
