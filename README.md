# ⚡ Electricity Consumption Forecaster

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://electricity-consumption-forecasting01.streamlit.app/)

## Overview
This project is an interactive machine learning web application that predicts a household's total electrical power consumption (`Global_active_power`) at any given hour. By combining behavioral time-series data with direct appliance sub-metering, the XGBoost model achieves an accuracy ($R^2$ score) of **~0.84**, learning the physical and routine-based limitations of a real-world electrical grid.

## Live Demo
**Try the live application here:** [Electricity Consumption Forecaster](https://electricity-consumption-forecasting01.streamlit.app/)

## 🧠 The Machine Learning Model
The predictive engine behind this application is an **XGBoost Regressor**.

To prevent target leakage and ensure realistic forecasting, the model is trained exclusively on:
* **Time-Based Behavioral Features:** `hours`, `DayOfWeek`, `month`, and `year`. These allow the model to understand human routines (e.g., evening peaks, weekend adjustments, and seasonal heating/cooling).
* **Direct Appliance Sub-metering (Watt-hours):** * `kitchen`: Ovens, microwaves, etc.
  * `laundry room`: Washing machines, dryers.
  * `climate & water`: Water heaters and air conditioning (the heaviest loads).

By identifying overlapping conditions between human behavior and active high-draw appliances, the model interpolates highly accurate total power constraints.

## 📊 Dataset
The model was trained on the **[Individual Household Electric Power Consumption Data Set](https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption)** from the UCI Machine Learning Repository. It contains over 2 million minute-by-minute measurements gathered from a house in Sceaux, France, between 2006 and 2010.

## 🛠️ Tech Stack
* **Language:** Python
* **Data Processing:** pandas, NumPy
* **Machine Learning:** XGBoost, scikit-learn
* **Web Framework & Deployment:** Streamlit, Streamlit Community Cloud

## 🚀 How to Run Locally

If you want to run this project on your own machine, follow these steps:

**1. Clone the repository**
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
