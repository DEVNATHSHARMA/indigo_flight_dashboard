# 🛫 Indigo Flight Analytics Dashboard

A sleek and interactive dashboard built using **Streamlit** and **PostgreSQL**, offering real-time analytics and insights into domestic flight operations in India. This project is based on a cleaned dataset of flight information including airline names, routes, stops, durations, and fares.

---

## 📊 Features

- 🔍 **Search Flights** by Source and Destination
- 📈 **Visualize Daily Trends** in Flight Frequency
- 🛬 **Compare Airlines** by:
  - Average Duration
  - Number of Non-Stop vs Connecting Flights
  - Most Frequent Routes
  - Cheapest Carrier per Route
- ✈️ **Predict Most Likely Airline** for a given source-destination pair
- 💡 Insights through interactive **Pie, Bar, and Line Charts** using Plotly

---

## 🧠 Technologies Used

- `Streamlit` – Interactive Web UI
- `PostgreSQL` – Backend Database
- `psycopg2` – Database Connector
- `Pandas` – Data Wrangling
- `Plotly` – Interactive Charts

---

## 📂 Project Structure
flights_sql_app/
│
├── app.py # Streamlit app
├── db.py # PostgreSQL DB connection logic
├── crud.py # SQL Queries for all analytics
├── requirements.txt # Python dependencies
└── README.md # Project overview
