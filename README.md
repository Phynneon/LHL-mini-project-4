# Mini-project IV

### [Assignment](assignment.md)

## Project/Goals
The goal of this project is to set up prediction model pipeline for bank loan granting. The model is then deployed on the cloud and returns loan grant predictions if it is given some information about the application in json. 

## Hypothesis
The hypothesis is that applicants that:
- Have higher income
- Have graduated
- Have a credit history
are more likely to have a loan approved.

## EDA 
The data correlation showed that:
- Having Graduated increases the likelyhood to be granted a loan.
- Married applicants tend to have a higher rate of being granted a loan (likely due to having a co-applicant).
- People with low combined income tend to have a higher chance to be refused a loan.
- The impact of credit history on loan approval is unclear due to missing values.

## Process
### 1 - Data Exploration
The first step of the project consists of:
- finding the amount of null values in each features
- finding the relationship between different features and the loan status
- looking at the distribution of numerical features such as income and loan amount

### 2 - Data Cleaning
The second step of the project consists of:
- replacing numberical null values with median of the feature
- replacing categorical null values with the highest occuring category
- removing columns that are unessesary for prediction such as loan ID

### 3 - Model building
The third step of the project consists of:
- Selecting a machine learning model
- applying scaling to numerical features
- applying encoding to categorical features
- performing grid search to find optimal parameters for the model
- performing prediction and model evaluation

### 4 - Pipeline
The fourth step of the project consists of:
- setting up the process of the first 3 steps into a pipeline model
- saving the final model to a pickle to be used in the app deployment

### 5 - App deployment
The fifth step of the project consists of:
- running the predictive model app in local computer
- deploying the app to AWS cloud
- sending a request in json format and obtain a reply from the prediction app

## Results/Demo
The accuracy of the preliminary logistic regression model ranges from 75 to 85 percent. It is very good at prediction when a loan will be approved but bad at prediction loans that are refused. The API created is a simple one that takes in a json file, run the model and returns a string telling the user if they are likely to have their loan approved or not. 

## Challanges 
The main challenge of the project is the pipeline. It was hard to convert some of the feature selection and generetion process in the pipeline. I ended up massively simplifying the pipeline process to get the preliminary model to work. (I plan to gradually update my pipeline model when I have more free time).

## Future Goals
The main change I will make is to improve on my pipeline model. I plan to add in a feature selection and engineering model to the process. Another element to change is the prediction model. Given the time I would like to run different models such as XGboost and SVM. I would also like to add a feature processing step such as pca and selectKbest and explore how those changes will improve on the base model.
