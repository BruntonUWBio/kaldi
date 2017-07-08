import ConfigParser
import sys

def validate_test_train_args(args):
	"""Given a ConfigParser, this returns the args. Along the way it validates that one and only 
	one of the flags '--test' and '--train' is set. If is not satisfied, it fails."""
	if (not (args.test ^ args.train)):
		print("Either --train or --test must be included")
		sys.exit(1)

	return args

def get_transcripts_root(config_file="settings.config"):
	config = ConfigParser.ConfigParser()
	config.read(config_file)

	try:
		return config.get('DEFAULT','TranscriptsPath')

	except KeyError:
		print("TranscriptsPath must be set in settings.config")
		sys.exit(1)