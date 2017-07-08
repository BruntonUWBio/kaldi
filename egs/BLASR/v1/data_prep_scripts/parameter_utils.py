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
	return _get_config_parameter('TranscriptsPath')

def get_training_data_dir(config_file="settings.config"):
	return _get_config_parameter('TrainingDataPath')


def _get_config_parameter(param, config_file="settings.config"):
	config = ConfigParser.ConfigParser()
	config.read(config_file)

	try:
		return config.get('DEFAULT', param)

	except KeyError:
		print("%s must be set in settings.config"%(param))
		sys.exit(1)