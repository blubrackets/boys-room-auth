import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)

good = 12
bad = 11

on = GPIO.HIGH
off = GPIO.LOW

GPIO.setup(good, GPIO.OUT)
GPIO.setup(bad, GPIO.OUT)

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def go():
	while True:
		password = input('Password: ')
	
		if password == 'boyroom':
			GPIO.output(good, on)
			GPIO.output(bad, off)
		if password != 'boyroom':
			GPIO.output(bad, on)
			GPIO.output(good, off)
	
		sleep(5)
		GPIO.output(good, off)
		GPIO.output(bad, on)

if __name__ == '__main__':
    go()
    GPIO.cleanup()
