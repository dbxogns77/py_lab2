#!/usr/bin/python

def OCT(x):
	digit = 1
	octnum = 0
	while(x != 0):
		temp = x % 1000
		if(temp == 0): continue

		digit_bin = 1
		binnum = 0
		while(temp != 0):
			binnum += temp%2 * digit_bin		
			temp = (int)(temp/10)
			digit_bin *=2

		octnum += binnum * digit
		x = (int)(x / 1000)
		digit *= 10
	return octnum

def DEC(x):
	digit = 1
	dec = 0
	while(x != 0):
		dec += x%2 * digit
		x = (int)(x/10)
		digit *= 2
	return dec

def HEX(x):
	l=[]
	
	while(x != 0):
		temp = x % 10000
		if(temp == 0): continue

		HEX_digitnum= 0
		digit_bin = 1 

		while(temp != 0):
			HEX_digitnum += temp%2 * digit_bin		
			temp = (int)(temp/10)
			digit_bin *=2
		
		if(HEX_digitnum in range(10, 16)):
			l.insert(0, (chr)(HEX_digitnum+55))
		else: l.insert(0, (chr)(HEX_digitnum+48))

		x = (int)(x / 10000)

	return "".join(l)
