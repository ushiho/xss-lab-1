#!/usr/bin/python3

import sys, os
from attack import Attack

URL = 'http://127.0.0.1:5000/'
PAYLOAD = '<script>alert("vulnerable")</script>'

def main():
	attack = Attack(URL)

	res = attack.run(PAYLOAD)
	if res:
		msg = "The app is vulnerable"
	else:
		msg = "You are in good hands"
	return (res, msg)

if __name__ == '__main__':
	res = main()
	print(res)