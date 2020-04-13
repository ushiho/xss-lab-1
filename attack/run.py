#!/usr/bin/python3

import sys, os
from attack import Attack


def main(url):
	# app.app.run(host="127.0.0.10", port=5000, debug=True)
	attack = Attack(url)
	payload = '&lt;script&gt;alert("vulnerable");&lt;/script&gt;'

	res = attack.run(payload)
	if res:
		msg = "The app is vulnerable"
	else:
		msg = "You are in good hands"
	return (res, msg)

if __name__ == '__main__':
	if len(sys.argv) > 1:
		print(main(sys.argv[1]))
	else:
		raise ValueError("required parameter: url")