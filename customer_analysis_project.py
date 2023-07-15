#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import pickle

import os

file_path = 'C:/Users/priya/Downloads/classifier.pkl'
model = pickle.load(open(file_path, 'rb'))

# Page configuration
st.set_page_config(page_title='Customer Segmentation Web App', layout='centered')
st.title('Customer Segmentation Web App')

# Function to segment customers
def segment_customers(input_data):
    prediction = model.predict(input_data)
    return prediction

def main():
    # Sidebar inputs
    st.sidebar.title("Customer Information")
    income = st.sidebar.text_input("Household Income")
    kidhome = st.sidebar.radio("Number of Kids in Household", ('0', '1', '2'))
    teenhome = st.sidebar.radio("Number of Teens in Household", ('0', '1', '2'))
    age = st.sidebar.slider("Age", 18, 85)
    partner = st.sidebar.radio("Living with Partner?", ('Yes', 'No'))
    education_level = st.sidebar.selectbox("Education Level", ("Undergraduate", "Graduate", "Postgraduate"))

    # Create input data frame
    input_data = pd.DataFrame({
        'Income': [income],
        'Kidhome': [kidhome],
        'Teenhome': [teenhome],
        'Age': [age],
        'Partner': [partner],
        'Education_Level': [education_level]
    })

    # Make prediction
    if st.sidebar.button("Segment Customer"):
        result = segment_customers(input_data)
        st.success("Customer segment: Cluster {}".format(result[0]))

if __name__ == '__main__':
    main()

