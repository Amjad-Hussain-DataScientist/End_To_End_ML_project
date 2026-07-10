# End-to-End Machine Learning Project: Writing Score Prediction

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![AWS](https://img.shields.io/badge/AWS-Cloud-yellow)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-success)
![License](https://img.shields.io/badge/License-MIT-green)

### *An end-to-end machine learning project that predicts writing score using supervised Regression learning. The project follows a production-ready architecture with Docker, CI/CD, AWS deployment. And The entire project is build using python version 3.13.5*

## **live Demo** 
### No live demo is deployed, see Deployment Status below for why, but you can pull and run the full app locally in one command using docker:
docker pull engrabuhassan/mlproject:v2
docker run -p 5000:5000 engrabuhassan/mlproject:v2
and then run **http://localhost:5000** for home page and for prediction **http://localhost:5000/prediction**

## **Table of Contents**
1. Problem Statement
2. Dataset
3. Tech Stack
4. Project Architecture
5. Model Performance
6. Deployment Status
7. Screenshots
8. Installation & Local Setup
9. Usage / API
10. CI/CD Pipeline
11. Future Improvements
12. Author

1. ## **Problem Statement**

Educators often lack early, data driven information to identify students who may need additional academic support. This project builds a regression model that predicts a student's writing score based on demographic and academic features (gender, parental education level, lunch type, test preparation course, math and reading score). The goal is to demonstrate a full production ML lifecycle  from raw data to a deployed, containerized web application rather than just a notebook experiment.

2. ## **DataSet**



3. ## **Tech Stack**

| Category         | Technology               |
| ---------------- | -------------------      |
| Language         | Python                   |
| ML               | Scikit-Learn             |
| Data Handling    | Pandas, Numpy            |
| Visualization    | Matplotlib, Seaborn      |
| Web Framework    | Flask                    |
| Frontend         | HTML/CSS                 |
| Containerization | Docker                   |
| Cloud            | AWS                      |
| CI/CD            | GitHub Actions           |
| ContainerRegistry| Amazon ECR               |
| Deployment       | EC2,ECR,Elastic BeanStalk|
| Version Control  | Git  & GitHub            |


4. ## **Project Architecture**

### **Overview**
The project follows a modular, end-to-end machine learning pipeline architecture designed for scalability, reproducibility, and deployment. The system is built using Python and follows industry best practices for machine learning projects.

### **Components**
1. **Data Ingestion**: Responsible for loading the raw data from the source (CSV file) and splitting it into training and testing datasets.
2. **Data Transformation**: Handles data cleaning, feature engineering, and preprocessing steps such as encoding categorical variables and scaling numerical features.
3. **Model Training**: Trains machine learning models (using Scikit-learn) on the processed data and evaluates their performance.
4. **Model Evaluation**: Evaluates the trained models using appropriate metrics ( R-squared score) and selects the best model.
5. **Model Deployment**: Packages the trained model and necessary preprocessing steps into a format suitable for deployment (using Flask for a simple web API).
6. **CI/CD Pipeline**: Uses GitHub Actions to automate testing, building Docker images, and deploying to AWS (EC2/ECR/Elastic Beanstalk).
7. **Monitoring**: Logs and monitors the model's performance in production (though basic logging is implemented).

5. ## **Directory Structure**
```
.
└── End_to_end_Ml_project/
    ├── .ebextensions/          
    │   └── python.config
    ├── .github\workflows/
    │   └── main.yaml
    ├── artifacts/
    │   ├── data.csv
    │   ├── model.pkl
    │   ├── preprocessor.pkl
    │   ├── train.csv
    │   └── test.csv
    ├── notebook/
    │   ├── Data
    │   ├── EDA.ipynb
    │   └── model_training.ipynb
    ├── src/
    │   ├── __init__.py
    │   ├── components/
    │   │   ├── __init__.py
    │   │   ├── data_ingestion.py
    │   │   ├── data_transformation.py
    │   │   └── model_trainer.py
    │   ├── pipeline/
    │   │   ├── __init__.py
    │   │   └── prediction_pipline.py
    │   ├── exception.py
    │   ├── logger.py
    │   └── utils.py
    ├── templates/
    │   ├── home.html
    │   └── index.htm
    ├── .dockerignore
    ├── .gitignore
    ├── application.py
    ├── Dockerfile
    └── README.md 
```

6. ## **Data Flow**
1. Data is ingested from `notebook/Data/students.csv` into the data ingestion component.
2. The data is split into training and testing sets and saved as artifacts.
3. The training data is passed to the data transformation component for preprocessing.
4. The transformed data is used to train the model in the model trainer component.
5. The trained model is saved as an artifact.
6. The prediction pipeline loads the model and preprocessing objects to make predictions on new data.
7. The Flask app (application.py) would use the prediction pipeline to serve predictions via an API.
8. Dockerfile containerizes the application.
9. GitHub Actions workflow builds the Docker image and pushes to Amazon ECR, then deploys to AWS Elastic Beanstalk first and then EC2.

7. ## **Model Performance**
   ### All regressors models which were test and their R2_score:

| Model's Name           | R2_score         |
| ---------------------- | ---------------- |
| Ridge                  | 0.938142         |
| Linear Regression      | 0.938133         |
| XGBRegressor           | 0.922760         |
| CatBoosting Regressor  | 0.915939         |
| Random Forest Regressor| 0.915255         |
| AdaBoost Regressor     | 0.912608         |
| Lasso	0.899408         | 0.899408         |
| K-Neighbors Regressor	 | 0.889659         |
| Decision Tree	         | 0.875626         |
