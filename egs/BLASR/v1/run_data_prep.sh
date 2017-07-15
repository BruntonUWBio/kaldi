#!/bin/bash

. cmd.sh
. path.sh

# This setup was modified from egs/swbd/s5b, with the following changes:
# 1. added more training data for early stages
# 2. removed SAT system (and later stages) on the 100k utterance training data
# 3. reduced number of LM rescoring, only sw1_tg and sw1_fsh_fg remain
# 4. mapped swbd transcription to fisher style, instead of the other way around

set -e # exit on error
has_fisher=false
local/swbd1_data_download.sh /media/storagedrive/ryan/corpora/LDC97S62
# local/swbd1_data_download.sh /mnt/matylda2/data/SWITCHBOARD_1R2 # BUT,

# prepare SWBD dictionary first since we want to find acronyms according to pronunciations
# before mapping lexicon and transcripts
local/swbd1_prepare_dict.sh

# Prepare Switchboard data. This command can also take a second optional argument
# which specifies the directory to Switchboard documentations. Specifically, if
# this argument is given, the script will look for the conv.tab file and correct
# speaker IDs to the actual speaker personal identification numbers released in
# the documentations. The documentations can be found here:
# https://catalog.ldc.upenn.edu/docs/LDC97S62/
# Note: if you are using this link, make sure you rename conv_tab.csv to conv.tab
# after downloading.
# Usage: local/swbd1_data_prep.sh /path/to/SWBD [/path/to/SWBD_docs]
local/swbd1_data_prep.sh /media/storagedrive/ryan/corpora/LDC97S62
# local/swbd1_data_prep.sh /home/dpovey/data/LDC97S62
# local/swbd1_data_prep.sh /data/corpora0/LDC97S62
# local/swbd1_data_prep.sh /mnt/matylda2/data/SWITCHBOARD_1R2 # BUT,
# local/swbd1_data_prep.sh /exports/work/inf_hcrc_cstr_general/corpora/switchboard/switchboard1

# This is adds proper prefixes to the switchboard data so that we can incorporate 
# the patient data properly. 
python ./data_prep_scripts/fix_swbd_spkr-id.py

python ./data_prep_scripts/produce_combined_text.py --train
python ./data_prep_scripts/produce_combined_text.py --test
python ./data_prep_scripts/prep_data.py --train
python ./data_prep_scripts/prep_data.py --test
# The following script is a python script that executes a few bash functions. 
# At first, this seems like more work then necessary, but it allows us to get 
# paths from the same source as the other previous patient data prep scripts.
python ./data_prep_scripts/combine_swbd_patient.py

./utils/utt2spk_to_spk2utt.pl data/train/utt2spk > data/train/spk2utt

./utils/fix_data_dir.sh data/train

utils/prepare_lang.sh data/local/dict_nosp \
  "<unk>"  data/local/lang_nosp data/lang_nosp
