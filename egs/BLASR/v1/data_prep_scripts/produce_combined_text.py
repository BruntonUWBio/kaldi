import glob
import argparse
import ConfigParser
import sys

parser = argparse.ArgumentParser(description='Concatenate a set of transcripts into a single file.')
parser.add_argument('--train', action='store_true', 
	help='Preset for creating training data. Creates a single file from files found in {TranscriptsPath}/train. (See settings.config)')
parser.add_argument('--test', action='store_true',
	help='Preset for creating testing data. Creates a single file from files found in {TranscriptsPath}/test. (See settings.config)')

# TODO: add --path for a more general case.
# TODO: add better error handling. 

args = parser.parse_args() # gets args as a dict

if (not (args.test ^ args.train)):
	print("Either --train or --test must be included")
	sys.exit(1)

config = ConfigParser.ConfigParser()
config.read('settings.config')

try:
	transcripts_root = config.get('DEFAULT','TranscriptsPath')

except KeyError:
	print("TranscriptsPath must be set in settings.config")
	sys.exit(1)


if (args.train):
	file_set = glob.glob ("%s/train/*.txt"%(transcripts_root))
	final_file_path = "%s/final_patient_train_data.txt"%(transcripts_root)

else:
	file_set = glob.glob ("%s/test/*.txt"%(transcripts_root))
	final_file_path = "%s/final_patient_test_data.txt"%(transcripts_root)

final_file = open(final_file_path, 'w')

for file_name in file_set:
	with open(file_name, 'r') as file_obj:
		for line in file_obj:
			final_file.write(line)

print("Combined %d files into %s"%(len(file_set), final_file))
