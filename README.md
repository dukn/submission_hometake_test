# Submission of takehome test

## Overview

This repository contains the solution for the takehome test, which involves forecasting the total amount of products sold in every shop for a given test set using historical sales data. 
The solution is divided into two main tasks:

1. **Modeling**: Data processing, analysis, modeling, and evaluation.
2. **Deployment**: Deploying the model to internal users via a web application.

## Task 1: Modeling

The solution involves the following steps:
1. **Data Loading**: Load the datasets using pandas.
2. **Data Exploration and Cleaning**: Explore the data and clean it by handling missing values and outliers.
3. **Feature Engineering**: Create new features that might help in improving the model's performance.
4. **Model Training**: Train an XGBoost model to predict the monthly sales.
5. **Model Evaluation**: Evaluate the model's performance using appropriate metrics.

The detailed implementation can be found in the `task1_solution.ipynb` notebook.

## Task 2: Deployment

### Summary

### Solution

To deploy this model for internal users. 

I believe that pre-calculating and showing pre-calculated results is suitable for the problem. 
- The input only changes every month, so the model only needs to run once a month.
- Pre-computing the results also makes querying and returning results faster, skipping the feature calculation and model inference time.

The API will be built on Flask library to simplify development and deployment. 
The pre-calculated results in the submission.csv file will be loaded into the API and return as a webform.

The solution involves the following steps:
1. **Flask Application**: Create a Flask application to serve the model.
2. **Web Interface**: Create a simple web interface using HTML.
3. **Model Integration**: Integrate the output of the model with the Flask application to provide predictions.

The detailed implementation can be found in the `task2_backend.py` file.

### Running the Application

To run the Flask application, execute the following command:

```sh
python task2_backend.py
```

The application will be available at http://127.0.0.1:5000/
