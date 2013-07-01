'''
			IMO.im JSON history to linear log converter.

	By Dean Camera (dean [at] fourwalledcubicle [dot] com)
	Released into the public domain.

	This script converts a IMO.im JSON log into a linear log for a given user
	email address.

	Sample input:

		{
		  "user@example.com": [
		    {
		      "from": "me",
		      "message": "Test message from me to Example User",
		      "timestamp": "2012-11-26 07:21:45",
		      "to": "user@example.com"
		    },
		    {
		      "from": "user@example.com",
		      "message": "Test message from Example User to me",
		      "timestamp": "2012-11-26 07:22:57",
		      "to": "me"
		    }
		}

	Sample output:

		Chat history for 'user@example.com':
		=====================================
		2012-11-26 07:21:45    Me      Test message from me to Example User
		2012-11-26 07:22:57    Them    Test message from Example User to me
		=====================================
'''

import json
import sys

def dump_user_history(log_data, user_email):
	print "\n"
	print "Chat history for '%s':" % user_email
	print "====================================="

	recipients = {"me" : "Them", user_email : "Me"}

	for m in log_data[user_email]:
		formatted_string = "%s\t%s\t%s" % (m['timestamp'], recipients[m['to']], m['message'])
		print formatted_string.encode('ascii', 'ignore')

	print "====================================="


def main():
	if len(sys.argv) < 2:
		print "Usage: python imo_history_dump.py <imo_history_filename> [user_email_to_dump]"
		exit(1)

	imo_history_filename = sys.argv[1]

	try:
		user_email_to_dump = sys.argv[2]
	except:
		user_email_to_dump = None

	with open(imo_history_filename, 'r') as f:
		read_data = f.read()
		json_data = json.loads(read_data)

		if user_email_to_dump is None:
			for u in json_data:
				dump_user_history(json_data, u)
		elif user_email_to_dump in json_data:
			dump_user_history(json_data, user_email_to_dump)
		else:
			print "Specified user '%s' not found in log file." % user_email_to_dump

	f.closed


if __name__ == "__main__":
    main()
