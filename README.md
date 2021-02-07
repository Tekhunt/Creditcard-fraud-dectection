
# Credit Card Fraud Detection using Azure Machine Learning
Fraud detection in financial transactions is one of the most important problems in financial companies.
![torch](https://user-images.githubusercontent.com/65784601/107155162-1b997a80-6977-11eb-9f83-18592722559d.jpg)
This project aims to detect potential fraud cases is credit card transactions and the task here is to differentiate between them. My ultimate intent is to tackle this situation by building classification models to classify and distinguish fraud transactions.
![step](https://user-images.githubusercontent.com/65784601/107155161-1a684d80-6977-11eb-9c10-0709a37f2aac.jpg)
Here I trianed models using AutoML and Hyperdrive after which I deployed the best model which in the case is the AutoML model

#### Steps from data acquisition to model deployment.
![flow1](https://user-images.githubusercontent.com/65784601/107155333-1983eb80-6978-11eb-882a-7981b906c914.png)



## Dataset

The original dataset is in [Kaggle Datasets.](https://www.kaggle.com/mlg-ulb/creditcardfraud)
The original data is licensed by Open Database License (ODbL) 1.0.[Open Database License (ODbL) 1.0.](https://opendatacommons.org/licenses/dbcl/1.0/)

This data is about fraud detection in credit card transactions. The data was made by credit cards in September 2013 by European cardholders. The dataset is highly unbalanced, the positive class which depicts fraudulent transactions (frauds) account for 0.17% of all transactions.

It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we do not have the original features and more background information about the data. Features V1, V2, ... V28 are the principal components obtained with Principal component analysis (PCA), the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-senstive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise."

#### Here goes my

### Task
This project aims to detect potential fraud cases is credit card transactions and the task here is to differentiate between them. My ultimate intent is to tackle this situation by building classification models to classify and distinguish fraud transactions. Detecting potential frauds so that customers are not charged for items that they did not purchase is the key objective of this project. So the goal is to build a classifier that tells if a transaction is a fraud or not.

### Access
The data is first loaded into this project repository and through this [link](https://media.githubusercontent.com/media/Tekhunt/Creditcard-fraud-dectection/master/fraud-data.csv) which points to the raw data in my repository I accessed it in different notebooks and scripts where it was used.

## Automated ML
##### Image below shows the AML Congiguration and Settings used in this project.
![aml settings](https://user-images.githubusercontent.com/65784601/107156857-045f8a80-6981-11eb-838f-a80efd9c39c2.png)

### n_cross-validation
How many cross validations to perform when user validation data is not specified.

### enable_early_stopping
Whether to enable early termination if the score is not improving in the short term. The default is False but it is set to True here.

### experiment_timeout_minutess
Maximum amount of time in minutes that all iterations combined can take before the experiment terminates.
It is set to 15 minutes here.

### verbosity
This is the verbosity level for writing to the log file and it is set to logging.INFO

### training_data 
This can be any of these: DataFrame or Dataset or DatasetDefinition or TabularDataset
The training data to be used within the experiment. It should contain both training features and a label column (optionally a sample weights column). If training_data is specified, then the label_column_name parameter must also be specified. 

### label_column_name
This is the name of the label column. If the input data is from a pandas.DataFrame which doesn't have column names, column indices can be used instead, expressed as integers.
Here we have column headers and our arget column is the Class column which we aim to predict in the project.

### max_cores_per_iteration
The maximum number of threads to use for a given training iteration. Acceptable values:
Equal to -1, which means to use all the possible cores per iteration per child-run.

### max_concurrent_iterations
Represents the maximum number of iterations that would be executed in parallel. The value used here is 4 

### compute_target
The Azure Machine Learning compute target to run the Automated Machine Learning experiment on.

### primary_metric
The metric that Automated Machine Learning will optimize for model selection. Accuracy is the primary_metric here.

### task
The type of task to run. Values the here is 'classification'

### Results

The votingEmsemble gave the best model with an accuracy of 0.9996. The data used in this experiment is highly skewed and i suggest that in the futere beter ways of handling this  kind of skeed dataset should be applied o further improve the model. Additionally, employinhg deep model algorithm will yield significanrt imprrovement, so I highly recommend it.

![run1](https://user-images.githubusercontent.com/65784601/107157936-3d9af900-6987-11eb-920b-b7a81aad7a71.png)
![service](https://user-images.githubusercontent.com/65784601/107157941-44297080-6987-11eb-953c-3eb37a2cb122.png)


*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
