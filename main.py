import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["2023-19-11", "2023-20-11", "2023-21-11", "2023-22-11",
             "2023-23-11", "2023-24-11", "2023-25-11", "2023-26-11"]
    temperatures = [76, 75, 77, 80, 74, 73, 78, 71]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d, t = get_data(days)
figure = px.line(x=d, y=t,
                 labels={"x": "Date", "y": "Temperature (F)"})
st.plotly_chart(figure)
