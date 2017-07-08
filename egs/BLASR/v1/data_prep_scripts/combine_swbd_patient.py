import parameter_utils
import subprocess

transcripts_root = parameter_utils.get_transcripts_root()
training_data_dir = parameter_utils.get_training_data_dir()

subprocess.call(["cat", 
	"%s/text_train"%(transcripts_root), 
	">>", 
	"%s/text"%(training_data_dir)])

subprocess.call(["cat", 
	"%s/wav_train.scp"%(transcripts_root), 
	">>", 
	"%s/wav.scp"%(training_data_dir)])

subprocess.call(["cat", 
	"%s/utt2spk_train"%(transcripts_root), 
	">>", 
	"%s/utt2spk"%(training_data_dir)])

subprocess.call(["cat", 
	"%s/segments_train"%(transcripts_root), 
	">>", 
	"%s/segments"%(training_data_dir)])