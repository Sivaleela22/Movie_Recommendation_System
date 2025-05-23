import requests
import json # Import json for pretty printing

# IMPORTANT: REPLACE THIS WITH YOUR ACTUAL TMDb v3 API KEY
api_key = "5130b00ad14fd07408a66ad29d21f8ae"

movie_id = 550 # This is the movie ID for 'Fight Club'

url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"

print(f"Attempting to fetch data from: {url}")

try:
    # Set a slightly longer timeout to see if it's just slow
    response = requests.get(url, timeout=15)
    response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
    data = response.json()

    print("\n--- API Call Successful! ---")
    print(f"Movie Title: {data.get('title', 'N/A')}")
    print(f"Poster Path: {data.get('poster_path', 'N/A')}")
    print(f"Full API Response (first 500 chars):\n{json.dumps(data, indent=2)[:500]}...")
    print("---------------------------\n")

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")
    print("This often means your API key is invalid or you're unauthorized (e.g., 401).")
except requests.exceptions.ConnectionError as conn_err:
    print(f"Connection error occurred: {conn_err}")
    print("Possible causes: No internet, firewall blocking, incorrect API key, or TMDb server issues.")
except requests.exceptions.Timeout as timeout_err:
    print(f"Timeout error occurred: {timeout_err}")
    print("The request took too long to get a response. This could be network congestion or server slowness.")
except requests.exceptions.RequestException as req_err:
    print(f"An unexpected requests error occurred: {req_err}")
except Exception as e:
    print(f"An unknown error occurred: {e}")