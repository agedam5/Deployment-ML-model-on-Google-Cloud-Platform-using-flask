# Deployment-ML-model-on-Google-Cloud-Platform-using-flask
Predicting the price of Smartphones based on the battery capacity, RAM size, ROM size and phone model.
This project consist of 9 files which are mentioned below :
1.Web scrapping using Beautiful soup and request-->> This is .py file for webscrapping performed on Flipkart website to extract data of smartphones(Redmi,Motorola,Oneplus and Samsung)
2.Flipkart.csv -->> data scrapped from Flipkart is saved into this csv file.
3.main_sript.py-->> reading Flipkart.csv file, data preprocessing, normalization and model building.
4.model1.pkl -->> saved model for prediction using pickle library
5.app.py-->> flask code for model deployment
6.templates-->> html code for API
7.style-->>css script for API
8.app.yaml -->> runtime version for python(specifically for Google cloud platform)
9.requirement.txt -->> All the libraries required to be used by GCP to run our model in cloud.
Screenshots for the API has been attached.
