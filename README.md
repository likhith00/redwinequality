# redwinequality
This repository is the end to end implementation of red wine quality. 

### Initial Steps
1. Clone this repository to your local IDE root folder.
2. Create virtual environment and activate it.
3. Create setup.py for versioning.
4. Create template.py for building project structure and execute ```python template.py```
5. Prepare requirements.txt and execute ```pip install -r requirements.txt```

### Logging and utils

1. Create logs for file handler and stream handler
2. Create a file called "common.py" to store and call reusable code in utils.


### Data Ingestion

1. Create Data Ingestion entity
2. prepare Data Ingestion configuration
3. construct Data Ingestion Component
4. Build Data Ingestion pipeline

### Data Validation

1. Create Data Validation entity
2. prepare Data Validation Configuration
3. Construct Data Validation Component
4. Build Data Validation pipeline

### Data Transformation

1. Create Data Transformation entity
2. prepare Data Transformation Configuration
3. Construct Data Transformation Component
4. Build Data Transformation pipeline

### Model Trainer

1. Create Model Trainer entity
2. prepare Model Trainer Configuration
3. Construct Model Trainer Component
4. Build Model Trainer pipeline

### Model Evaluation

1. Connect repository to Dagshub
2. get dagshub experiment credentials
3. Create Model Trainer entity
4. prepare Model Evaluation Configuration
5. Construct Model Evaluation Component
6. Build Model Evaluation pipeline

## prediction pipeline

1. create prediction.py file in pipelines.
2. Build HtML files for frontend access.
3. create flask app in app.py

## Deployment

1. create DockerFile
2. Create Azure resource group using ```az group create --name myResourceGroup --location eastus```
3. create azure container apps and push the docker image ```az containerapp up --resource-group myResourceGroup --name redwinecont2 --ingress external --target-port 8080 --source .```
4. destroy the resources after usage ```az group delete --name myResourceGroup```