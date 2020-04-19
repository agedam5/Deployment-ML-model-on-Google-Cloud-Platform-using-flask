# Deployment-ML-model-on-Google-Cloud-Platform-using-flask
Predicting the price of Smartphones based on the battery capacity, RAM size, ROM size and phone model.
This project consist of 9 files which are mentioned below :
Web scrapping using Beautiful soup and request-->> This is .py file for webscrapping performed on Flipkart website to extract data of smartphones(Redmi,Motorola,Oneplus and Samsung)
Flipkart.csv -->> data scrapped from Flipkart is saved into this csv file.
main_sript.py-->> reading Flipkart.csv file, data preprocessing, normalization and model building.
model1.pkl -->> saved model for prediction using pickle library
app.py-->> flask code for model deployment
templates-->> html code for API
style-->>css script for API
app.yaml -->> runtime version for python(specifically for Google cloud platform)
requirement.txt -->> All the libraries required to be used by GCP to run our model in cloud.
Screenshots for the API has been attached.
