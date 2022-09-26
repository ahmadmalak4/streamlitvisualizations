
import pandas as pd
import streamlit as st

import numpy as np
import plotly.graph_objects as go



import plotly.express as px

st.set_page_config(
    page_title="learning visualizations",
    page_icon="👋",
)
st.write("# hey,welcome to our visualizations")

st.markdown(
    """
   “The greatest value of a picture is when it
forces us to notice what we never expected
to see.”
John W . Tukey, Exploratory Data Analysis (1977)
"""
)


st.title("visualization of three graphs")
df = pd.read_csv(r"C:\Users\ahmad malak\Desktop\seattle-weather.csv")
st.dataframe(df)
st.header("correlation between wind and Temp_max")




fig1 = px.scatter(df, x="wind", y="temp_max")
st.plotly_chart(fig1)
with st.expander("See explanation"):
    st.write("""
       this chart represent the realtion between wind and temp_max and how the two realtes to each other 
    """)
st.header("counting the weather based on recurrence by days.")
fig2 = px.histogram(df, x="weather")
st.plotly_chart(fig2)
option = st.selectbox(
    'How would you like to be contacted?',
    (("drizzle", "rain", "sun","snow","fog")))

st.write('You selected:', option) 

 
st.header("Line chart showing the variations of temp-min by days of the year.")
fig3 = px.line(df, x="date", y="temp_min", title='weather variations')
st.plotly_chart(fig3)

st.header("Table 2:  how the population, land area and med.age affects the world share of a country.")
df2 = pd.read_csv(r"C:\Users\ahmad malak\Desktop\population.csv")
st.dataframe(df2)



st.header("Pie chart showing the population by percentage of the top 10 countries by population number.")
fig4 = px.pie(df2.head(10), values='Population (2020)', names='Country (or dependency)')
fig4.update_traces(textposition='inside',textinfo='percent+label')
st.plotly_chart(fig4)
st.header("Bubble chart showing the country size by population using the makers in blue with different makers size representing the size of the population.")
fig5 = go.Figure(data=[go.Scatter(x=df2.head(10)["Country (or dependency)"], y=df2.head(10)["Population (2020)"],mode='markers',
    marker_size=[220,200,180,160,140,120,100,80,60,40])])
st.plotly_chart(fig5)


if st.button('what is the biggest country by pupulation'):
    st.write('china with 1.44b')

