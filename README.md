# Project Name- Weather API

A weather API allows developers to access and retrieve weather-related information from a weather data provider 
i.e. "https://open-meteo.com/" in this case. Weather APIs provide a programmatic way to access historical weather data.


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/savitaredekar10/weather_api.git

2. Navigate to the project directory:
   cd weather_api

3. Install dependencies:
   pip install -r requirements.txt

# Postman Testing-
This project includes automated tests created with Postman. 
These tests help ensure the functionality and reliability of the API. 
Below are instructions on how to run and understand the Postman tests.

# Running Tests-
1.	Open Postman.
2.	
2. Run the endpoints as below for user creation:
     1. Register user with username and password-
  	http://127.0.0.1:8000/api/user/register/   
     2. Create token for user with username and password-
  	http://127.0.0.1:8000/api/user/token/   
     3. Authorize user with token-
  	http://127.0.0.1:8000/api/user/secure/

3. Run the endpoints as below for weather data creation:
	Provide latitude, longitude, start and end date as params and also add Authorization in 	headers with access token for user
	http://127.0.0.1:8000/api/weather/historical-weather/


