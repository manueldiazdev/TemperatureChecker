import serial
import os
from twilio.rest import Client
import sys
import TwilioTokens
#Configs for UART communication with STM32
ser = serial.Serial ("/dev/serial0",
	baudrate = 38400,
	bytesize = serial.EIGHTBITS,
	parity = serial.PARITY_NONE,
	stopbits = serial.STOPBITS_ONE)

#Keys for API
account_sid = TwilioTokens.account_sid
auth_token = TwilioTokens.auth_token
client = Client(account_sid, auth_token)


text_message = 'You\'re too hot. You\'re temp is'

temp = 0.0
while(1):
	temp_reading = ser.readline().decode('utf-8')
	try:
		temp = float(temp_reading)
		print(temp)
		if temp > 95.5:
			print(f'{text_message} {temp}')
			message = client.api.account.messages.create(
				#User Phonenumber
				to="+(CountryCode)#######", 
				#Twilio's number giving from API
				from_="+(CountryCode)#######", 
        		body = f'{text_message} {temp:.1f} F')
			

	except ValueError:
		print(f'{temp_reading}')
