from sklearn.ensemble import IsolationForest
import numpy as np

# load the dataset of features
X = np.load('program_features.npy')

# create the isolation forest model
model = IsolationForest(n_estimators=100, max_samples='auto', contamination=0.05)

# fit the model to the dataset
model.fit(X)

# predict the anomalies
y_pred = model.predict(X)

# print the anomalies
anomalies = X[np.where(y_pred == -1)]
print(anomalies)