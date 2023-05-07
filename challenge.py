import os
import googlemaps
import requests
from dotenv import load_dotenv

load_dotenv()

gmaps = googlemaps.Client(key=os.environ.get('API_KEY'))

# Geocoding an address
def get_coordinates(address):
    geocode_result = gmaps.geocode(address)
    
    location = geocode_result[0]['geometry']['location']
    lat, lng = location['lat'], location['lng']
    
    return lat,lng

# Get neighborhood name from coordinates using the portlandmaps REST endpoint
def get_neighborhood_name(lat, lng):

    # Params to use with the query to get the neighborhood name
    params = {
        'where': '1=1',
        'geometry': f"{{'x':{lng},'y':{lat}}}",
        'geometryType': 'esriGeometryPoint',
        'inSR': 4326,
        'returnGeometry': False,
        'f': 'json'
    }
    
    url = 'https://www.portlandmaps.com/arcgis/rest/services/Public/COP_OpenData/MapServer/125/query'
    response = requests.get(url, params=params)

    result = response.json()['features'][0]['attributes']
    neighborhood_name = result['NAME']
    
    return neighborhood_name

# Recursive function to get a different neigborhood from the original one
def get_different_neighborhood(neighborhood_name, address):
    
    # Add 100 to the street number and get the new coordinates and neighborhood name
    street_number = int(address.split()[0])
    new_street_number = street_number + 100
    new_address = address.replace(str(street_number), str(new_street_number))
    new_lat, new_lng = get_coordinates(new_address)
    new_neighborhood_name = get_neighborhood_name(new_lat, new_lng)
    
    # If the new neighborhood name is different than the original
    if new_neighborhood_name != neighborhood_name:
        return new_address, new_neighborhood_name
    
    # Otherwise, recursively call the function with the new address
    return get_different_neighborhood(new_neighborhood_name, new_address)
    
# BEGIN PROGRAM
address = '1300 SE Stark Street, Portland, OR 97214'
lat, lng = get_coordinates(address)
og_neighborhood = get_neighborhood_name(lat, lng)
print(f'The original neighborhood is {og_neighborhood} with the address {address}')

different_address, different_neighborhood = get_different_neighborhood(og_neighborhood, address)
print(f"The next different neighborhood is {different_neighborhood} with the address {different_address}")