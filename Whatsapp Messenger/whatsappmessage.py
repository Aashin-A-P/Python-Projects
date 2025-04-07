import pywhatkit as pwk

# Define recipient's phone number (with country code)
phone_number = "+916374560135"  # Replace with the recipient's number

# Define message
message = "Hello! This is an automated message sent using Python."

hours = 19
minutes = 00

# Send the message
pwk.sendwhatmsg(phone_number, message,hours,minutes)

print("Message Scheduled Successfully!")
