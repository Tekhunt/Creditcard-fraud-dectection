from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
from azureml.core import Dataset 

# TODO: Create TabularDataset using TabularDatasetFactory
# Data is located at:
# "https://media.githubusercontent.com/media/Tekhunt/Creditcard-fraud-dectection/master/fraud-data.csv"


def my_dataset(data):
    
    x_data = data.to_pandas_dataframe().copy()
    y_data = x_data.pop('Class')
    return x_data, y_data



data_path = "https://media.githubusercontent.com/media/Tekhunt/Creditcard-fraud-dectection/master/fraud-data.csv"

### YOUR CODE HERE ###
#data = Dataset.Tabular.from_delimited_files(path=data_path)
data = TabularDatasetFactory.from_delimited_files(path=data_path)

x_data, y_data = my_dataset(data)

# TODO: Split data into train and test sets.

### YOUR CODE HERE ###
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size = 0.3, random_state = 6)

run = Run.get_context()


def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)
    joblib.dump(model, 'outputs/model.joblib')

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))

if __name__ == '__main__':
    main()