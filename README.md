# End-to-End Machine Learning Project: Writing Score Prediction

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![AWS](https://img.shields.io/badge/AWS-Cloud-yellow)
![GitHub Actions](https://img.shields.io/badge/GitHub-Actions-success)
![License](https://img.shields.io/badge/License-MIT-green)

### *An end-to-end machine learning project that predicts writing score using supervised Regression learning. The project follows a production-ready architecture with Docker, CI/CD, AWS deployment. And The entire project is build using python version 3.13.5*



## **Tech Stack**

| Category         | Technology               |
| ---------------- | -------------------      |
| Language         | Python                   |
| ML               | Scikit-Learn             |
| Data Handling    | Pandas, Numpy            |
| Visualization    | Matpolotlib, Seaborn     |
| Web Framework    | Flask                    |
| Frontend         | HTML/CSS                 |
| Containerization | Docker                   |
| Cloud            | AWS                      |
| CI/CD            | GitHub Actions           |
| ContainerRegistry| Amazon ECR               |
| Deployment       | EC2 instance with ECR    |
| Deployment       | Elastic Beanstalk        |
| Version Control  | Git  & GitHub            |

## **Project Architecture**

### Overview
The project follows a modular, end-to-end machine learning pipeline architecture designed for scalability, reproducibility, and deployment. The system is built using Python and follows industry best practices for machine learning projects.

### Components
1. **Data Ingestion**: Responsible for loading the raw data from the source (CSV file) and splitting it into training and testing datasets.
2. **Data Transformation**: Handles data cleaning, feature engineering, and preprocessing steps such as encoding categorical variables and scaling numerical features.
3. **Model Training**: Trains machine learning models (using Scikit-learn) on the processed data and evaluates their performance.
4. **Model Evaluation**: Evaluates the trained models using appropriate metrics (e.g., R-squared score) and selects the best model.
5. **Model Deployment**: Packages the trained model and necessary preprocessing steps into a format suitable for deployment (using Flask for a simple web API).
6. **CI/CD Pipeline**: Uses GitHub Actions to automate testing, building Docker images, and deploying to AWS (EC2/ECR/Elastic Beanstalk).
7. **Monitoring**: Logs and monitors the model's performance in production (though basic logging is implemented).

### Directory Structure
```
End_to_end_Ml_project/
├── notebook/
│   └── EDA.ipynb                  # Exploratory Data Analysis notebook
├── src/
│   ├── __init__.py
│   ├── logger.py                  # Logging configuration
│   ├── exception.py               # Custom exception handling
│   ├── utils.py                   # Utility functions
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py      # Data ingestion component
│   │   ├── data_transformation.py # Data transformation component
│   │   └── model_trainer.py       # Model training component
│   └── pipeline/
│       ├── __init__.py
│       ├── train_pipline.py       # Training pipeline orchestration
│       └── prediction_pipeline.py # Prediction pipeline for serving
├── notebook/
│   └── Data/
│       └── students.csv           # Raw data
├── artifacts/                     # Generated data and models (created during runtime)
├── logs/                          # Log files
├── projectvenv/                   # Virtual environment
├── Dockerfile                     # Docker configuration for containerization
├── .github/
│   └── workflows/
│       └── main.yml               # GitHub Actions CI/CD workflow
├── requirements.txt               # Python dependencies
├── setup.py                       # Package setup script
└── README.md
```

### Data Flow
1. Data is ingested from `notebook/Data/students.csv` into the data ingestion component.
2. The data is split into training and testing sets and saved as artifacts.
3. The training data is passed to the data transformation component for preprocessing.
4. The transformed data is used to train the model in the model trainer component.
5. The trained model is saved as an artifact.
6. The prediction pipeline loads the model and preprocessing objects to make predictions on new data.
7. The Flask app (not shown in the current src but implied) would use the prediction pipeline to serve predictions via an API.
8. Dockerfile containerizes the application.
9. GitHub Actions workflow builds the Docker image and pushes to Amazon ECR, then deploys to AWS Elastic Beanstalk or EC2.

### Technologies Used
- **Language**: Python 3.13.5
- **Machine Learning**: Scikit-Learn
- **Data Handling**: Pandas, Numpy
- **Visualization**: Matplotlib, Seaborn (for EDA)
- **Web Framework**: Flask (for API)
- **Containerization**: Docker
- **Cloud**: AWS (ECR, EC2, Elastic Beanstalk)
- **CI/CD**: GitHub Actions
- **Version Control**: Git & GitHub