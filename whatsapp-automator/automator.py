import pywhatkit as kit
import time

phone_number = "+91XXXXXXXXXX" #enTER NUMBER WITH COUNTRY CODE 
message = "Hello! This is an automated message."

for i in range(5):
    kit.sendwhatmsg_instantly(phone_number, message, wait_time=15, tab_close=True)
    print(f"Sent message {i+1}")
    time.sleep(20)  
