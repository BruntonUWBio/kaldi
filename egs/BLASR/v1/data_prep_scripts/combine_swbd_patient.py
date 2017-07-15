import parameter_utils
import subprocess
import os
import sys


def line_count(file_name):
	with open(file_name) as file_to_count:
		return sum(1 for _ in file_to_count)

def concatenate_and_sort(incoming_file, destination_file):
	"""This adds the body of the incoming file to the destination file. It then sorts the destination file.
	This is done using shell commands to hopefully be more efficient. """

	# WARNING, subprocess.call can be vulnerable to code injection when using shell=True, hence the following checks
	if (not os.path.exists(incoming_file)):
		print("Incoming file not properly specified!")
		sys.exit(1)

	if (not os.path.exists(destination_file)):
		print("Destination file not properly specified!")
		sys.exit(1)

	in_file_line_num = line_count(incoming_file)
	dest_file_line_num = line_count(destination_file)
	print("Appending\t %d lines, from %s"%(in_file_line_num, incoming_file))
	print("to the\t %d lines in %s"%(dest_file_line_num, destination_file))

	subprocess.call("cat %s >> %s"%(incoming_file, destination_file),
		shell=True)
	subprocess.call("sort %s -o %s"%(destination_file, destination_file),
		shell=True)
	print("Expected \t %d lines"%(in_file_line_num + dest_file_line_num))
	print("Totalled \t %d lines in %s"%(line_count(destination_file), destination_file))

transcripts_root = parameter_utils.get_transcripts_root()
training_data_dir = parameter_utils.get_training_data_dir()

concatenate_and_sort(
	incoming_file = "%s/text_train"%(transcripts_root),
	destination_file = "%s/text"%(training_data_dir)
)
concatenate_and_sort(
	incoming_file = "%s/wav_train.scp"%(transcripts_root),
	destination_file = "%s/wav.scp"%(training_data_dir)
)
concatenate_and_sort(
	incoming_file = "%s/utt2spk_train"%(transcripts_root),
	destination_file = "%s/utt2spk"%(training_data_dir)
)
concatenate_and_sort(
	incoming_file = "%s/segments_train"%(transcripts_root),
	destination_file = "%s/segments"%(training_data_dir)
)

