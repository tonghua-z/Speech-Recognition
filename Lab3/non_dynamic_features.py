import numpy as np
import argparse
from tqdm import tqdm

# Default values for CLI arguments
DEFAULT_FEATURES = 'lmfcc'

def get_arguments():
    """Parse all the arguments provided from the CLI.

    Returns:
      A list of parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Phoneme recognition.")
    parser.add_argument("--feature-type", type=str, default = DEFAULT_FEATURES,
                        help="Type of features to use.")
    return parser.parse_args()

args = get_arguments()

#training_data = np.load("Lab3_files/training_data.npy", allow_pickle=True)
#validation_data = np.load("Lab3_files/validation_data.npy", allow_pickle=True)
testing_data = np.load("Lab3_files/testdata.npy", allow_pickle=True)

'''for sample in tqdm(training_data):
    feature_list = [np.array(feature) for feature in sample[args.feature_type]]
    sample['features'] = np.array(feature_list)

np.save("Lab3_files/lmfcc_nd_training_data.npy", training_data)'''

'''for sample in tqdm(validation_data):
    feature_list = [np.array(feature) for feature in sample[args.feature_type]]
    sample['features'] = np.array(feature_list)

np.save("Lab3_files/lmfcc_nd_validation_data.npy", validation_data)'''

for sample in tqdm(testing_data):
    feature_list = [np.array(feature) for feature in sample[args.feature_type]]
    sample['features'] = np.array(feature_list)

np.save("Lab3_files/lmfcc_nd_test_data.npy", testing_data) 
