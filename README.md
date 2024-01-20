![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.0-orange.svg)
![Plotly](https://img.shields.io/badge/plotly-5.0-blue.svg)
![API](https://img.shields.io/badge/API-v1-green.svg)

### Weather Forecast for the Next Days

This Python application uses Streamlit to provide a user-friendly interface for viewing weather forecasts. The application allows users to input a location and select the number of days for the forecast. It then displays temperature data or sky conditions based on the user's choice.

#### Features

- Input for specifying the location.
- Slider to select the number of forecast days (1 to 5 days).
- Option to choose between viewing temperature data or sky conditions.
- Visual representation of temperature trends using Plotly.
- Display of sky conditions using images.

#### Installation

To run this application, you need Python installed on your system. Clone the repository and install the dependencies:

```bash
git clone https://github.com/python-dev-og/weather-forecast-dashboard.git
cd weather-forecast
pip install -r requirements.txt
```

#### Usage

Run the application with Streamlit:

```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` in your web browser to view the application.

#### Dependencies

- Streamlit
- Plotly
- Backend module for data retrieval (`backend.py`)


#### Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

#### License

Distributed under the MIT License. See `LICENSE` for more information.

### Final Look 

![temperature.png](images%2Ftemperature.png)

![sky.png](images%2Fsky.png)