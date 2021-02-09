
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

It contains only numerical input variables which are the result of a PCA transformation. Unfortunately, due to confidentiality issues, we do not have the original features and more background information about the data. Features V1, V2, ... V28 are the principal components obtained with Principal component analysis (PCA), the only features which have not been transformed with PCA are 'Time' and 'Amount'. Feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction Amount, this feature can be used for example-dependant cost-senstive learning. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.

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
It is set to 5 minutes here.

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

![run_id_LI](https://user-images.githubusercontent.com/65784601/107300600-2426a980-6a7a-11eb-981c-29f7a8990f09.jpg)
### RunDetails output
![run details](https://user-images.githubusercontent.com/65784601/107300610-27219a00-6a7a-11eb-9f88-c7252f05522d.png)

![aml run id_LI](https://user-images.githubusercontent.com/65784601/107300622-2d177b00-6a7a-11eb-8612-f45f60e391d4.jpg)
![aml run id](https://user-images.githubusercontent.com/65784601/107300624-2ee13e80-6a7a-11eb-97fa-42dd1c1291dc.png)
### View in Azure Ml Studio

![view in azure](https://user-images.githubusercontent.com/65784601/107301089-06a60f80-6a7b-11eb-8ad4-4d88b952955e.png)



## Hyperparameter Tuning








![hyperdrive settings](https://user-images.githubusercontent.com/65784601/107300124-276d6580-6a79-11eb-8acf-7b2d6aceed5c.png)
LogisticRegression is the algorithm used in this classification task. The algorithm is a two class classification to predict between two categories(fraudulent or not fraudulent). And To improve the model we optimized the hyperparameters using the powers of Azure Machine Learning's Hyperdrive

The hyperparameter space defined implies tuning the C and max_iter parameters. Random sampling, which supports discrete and continuous hyperparameters was used and the primary metric to optimize was accuracy and the the goal was to maximize.

Early termination policy was Bandit Policy and the parameters are slack_factor and evaluation_interval. A slack factor equal to 0.1 as criteria for evaluation to conserve resources by terminating runs where the primary metric is not within the specified slack factor/slack amount compared to the best performing run.
Once completed we create the SKLearn estimator

I then defined the hyperdrive configuration and submitted the experiment

### Results
The best model gave an accuracy of 0.998.
![hyperdrive run details](https://user-images.githubusercontent.com/65784601/107300111-1de3fd80-6a79-11eb-8955-8a3974ace771.png)
![metrics](https://user-images.githubusercontent.com/65784601/107300118-23414800-6a79-11eb-83b2-ebb76e5cadcb.png)


![hyperdriverun id](https://user-images.githubusercontent.com/65784601/107300156-3522eb00-6a79-11eb-8a47-fc7d240cc4b0.png)

##### The best model was generated using Regularization strenght of '100.0', max_iter = '250' which gave an accuracy of '0.9988' as shown in the screenshot below.
![run_info](https://user-images.githubusercontent.com/65784601/107300178-40761680-6a79-11eb-91d7-51268cb03b71.png)
![run_info_LI (2)](https://user-images.githubusercontent.com/65784601/107300185-44a23400-6a79-11eb-9055-aff269f66361.jpg)

### View in Azure ML Studio
![azure details](https://user-images.githubusercontent.com/65784601/107300131-2b00ec80-6a79-11eb-9ed8-fbaac539153f.png)

This experiment can be improved using a different algorithm, using differnet features and also adding more iteration in the hyperdrive configuration which can deliver a better result.


## Model Deployment
Below are screenshots which demonstratethe overview of the deployed model and instructions on how to query the endpoint with a sample input.
### Save and register the best model for the deployment
### Download the conda
### set the environment
### and set the inference config and the Aci Web service config

##




##
![save download model](https://user-images.githubusercontent.com/65784601/107313418-c488c800-6a92-11eb-9b33-a0cfb67b6f49.png)
![register model](https://user-images.githubusercontent.com/65784601/107313422-c6eb2200-6a92-11eb-8b15-f8982a976b08.png)

![deploy model](https://user-images.githubusercontent.com/65784601/107313438-ce123000-6a92-11eb-9125-2161d1ad522a.png)
### download the scoring uri and swagger uri
![deployed model](https://user-images.githubusercontent.com/65784601/107313434-cbafd600-6a92-11eb-9e8f-b69e9628818a.png)
### Extract sample data
![sample data](https://user-images.githubusercontent.com/65784601/107313443-d1a5b700-6a92-11eb-9344-ad96ffa82ac4.png)

### Experiment Output


![request output](https://user-images.githubusercontent.com/65784601/107313449-d5d1d480-6a92-11eb-8600-328e3bee7d87.png)

## Screen Recording
https://youtu.be/wJ5l3GzWEVM
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response
