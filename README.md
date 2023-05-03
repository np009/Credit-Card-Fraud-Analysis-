## Credit Card Fraud Detection
This project aims to create a machine learning model to detect fraudulent credit card transactions. The dataset used is the Credit Card Fraud Detection dataset from Kaggle.

## Table of Contents
* [Dataset Information](#Datasetinformation)
* [File Description](#description)
* [How to run the project code](#Howtoruntheprojectcode)

## Dataset information
The Credit Card Fraud Detection dataset contains transactions made by credit cards in September 2013 by European cardholders. It includes 492 frauds out of 284,807 transactions, making it a highly unbalanced dataset where the positive class (frauds) accounts for only 0.172% of all transactions.

The dataset contains only numerical input variables which are the result of a PCA transformation. Features V1, V2, … V28 are the principal components obtained with PCA, while the only features which have not been transformed with PCA are 'Time' and 'Amount'. The feature 'Time' contains the seconds elapsed between each transaction and the first transaction in the dataset. The feature 'Amount' is the transaction amount, and feature 'Class' is the response variable and takes the value 1 in case of fraud and 0 otherwise.

## File Description
This repository includes the following files:

* credit-card-fraud-detection.ipynb: a Jupyter notebook containing the project code
* creditcard.csv: the Credit Card Fraud Detection dataset in CSV format
* README.md: a file containing information about the project and instructions on how to run the code

## How to run the project code
To run the project code, follow these steps:

* Clone the repository to your local machine.
* Open the credit-card-fraud-detection.ipynb file in Jupyter notebook.
* Run the code cells to train and test the machine learning models.
* The AUPRC scores for each model will be displayed in the output.

Note: The dataset is provided in the repository for convenience, but it can also be downloaded from the Kaggle website.



