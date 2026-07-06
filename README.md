#  Spam Email Detection using Machine Learning

#  Project Overview

This project is a Machine Learning-based Spam Email Detection System developed using Python. It classifies email messages as either **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) techniques and a Logistic Regression classifier. A simple Streamlit web interface allows users to enter an email and instantly check the prediction.


##  Features

- Detects whether an email is Spam or Ham.
- Uses Machine Learning for text classification.
- Converts text into numerical features using TF-IDF Vectorization.
- Interactive web interface built with Streamlit.
- Easy-to-use and beginner-friendly.

##  Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

##  Project Structure

Spam_Email_Detection
* app.py
* spam_model.pkl
* vectorizer.pkl

##  Application

The user enters an email message into the text box and clicks the **Predict** button.

The application predicts whether the email is:

-  Ham (Not Spam)
-  Spam
<img width="964" height="563" alt="Screenshot 2026-07-06 at 8 09 55 PM 2" src="https://github.com/user-attachments/assets/9f31db96-0204-4c29-abb9-ece4086abe0e" />

                  
##  Machine Learning Workflow

1. Load the dataset
2. Preprocess the text
3. Convert text into numerical features using TF-IDF Vectorizer
4. Split the dataset into training and testing sets
5. Train the Logistic Regression model
6. Evaluate the model
7. Save the trained model and vectorizer
8. Deploy using Streamlit

##  Future Improvements

- Improve prediction accuracy using advanced models.
- Add support for multiple languages.
- Deploy the application online.
- Enhance the user interface.

##  Author

##sRegmi99
