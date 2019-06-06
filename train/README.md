# A Comprehensive ML Workflow with Python

## Problem Feature

This dataset contains information about 11 different variables:

* Age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5

* Sibsp: The dataset defines family relations in this way...
  * Sibling: brother, sister, stepbrother, stepsister
  * Spouse: husband, wife (mistresses and fiancés were ignored)

* Parch: The dataset defines family relations in this way...
  * Parent: mother, father
  * Child: daughter, son, stepdaughter, stepson
  * Some children travelled only with a nanny, therefore parch=0 for them.

* Pclass: A proxy for socio-economic status (SES)
  * 1st = Upper
  * 2nd = Middle
  * 3rd = Lower
  
* Embarked: nominal datatype
* Name: nominal datatype . It could be used in feature engineering to derive the gender from title
* Sex: nominal datatype. Female (0) or Male(1)
* Ticket: that have no impact on the outcome variable. Thus, they will be excluded from analysis
* Cabin: is a nominal datatype that can be used in feature engineering
* Fare: Indicating the fare
* PassengerID: have no impact on the outcome variable. Thus, it will be excluded from analysis
* Survival: dependent variable , 0 or 1

### Types of Features

* **Categorical**: Has two or more categories and each value in that feature can be categorised by them.(Sex,Embarked)
* **Ordinal**: An ordinal variable is similar to categorical values, but the difference between them is that we can have relative ordering or sorting between the values (PClass)
* **Continous**: A feature is said to be continous if it can take values between any two points or between the minimum or maximum values in the features column. (Age)

# Exploratory Data Analysis(EDA)

## Data Collection

Data collection is the process of gathering and measuring data, information or any variables of interest in a standardized and established manner.

* Each row is an observation (also known as : sample, example, instance, record)
* Each column is a feature (also known as: Predictor, attribute, Independent Variable, input, regressor, Covariate)

## Visualization

Data visualization is the presentation of data in a pictorial or graphical format. It enables decision makers to see analytics presented visually, so they can grasp difficult concepts or identify new patterns

## Data Preprocessing

Data preprocessing refers to the transformations applied to our data before feeding it to the algorithm. Data Preprocessing is a technique that is used to convert the raw data into a clean data set.

* How many columns and rows are there in my dataset ? (print(df_train.shape)) (891, 12)

## Data Cleaning

### Transforming Features

Data transformation is the process of converting data from one format or structure into another format or structure

* **simplify_ages**: Turns Age continuous variable into categorical valiable.
* **simplify_cabins**: Keeps only one character of each value.
* **simplify_fare**: Turns Fare continuous variable into categorical valiable.
* **format_name**: Saves name and name prefix into two different variables (Lname, NamePrefix).
* **drop_features**: Delete columns that will be unused.

### Feature Encoding

Our machine learning algorithm can only read numerical values, so it is essential to encoding categorical features into numerical values. Features encoded ('Fare', 'Cabin', 'Age', 'Sex', 'Lname', 'NamePrefix')

## Model Deployment

### how to prevent overfitting & underfitting???

### RandomForestClassifier

A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.

### Model Persistence

After trainig the model, it is desirable to have a way to persist the model for future use without having to retrain. There are 2 libraries that make this possible:

* joblib (Selected)
* pickle
