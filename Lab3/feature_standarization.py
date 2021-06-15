import numpy as np
import argparse
from sklearn import preprocessing
# from sklearn.externals import joblib


# Default values for CLI arguments
DEFAULT_TRAIN_PATH = "Lab3_files/lmfcc_d_training_data.npy"
DEFAULT_VAL_PATH =  "Lab3_files/lmfcc_d_validation_data.npy"
DEFAULT_TEST_PATH =  "Lab3_files/lmfcc_d_test_data.npy"
DEFAULT_STATE_LIST_PATH = "Lab3_files/state_list.npy"
DEFAULT_PREPROCESSOR_SAVE_PATH = "Lab3_files/scaler.save"

def get_arguments():
    """Parse all the arguments provided from the CLI.

    Returns:
      A list of parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Phoneme recognition.")
    parser.add_argument("--train-path", type=str, default = DEFAULT_TRAIN_PATH,
                        help="Training input data path.")
    parser.add_argument("--val-path", type=str, default = DEFAULT_VAL_PATH,
                        help="Validation input data path.")
    parser.add_argument("--test-path", type=str, default=DEFAULT_TEST_PATH,
                        help="Test input data path.")
    parser.add_argument("--state-list-path", type=str, default = DEFAULT_STATE_LIST_PATH,
                        help="Training labels data path..")
    parser.add_argument("--preproc-save-path", type=str, default = DEFAULT_PREPROCESSOR_SAVE_PATH,
                        help="Path for saving the standard scaler object.")
    return parser.parse_args()

args = get_arguments()





state_list = list(np.load(args.state_list_path))

# Load training dataset
training_data = np.load(args.train_path, allow_pickle=True)
N = 0
D = np.prod(np.array(training_data[0]['features']).shape[1:3])
for sample in training_data:
    N += sample['features'].shape[0]


X_train = np.zeros((N, D))
y_train = np.zeros((N, 1))
prev_idx = 0
for sample in training_data:
    dynamic_features = np.array(sample['features'])
    n = dynamic_features.shape[0]
    X_train[prev_idx:prev_idx + n] = dynamic_features.reshape((n, D))
    y_train[prev_idx:prev_idx + n, 0] = sample['targets']
    prev_idx += n

# Load validation dataset
validation_data = np.load(args.val_path)
N = 0
for sample in validation_data:
    N += np.array(sample['features']).shape[0]

X_val = np.zeros((N, D))
y_val = np.zeros((N, 1))
prev_idx = 0
for sample in validation_data:
    dynamic_features = np.array(sample['features'])
    n = dynamic_features.shape[0]
    X_val[prev_idx:prev_idx + n] = dynamic_features.reshape((n, D))
    y_val[prev_idx:prev_idx + n, 0] = sample['targets']
    prev_idx += n

# Load test dataset
test_data = np.load(args.test_path)
N = 0
for sample in test_data:
    N += np.array(sample['features']).shape[0]

X_test = np.zeros((N, D))
y_test = np.zeros((N, 1))
prev_idx = 0
for sample in test_data:
    dynamic_features = np.array(sample['features'])
    n = dynamic_features.shape[0]
    X_test[prev_idx:prev_idx + n] = dynamic_features.reshape((n, D))
    y_test[prev_idx:prev_idx + n, 0] = sample['targets']
    prev_idx += n

# Standarize
scaler = preprocessing.StandardScaler().fit(X_train)

X_train = scaler.transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

X_train = X_train.astype('float32')
X_val = X_val.astype('float32')
X_test = X_test.astype('float32')

print(X_train.shape)
print(X_val.shape)
print(X_test.shape)

np.save("final_data/X_train.npy", X_train)
np.save("final_data/X_val.npy", X_val)
np.save("final_data/X_test.npy", X_test)

np.save("final_data/y_train.npy", y_train)
np.save("final_data/y_val.npy", y_val)
np.save("final_data/y_test.npy", y_test)


# joblib.dump(scaler, args.preproc_save_path)
