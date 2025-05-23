import streamlit as st
import pickle
import pandas as pd
import requests # Make sure 'requests' is imported

# --- CONFIGURATION ---
# Set this to True to bypass fetching posters from TMDb.
# This is recommended if you are consistently getting connection errors.
# When True, it will always show a placeholder image instead of trying to fetch from TMDb.
BYPASS_POSTER_FETCHING = False# <--- SET TO TRUE TO BYPASS POSTER API CALLS

# IMPORTANT: Replace 'YOUR_API_KEY' with your actual TMDb API key
# This key is only used if BYPASS_POSTER_FETCHING is False.
TMDb_API_KEY = "5130b00ad14fd07408a66ad29d21f8ae" # <--- REPLACE THIS WITH YOUR ACTUAL API KEY (only if BYPASS_POSTER_FETCHING is False)


# Function to fetch movie poster
def fetch_poster(movie_id):
    if BYPASS_POSTER_FETCHING:
        # If bypassing, return a generic placeholder image
        return f"https://placehold.co/200x300/E0E0E0/333333?text=No+Poster"

    # If not bypassing, attempt to fetch from TMDb
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={TMDb_API_KEY}&language=en-US"

    try:
        response = requests.get(url, timeout=10) # Added a timeout
        response.raise_for_status() # Raises HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        poster_path = data.get('poster_path') # Use .get() to avoid KeyError if path is missing
        if poster_path:
            full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
            return full_path
        else:
            # Fallback if poster_path is null or empty
            return "https://placehold.co/200x300/E0E0E0/333333?text=No+Poster"
    except requests.exceptions.HTTPError as http_err:
        st.error(f"HTTP error occurred while fetching poster: {http_err} (Status Code: {response.status_code}). Check API key or URL.")
        return "https://placehold.co/200x300/E0E0E0/333333?text=Error"
    except requests.exceptions.ConnectionError as conn_err:
        st.error(f"Connection error occurred while fetching poster: {conn_err}. Check your internet connection or API key.")
        return "https://placehold.co/200x300/E0E0E0/333333?text=No+Connection"
    except requests.exceptions.Timeout as timeout_err:
        st.error(f"Timeout error occurred while fetching poster: {timeout_err}")
        return "https://placehold.co/200x300/E0E0E0/333333?text=Timeout"
    except requests.exceptions.RequestException as req_err:
        st.error(f"An unexpected error occurred while fetching poster: {req_err}")
        return "https://placehold.co/200x300/E0E0E0/333333?text=Error"
    except Exception as e:
        st.error(f"An unknown error occurred: {e}")
        return "https://placehold.co/200x300/E0E0E0/333333?text=Error"


# Load the data
try:
    # Assuming 'movie_data.csv' is in the 'model' subfolder
    movies = pd.read_csv('model/movie_data.csv')
    # Assuming 'similarity.pkl' is in the 'model' subfolder
    with open('model/similarity.pkl', 'rb') as f:
        similarity = pickle.load(f)
except FileNotFoundError:
    st.error("Error: 'movie_data.csv' or 'similarity.pkl' not found in the 'model/' directory. Please ensure these files are correctly placed.")
    st.stop()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()


# Function to recommend movies
def recommend(movie):
    movie_lower = movie.lower()
    if movie_lower not in movies['title'].str.lower().values:
        return [], f"❌ Movie '{movie}' not found in the dataset."

    # Find the index of the selected movie (case-insensitive search)
    index = movies[movies['title'].str.lower() == movie_lower].index[0]
    distances = list(enumerate(similarity[index]))
    sorted_movies = sorted(distances, key=lambda x: x[1], reverse=True)[1:6] # Get top 5 recommendations

    recommended_movie_names = []
    recommended_movie_posters = []
    for i in sorted_movies:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_posters.append(fetch_poster(movie_id)) # Call fetch_poster here
    return recommended_movie_names, recommended_movie_posters

st.set_page_config(layout="wide")

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Type or select a movie from the dropdown',
    movies['title'].values
)

if st.button('Show Recommendation'):
    if selected_movie_name:
        names, posters = recommend(selected_movie_name)
        if names and not isinstance(names, str): # Check if names is a list (not an error message string)
            st.subheader("Recommended Movies:")
            col1, col2, col3, col4, col5 = st.columns(5)
            # Display recommendations in columns
            with col1:
                st.text(names[0])
                st.image(posters[0])
            with col2:
                st.text(names[1])
                st.image(posters[1])
            with col3:
                st.text(names[2])
                st.image(posters[2])
            with col4:
                st.text(names[3])
                st.image(posters[3])
            with col5:
                st.text(names[4])
                st.image(posters[4])
        else:
            st.warning(posters) # This will display the "Movie not found" message
    else:
        st.warning("Please select a movie to get recommendations.")
