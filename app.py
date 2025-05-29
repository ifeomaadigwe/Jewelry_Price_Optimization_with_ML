<<<<<<< HEAD
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load models (make sure these files are in the same folder)
RF_model = joblib.load('RF_model.pkl')
cat_model = joblib.load('CatBoost_model.pkl')
et_model = joblib.load('ExtraTrees_model.pkl')

st.title("Jewelry Price Prediction App")

# Select model
model_choice = st.sidebar.selectbox(
    "Choose a model",
    ("Random Forest", "CatBoost", "Extra Trees")
)

if model_choice == "Random Forest":
    model = RF_model
elif model_choice == "CatBoost":
    model = cat_model
else:
    model = et_model

# Define features your model expects (update with your actual feature list)
features = ['Quantity of SKU', 'Main metal_platinum', 'Category alias_jewelry.ring', 'Product gender_female']

st.sidebar.header("Input Features")

# Create inputs dynamically
input_data = {}
for feature in features:
    if 'Category' in feature or 'metal' in feature or 'gender' in feature:
        # Binary features: checkbox returns True/False, convert to int
        input_data[feature] = int(st.sidebar.checkbox(feature))
    else:
        # Numeric features
        input_data[feature] = st.sidebar.number_input(feature, min_value=0)

# Convert inputs to dataframe
input_df = pd.DataFrame([input_data])

# Fill missing columns with 0 (all other features expected by model)
for col in model.feature_names_in_:
    if col not in input_df.columns:
        input_df[col] = 0

# Reorder columns to match training
input_df = input_df[model.feature_names_in_]

# Predict button
if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Price: {prediction[0]:.2f}")
=======
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load models (make sure these files are in the same folder)
RF_model = joblib.load('RF_model.pkl')
cat_model = joblib.load('CatBoost_model.pkl')
et_model = joblib.load('ExtraTrees_model.pkl')

st.title("Jewelry Price Prediction App")

# Select model
model_choice = st.sidebar.selectbox(
    "Choose a model",
    ("Random Forest", "CatBoost", "Extra Trees")
)

if model_choice == "Random Forest":
    model = RF_model
elif model_choice == "CatBoost":
    model = cat_model
else:
    model = et_model

# Define features your model expects (update with your actual feature list)
features = ['Quantity of SKU', 'Main metal_platinum', 'Category alias_jewelry.ring', 'Product gender_female']

st.sidebar.header("Input Features")

# Create inputs dynamically
input_data = {}
for feature in features:
    if 'Category' in feature or 'metal' in feature or 'gender' in feature:
        # Binary features: checkbox returns True/False, convert to int
        input_data[feature] = int(st.sidebar.checkbox(feature))
    else:
        # Numeric features
        input_data[feature] = st.sidebar.number_input(feature, min_value=0)

# Convert inputs to dataframe
input_df = pd.DataFrame([input_data])

# Fill missing columns with 0 (all other features expected by model)
for col in model.feature_names_in_:
    if col not in input_df.columns:
        input_df[col] = 0

# Reorder columns to match training
input_df = input_df[model.feature_names_in_]

# Predict button
if st.button("Predict Price"):
    prediction = model.predict(input_df)
    st.success(f"Predicted Price: {prediction[0]:.2f}")
>>>>>>> 802c60b (Final model updates, added CatBoost and ExtraTrees models)
