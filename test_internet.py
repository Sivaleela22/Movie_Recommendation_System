import requests

test_url = "https://jsonplaceholder.typicode.com/posts/1" # A simple, reliable API

print(f"Attempting to fetch data from: {test_url}")

try:
    response = requests.get(test_url, timeout=10)
    response.raise_for_status() # Raise an HTTPError for bad responses (4xx or 5xx)
    data = response.json()
    print("\n--- General Internet Connection Test Successful! ---")
    print(f"Fetched data: {data.get('title')}")
    print("--------------------------------------------------\n")
except requests.exceptions.RequestException as e:
    print(f"General internet connection test failed: {e}")
    print("This indicates a broader network issue, not just with TMDb.")
except Exception as e:
    print(f"An unexpected error occurred during general test: {e}")