# Wine Quality Prediction with MLflow

# End-to-end-Machine-Learning-Project-with-MLflow

This project demonstrates wine quality prediction using machine learning techniques and manages the experiment tracking using MLflow. The dataset contains various features related to the chemical composition of wines and their corresponding quality ratings.

# Table of Contents

Introduction
Features
Technology Used
Installation
MLflow Tracking
AWS CICD Deployment with Github Actions
Preview of Wine Quality Prediction in Action
License


# Introduction

In this project, we utilize machine learning algorithms to predict the quality of wines based on their chemical attributes. MLflow is used to manage the end-to-end machine learning lifecycle, including experiment tracking, model development, and deployment.

# Features

The Wine Quality Prediction model utilizes a set of chemical attributes as features to predict the quality of wines. The features used in this project include:

Fixed Acidity: The amount of fixed acids in the wine.
Volatile Acidity: The amount of volatile acids in the wine, which contribute to its odor.
Citric Acid: The amount of citric acid present in the wine.
Residual Sugar: The amount of residual sugar left after fermentation.
Chlorides: The level of salt present in the wine.
Free Sulfur Dioxide: The amount of sulfur dioxide that is not bound to other molecules.
Total Sulfur Dioxide: The total amount of sulfur dioxide in the wine.
Density: The density of the wine.
pH: The pH level, which indicates the acidity or alkalinity of the wine.
Sulphates: The amount of sulfur compounds present in the wine.
Alcohol: The alcohol content of the wine.
These features are used to train the machine learning model and make predictions about the quality of the wine. The dataset containing these features has been preprocessed and split into training and testing sets for model training and evaluation.


# Technology used

This project leverages various technologies to achieve its goals:

Programming Language: Python

MLflow: MLflow is employed for experiment tracking, model versioning, and deployment. It allows us to seamlessly manage the end-to-end machine learning lifecycle.

Dagshub: Dagshub is used for experiment tracking and collaboration, providing an integrated platform to log experiments and share results.

FastAPI: A modern, fast web framework for building APIs with Python.

Docker: A platform to develop, ship, and run applications in containers.

Amazon Web Services (AWS): A cloud computing platform that provides various services and tools to facilitate deployment and management of applications.

AWS Identity and Access Management (IAM): Used to manage access to AWS resources securely.
Elastic Container Registry (ECR): A managed container registry to store, manage, and deploy Docker container images.
Amazon Elastic Compute Cloud (Amazon EC2): Provides scalable compute capacity in the cloud, often used to host applications and services.
These technologies collectively enable us to efficiently develop, evaluate, and deploy machine learning models for wine quality prediction.



# Steps to run

Clone the repository:

git clone https://github.com/sanjana-v/Wine-Quality-ML-Flow-.git

Navigate to the project directory:

cd Wine-Quality-Prediction-with-MLflow

Create a conda environment after opening the repository:

conda create -n mlops python=3.8 -y

Activate the conda environment:

conda activate mlops

Install the required dependencies:

pip install -r requirements.txt

Finally, run the following command to start the application:

python app.py

Open your preferred web browser and visit:

http://localhost:8080



# MLflow Tracking

To integrate MLflow tracking with dagshub, follow these steps:

Log in to dagshub and connect your account to GitHub.
Connect to your repository and add access.
Click on the selected repository for the project name and connect to it.
Go to "Remote" and click on "Experiment".
Copy the MLflow training command provided.
MLFLOW_TRACKING_URI=https://dagshub.com/sanjana-v/Wine-Quality-ML-Flow-.mlflow
MLFLOW_TRACKING_USERNAME=sanjana-v 
MLFLOW_TRACKING_PASSWORD=9a195bb9e7d4b8f35a21d054c7d379007e630914
python script.py
Make changes in the "export as env variables" command according to your information:

Run this to export as env variables:

export MLFLOW_TRACKING_URI=https://dagshub.com/sanjana-v/Wine-Quality-ML-Flow-.mlflow \

export MLFLOW_TRACKING_USERNAME=sanjana-v \

export MLFLOW_TRA

# Preview of Wine Quality Prediction in Action


![Alt text](<Screenshot 2024-01-05 at 8.13.39 PM.png>)


![Alt text](<Screenshot 2024-01-05 at 8.12.08 PM.png>)