import streamlit as st
from dbhelper import DB
import pandas as pd
import plotly.express as px
db=DB()
st.sidebar.title("flights analytics") 
user_option=st.sidebar.selectbox('Menu',['select one','check flights','flights analytics'])
if user_option=='check flights':
    st.title('Flights')
    col1,col2=st.columns(2)
    city=db.fetch_city_name()
    with col1:
         
         source=st.selectbox('source',sorted(city))
    with col2:
         destination=st.selectbox('destination',sorted(city))
    # Search button
    if st.button('Search Flights'):
        if source == destination:
            st.warning("Source and destination cannot be the same.")
        else:
            results = db.fetch_all_flights(source, destination)
            if results:
                st.success(f"Found {len(results)} flights.")
                st.dataframe(results, use_container_width=True)
            else:
                    st.info("No flights found for the selected route.")
elif user_option=='flights analytics':
    st.title('Analysis')
    airline,frequency=db.fetch_airlines_frequency()
    fig = px.pie(
    names=airline,
    values=frequency,
    title="Airline Market Share",
    hole=0.3)  # Set to 0 for full pie, >0 for donut

    # Show in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    name,count=db.busy_airport()
    # Create plotly bar chart
    fig = px.bar(
        x=name,
        y=count,
        labels={'x': 'Airline', 'y': 'Number of Flights'},
        title='Busiest airports',
        color=name  # Optional: adds different color per bar
    )

    # Display in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    date,count=db.flights_per_day()
    # Create Plotly line chart
    fig = px.line(
        x=date,
        y=count,
        labels={'x': 'date', 'y': 'Flights'},
        title='Daily Flight Count'
    )

    # Show in Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    data=db.non_stop_vs_connecting()
    # Create DataFrame
    df = pd.DataFrame(data, columns=['Airline', 'Total_Stops', 'Flight_Count'])

# Plot grouped bar chart
    fig = px.bar(
        df,
        x='Airline',
        y='Flight_Count',
        color='Total_Stops',
        title='Non-stop vs Connecting Flights per Airline',
        barmode='group'
    )

    st.plotly_chart(fig, use_container_width=True)
    
    data=db.fastest_airlines()
    df = pd.DataFrame(data, columns=['Airline', 'Avg_Duration_Minutes'])

# Plot horizontal bar chart
    fig = px.bar(
        df,
        x='Avg_Duration_Minutes',
        y='Airline',
        orientation='h',
        title='Airlines with Fastest Average Route Duration',
        color='Avg_Duration_Minutes',
        color_continuous_scale='Viridis'
    )

    st.plotly_chart(fig, use_container_width=True)
    
    
    data=db.cheapest_flights()
    df = pd.DataFrame(data, columns=["Airline", "Avg Price"])

    # Plot bar chart
    st.subheader("💸 Cheapest Airlines by Average Price")
    fig = px.bar(df, x="Airline", y="Avg Price",
                color="Avg Price",
                color_continuous_scale="Blues",
                labels={"Avg Price": "Average Price (₹)"},
                title="Airline-wise Average Flight Price")

    fig.update_layout(xaxis_title="Airline", yaxis_title="Average Price (₹)")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.title("✈️ Indigo Flight Analytics Dashboard")

    # Subtitle
    st.subheader("A Streamlit + PostgreSQL powered visualization tool for flight data insights")

    # Description
    st.markdown("""
    Welcome to the **Indigo Flight Analytics Dashboard** — a powerful data exploration tool built using **Streamlit** and **PostgreSQL**.

    This project analyzes flight data from the `flights_cleaned` table, which contains key information such as:
    - ✈️ **Airline names**
    - 📍 **Source & destination cities**
    - 🕐 **Departure times**
    - ⏱️ **Flight durations (in minutes)**
    - 🔁 **Number of stops**
    - 📅 **Journey dates**

    ---

    ### 🔍 Key Insights Provided:
    - 📈 **Daily flight trends** to monitor traffic over time  
    - 🛫 **Airline-wise performance** in terms of frequency and speed  
    - 📍 **Route analysis** for identifying high-traffic or fastest paths  
    - ⏱️ **Duration and stop comparisons** across airlines  
    - 🕐 **Departure time distributions** throughout the day  

    ---

    ### 🛠️ Technologies Used:
    - 🐍 **Python** + **Streamlit** for interactive UI  
    - 🗃️ **PostgreSQL** for robust SQL querying  
    - 📊 **Plotly** for modern and responsive charts  

    Whether you're a data analyst, airline manager, or travel enthusiast — this dashboard helps you **visualize and explore commercial flight patterns** in a clean, user-friendly interface.
    """)

