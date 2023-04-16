
import os
from pocketsphinx import LiveSpeech

# Set up PocketSphinx configuration
# config = {
#     'verbose': False,
#     'sampling_rate': 16000,
#     'buffer_size': 2048,
#     'no_search': True,
#     'full_utt': False,
#     'hmm': os.path.join(os.getcwd(), 'model/hindi-model/hindi-dic'),
#     'lm': os.path.join(os.getcwd(), 'model/hindi-model/hindi.lm'),
#     'dict': os.path.join(os.getcwd(), 'model/hindi-model/hindi.dic')
# }

config = {
    'verbose': False,
    'sampling_rate': 16000,
    'buffer_size': 2048,
    'no_search': True,
    'full_utt': False,
    'hmm': os.path.join(os.getcwd(), 'model/english-model/en_in.cd_cont_5000'),
    'lm': os.path.join(os.getcwd(), 'model/english-model/en-us.lm.bin'),
    'dict': os.path.join(os.getcwd(), 'model/english-model/en_in.dic')
}

# Create LiveSpeech object
speech = LiveSpeech(**config)

# Loop through speech input and print transcriptions
for phrase in speech:
    print(phrase)