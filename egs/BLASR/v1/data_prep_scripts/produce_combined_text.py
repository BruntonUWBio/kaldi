import glob
import argparse
import parameter_utils

parser = argparse.ArgumentParser(description='Concatenate a set of transcripts into a single file.')
parser.add_argument('--train', action='store_true', 
	help='Preset for creating training data. Creates a single file from files found in {TranscriptsPath}/train. (See settings.config)')
parser.add_argument('--test', action='store_true',
	help='Preset for creating testing data. Creates a single file from files found in {TranscriptsPath}/test. (See settings.config)')

# TODO: add --path for a more general case.
# TODO: add better error handling. 

args = parser.parse_args()
args = parameter_utils.validate_test_train_args(args)

transcripts_root = parameter_utils.get_transcripts_root()

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
