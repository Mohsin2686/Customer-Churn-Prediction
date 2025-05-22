# End to End Customer-Churn-Prediction Project

## Tools
- Anaconda: https://www.anaconda.com/
- Vs code: https://code.visualstudio.com/download
- Git: https://git-scm.com/
- MLOPs Tool: https://www.evidentlyai.com/
- MongoDB: https://account.mongodb.com/account/login
- Data link: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

## How to run?

```bash
conda create -n churn python=3.8 -y
```

```bash
conda activate churn
```

```bash
pip install -r requirements.txt
```

## Run all the cells in notebooks/mongodb_connetion.ipynb to create the collection of dataset in MongoDB

## Export the  environment variable



export MONGODB_URL="mongodb+srv://<username>:<password>...."

export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>



### To run training pipeling 

```bash
python domo.py
```



### To run prediction app 

```bash

python app.py
```
