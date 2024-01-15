from django.http import JsonResponse
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from .models import WeatherData
import requests
from datetime import datetime, timedelta
from django.utils import timezone

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_historical_weather(request):
    latitude    = float(request.query_params.get('latitude'))
    longitude   = float(request.query_params.get('longitude'))
    days        = int(request.query_params.get('days', 7))  # Default to 7 days if not provided
    end_date    = request.query_params.get('end_date', None)
    timezone    = request.query_params.get('timezone', 'auto')
    start_date = request.query_params.get('end_date')
    user        = request.user 

    if not end_date:
        end_date = datetime.now()     
    
    # Construct the Open Meteo API URL
    open_meteo_api_url = f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&hourly=temperature_2m,precipitation,cloud_cover&timezone=auto"

    try:
        # Fetch data from the Open Meteo API
        response = requests.get(open_meteo_api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        print(response.text)
        # Parse the JSON response
        data = response.json()

        # Check if the 'hourly' key is present in the response
        if 'hourly' in data: 
            hourly_data = data['hourly']

            # Extract temperature, precipitation, and cloud cover data
            timestamps      = hourly_data.get('time', [])
            temperatures    = hourly_data.get('temperature_2m', [])
            precipitation   = hourly_data.get('precipitation', [])
            cloud_cover     = hourly_data.get('cloud_cover', [])

            # Create WeatherData instances and save to the database
            for timestamp, temp, prec, cloud in zip(timestamps, temperatures, precipitation, cloud_cover):
                WeatherData.objects.create(
                    user        = user,
                    location    = f"{latitude}, {longitude}",
                    latitude    = latitude,
                    longitude   = longitude,
                    temperature = temp,
                    precipitation = prec,
                    cloud_cover   = cloud,
                    timestamp     = timestamp               
                )

            return JsonResponse({'message': f'{len(temperatures)} records created successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Unexpected response format: Missing or invalid "hourly" key'}, status=500)

    except ValueError as ve:
        return JsonResponse({'error': f'Invalid parameter value: {ve}'}, status=400)

    except requests.exceptions.RequestException as e:
        # Handle exceptions such as network errors
        return JsonResponse({'error': str(e)}, status=500)
