import json
import sys

if len(sys.argv) != 3:
	print "Usage: python imo_history_dump.py <imo_history_filename> <user_email_to_dump>"
	exit(1)

imo_history_filename = sys.argv[1]
user_email_to_dump   = sys.argv[2]


with open(imo_history_filename, 'r') as f:
	read_data = f.read()
	json_data = json.loads(read_data)

	print "Chat history for '%s':" % user_email_to_dump
	print "====================================="

	recipients = {"me" : "Them", user_email_to_dump : "Me"}

	for m in json_data[user_email_to_dump]:
		formatted_string = "%s\t%s\t%s" % (m['timestamp'], recipients[m['to']], m['message'])
		print formatted_string.encode('ascii', 'ignore')

	print "====================================="

f.closed
