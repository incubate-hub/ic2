# ic2


## Problem Statement

Code Review Bot: Develop a machine learning model that can identify anomalies in code reviews, such as unusual patterns of comments or code changes, and flag them for further investigation. 

#### Short video on the Human Cost of Cyberattacks:
[![Watch video](https://img.youtube.com/vi/1hIlTFG-RsU/mqdefault.jpg)](https://www.youtube.com/watch?v=1hIlTFG-RsU)

## Dataset 

The dataset represents python programs which are used to train the Isolation Forest Algorithm.

## Methodology

The Code review bots use machine learning algorithms to identify patterns in code and make recommendations for improvements. These bots may analyze code syntax, comments, and commit messages to learn about the codebase and provide feedback.

Isolation Forest Algorithm is used for the above problem statement.

Isolation Forest is an unsupervised machine learning algorithm that is used for anomaly detection. It was first introduced in 2008 by Fei Tony Liu, Kai Ming Ting, and Zhi-Hua Zhou. The algorithm is based on the idea of isolating anomalies in a dataset by creating isolation trees.

Here is how the algorithm works:

    Randomly select a subset of data points from the dataset and create a tree structure by recursively splitting the data points along randomly selected features.

    Continue creating trees until all data points are isolated, or until a maximum tree depth is reached.

    To identify anomalies, the algorithm calculates the average path length for each data point across all trees. The average path length is a measure of how many splits are needed to isolate a data point.

    Data points with shorter average path lengths are considered anomalies because they are easier to isolate in the tree structure.

The main advantages of the Isolation Forest algorithm are that it can handle high-dimensional datasets, it is computationally efficient, and it does not require labeled data. The algorithm is also robust to outliers and can detect anomalies in both small and large datasets.

However, the Isolation Forest algorithm may not perform well in datasets where anomalies are densely clustered, and it may struggle to identify anomalies in datasets with low-dimensional feature spaces. Additionally, the algorithm may require some parameter tuning to achieve optimal performance.

# Software Requirements
- Python and its libraries.
- Streamlit Framework.
- Jupyter Notebook.
- Spyder.

## Front End

The project has an interacting working webapp that can be used to detect anomalies in python programs.


To run the webapp you need to enter the following command on your terminal
 
 ```
 streamlit run "/Elite16/Bot/bot.py"
 ```
 
 To work this webapp needs to have Streamlit,chatterbot and pytz installed upon a standard Anaconda installation.
 
 You can install them using:
 ```
 pip install "chatterbot==1.0.0"
 pip install pytz
 pip install streamlit
 ```
 
 


