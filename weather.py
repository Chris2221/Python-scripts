import requests
from pprint import pprint
API_Key = ""
location = input("Enter Your Desired Location: ")
weather_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Phillipines?unitGroup=metric&key=X3PECJNFRQE8FFCJQGGUAJPMS&contentType=json"
final_url = weather_url + API_Key
weather_data = requests.get(final_url).json()
pprint(weather_data)