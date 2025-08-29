---

# Loan Status Prediction Model

A machine learning project to predict loan approval status using **Support Vector Machines (SVM)** in Python. The model analyzes applicant details to automate decision-making for banks, reducing manual effort and improving consistency.

---

# Goal

To build a machine learning model that predicts whether a loan application should be approved or rejected based on applicant data.

---

# Problem Statement

Banks receive thousands of loan applications daily. Manual verification is:

* Time-consuming
* Error-prone
* Inconsistent

This project automates the screening process using an SVM classifier.

---

# Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Seaborn, Matplotlib, Scikit-learn
* **Model:** Support Vector Machine (SVM)

---

# Dataset

* Source: Loan dataset (Kaggle / Universal Bank dataset)
* Records: 614 entries, 13 columns
* Target Variable: **Loan\_Status (Y/N)**
* Features:

  * **Categorical:** Gender, Married, Education, Self\_Employed, Property\_Area
  * **Numerical:** ApplicantIncome, CoapplicantIncome, LoanAmount, Loan\_Amount\_Term, Credit\_History

---

# Approach

1. **Data Cleaning** – handled missing values.
2. **Encoding** – converted categorical values into numerical form.

   * Example: Male → 1, Female → 0; Graduate → 1, Not Graduate → 0
3. **EDA (Exploratory Data Analysis)** – used count plots and visualizations to identify patterns.
4. **Feature Selection** – removed irrelevant columns (e.g., Loan\_ID).
5. **Data Splitting** – stratified train-test split to preserve class balance.
6. **Model Training** – trained an **SVM (linear kernel)** classifier.
7. **Evaluation** – achieved \~83% accuracy on the test set.
8. **Predictive System** – user inputs are reshaped & encoded before prediction.

---

# Results

* Training Accuracy: \~80%
* Testing Accuracy: \~83%
* Developed a predictive system that takes user inputs and instantly returns loan approval status.

---

# Deployment

* Integrated with a frontend using **HTML & CSS** for end-user accessibility.
  
---
*This project demonstrates the application of SVM for real-world decision-making in the financial sector.*


Would you like me to also include **setup instructions (installation & run commands)** so others can directly clone and try it from GitHub?
