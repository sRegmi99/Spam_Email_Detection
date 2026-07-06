import streamlit as st
import pickle

# Load the trained model
with open("spam_model.pkl", "rb") as file:
    model = pickle.load(file)

# Load the vectorizer
with open("vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)

# Title
st.title("📧 Spam Email Detection")
st.write("Enter an email message below and click Predict.")

# User input
email = st.text_area("Enter Email Text")

# Prediction button
if st.button("Predict"):

    if email.strip() == "":
        st.warning("Please enter an email message.")
    else:
        # Convert text to numerical features
        email_vector = vectorizer.transform([email])

        # Predict
        prediction = model.predict(email_vector)

        # Display result
        if prediction[0] == 1:
            st.error("🚨 Spam Email")
        else:
            st.success("✅ Not Spam (Ham)")