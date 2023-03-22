from sklearn.ensemble import IsolationForest
import numpy as np
import os
import ast
import traceback

# define a function to extract the features from a Python file
def extract_features(filename):
    try:
        with open(filename, 'r') as f:
            node = ast.parse(f.read())
        # extract the features from the AST
        # and return them as a numpy array
        # ...
        # replace this with your code to extract features
        features = np.random.rand(10)
        return features
    except Exception as e:
        print(f"Error while extracting features from {filename}:")
        traceback.print_exc()
        return None

# set the directory containing the Python files
directory = "/path/to/directory"

# get a list of all the Python files in the directory
python_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.py')]

# extract the features for each file and store them in a list
features_list = []
for filename in python_files:
    features = extract_features(filename)
    if features is not None:
        features_list.append(features)

# convert the list of features to a numpy array
X = np.array(features_list)

# create the isolation forest model
model = IsolationForest(n_estimators=100, max_samples='auto', contamination=0.05)

# fit the model to the dataset
model.fit(X)

# predict the anomalies
y_pred = model.predict(X)

# print the anomalies
anomalies = [python_files[i] for i in np.where(y_pred == -1)[0]]
print("Anomalies:")
for filename in anomalies:
    print(filename)



