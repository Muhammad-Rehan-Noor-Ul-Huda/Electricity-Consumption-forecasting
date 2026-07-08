import streamlit as st
import pickle
import pandas as pd

def main():
# 1. Load your saved model
    with open('electricity_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # 2. Set up the web page title
    st.title("⚡ Electricity Consumption Forecaster")
    st.write("Enter the details below to predict the total Global Active Power.")

    # 3. Create input fields for the user
    col1, col2 = st.columns(2)

    with col1:
        kitchen = st.number_input("Kitchen Sub-metering", min_value=0.0, value=0.0)
        laundry = st.number_input("Laundry Room Sub-metering", min_value=0.0, value=0.0)
        climate = st.number_input("Climate & Water Sub-metering", min_value=0.0, value=0.0)

    with col2:
        month = st.selectbox("Month", range(1, 13))
        hour = st.slider("Hour of Day", 0, 23, 12)
        day_of_week = st.selectbox("Day of Week (0=Mon, 6=Sun)", range(0, 7))
        year = st.number_input("Year", min_value=2000, value=2010)

    # 4. Make the prediction when a button is clicked
    if st.button("Predict Consumption"):
        # Create a DataFrame that matches the exact column names your model expects
        input_data = pd.DataFrame({
            'kitchen': [kitchen],
            'laudary room': [laundry],
            'climate & water': [climate],
            'month': [month],
            'hours': [hour],
            'DayOfWeek': [day_of_week],
            'year': [year]
        })
        
        # Generate the prediction
        prediction = model.predict(input_data)
        
        # Display the result to the user
        st.success(f"Predicted Total Power: {prediction[0]:.3f} kilowatts")
if __name__=="__main__":
    main()