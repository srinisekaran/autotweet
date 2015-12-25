import config
import sys
from logger import log as log
from twython import Twython

APP_KEY = config.user['APP_KEY']
APP_SECRET = config.user['APP_SECRET']
OAUTH_TOKEN = config.user['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = config.user['OAUTH_TOKEN_SECRET']

f_path = config.file_path

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def get_status():
	with open(f_path, 'r') as f:
		message = f.readlines()
	if not message: # Check if empty message list
		sys.exit(1)
	custom_status = message.pop(0)
	custom_status = custom_status.strip('\n')

	with open(f_path, 'w') as fout: # Remove custom status from text file
		fout.writelines(message)

	return custom_status

@log
def add_content(content): # Supply additional arguments to append to text file
	with open(f_path, 'a') as fin:
		content = ' '.join(content[1:])
		fin.write(content + '\n')

@log
def tweet():
	twitter.update_status(status=get_status())

def main():
	if len(sys.argv) > 1: 
		add_content(sys.argv)
	else:
		while True:
			try:
				tweet()
			except:
				print 'Could not tweet. Retrying next tweet...'
				continue
			break

if __name__ == '__main__':
	main()
