# Apple-Foliar-Disease-Classification

[![Kaggle](https://img.shields.io/badge/Dataset-Kaggle-blue.svg)](https://www.kaggle.com/competitions/plant-pathology-2020-fgvc7/data) ![Python 3.6](https://img.shields.io/badge/Python-3.6-brightgreen.svg)

### Problem statement:
A DL project that helps in identifying Foliar disease in apple trees weather its leaves are healthy, are infected with apple rust, those that have apple scab, and those with more than one disease.

### Dataset
You can find the dataset [here.](https://www.kaggle.com/competitions/plant-pathology-2020-fgvc7/data)

## setup
To create a project from scratch use following steps - -

- Clone the repository : https://github.com/ni3choudhary/Apple-Foliar-Disease-Classification-Deployment.git
- Inside the project root directory, Create Python Virtual Environment using below command.
```console
$ python3 -m venv venv
``` 

Activate Virtual Environment
```console
$ .venv/bin/activate 
          OR
$ .\venv\Scripts\activate
```
Install Libraries using below command
```console
$ pip install -r requirements.txt
```
- Run jupyter notebook to get the model and labels pickle file.

- Copy both pickle files and paste inside **flask** directory .

- Inside the **flask** directory run **app.py** on terminal to start local server.
```console
$ python app.py
```

• If you want to view the deployed model, click on the following link: Deployed at: https://apple-foliar-disease-classify.herokuapp.com/

• Please do ⭐ the repository, if it helped you in anyway.

