import os
import parameter_utils

training_data_dir = parameter_utils.get_training_data_dir()

orig_file_name = os.path.join(training_data_dir, 'utt2spk')
fixed_file_name = os.path.join(training_data_dir, 'utt2sp_fixed')

with open(orig_file_name) as utt2spk_old, \
     open(fixed_file_name, 'w') as utt2spk_new:
    for lines in utt2spk_old:
	    uttid = lines.split(' ')[0]
	    spkid = lines.split(' ')[1]
	    utt2spk_new.write(uttid + '\t sw0' + spkid)

os.rename(fixed_file_name, orig_file_name)
print('Fixed switchboard utt2spk file')
