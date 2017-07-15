import ConfigParser
import sys
import os

default_settings_path = os.path.join(os.path.dirname(__file__), "settings.config")

def validate_test_train_args(args):
	"""Given a ConfigParser, this returns the args. Along the way it validates that one and only 
	one of the flags '--test' and '--train' is set. If is not satisfied, it fails."""
	if (not (args.test ^ args.train)):
		print("Either --train or --test must be included")
		sys.exit(1)

	return args

def get_transcripts_root(config_file=default_settings_path):
	return _validate_is_path(_get_config_parameter('TranscriptsPath', config_file))

def get_training_data_dir(config_file=default_settings_path):
	return _validate_is_path(_get_config_parameter('TrainingDataPath', config_file))


def _validate_is_path(str_to_validate):
	"""We want to be able to use possibily unsafe commands (ex: subprocess.call). Because they are vulnerable to 
	code injection, we want to validate our settings files just in case."""
	if (os.path.exists(str_to_validate)):
		return str_to_validate
	else:
		print("%s is not a valid path"%(param))
		sys.exit(1)


def _get_config_parameter(param, config_file=default_settings_path):
	config = ConfigParser.ConfigParser()
	config.read(config_file)

	try:
		return config.get('DEFAULT', param)

	except KeyError:
		print("%s must be set in settings.config"%(param))
		sys.exit(1)
