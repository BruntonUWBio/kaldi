import os

with open('../data/train/utt2spk') as utt2spk_old, \
     open('../data/train/utt2spk_fixed', 'w') as utt2spk_new:
    for lines in utt2spk_old:
	    uttid = lines.split(' ')[0]
	    spkid = lines.split(' ')[1]

	    new_u2s.write(uttid + '\t sw0' + spkid)

os.rename('../data/train/utt2spk_fixed', '../data/train/utt2spk')