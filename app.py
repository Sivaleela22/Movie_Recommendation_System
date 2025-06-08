import pickle
import streamlit as st
import requests
import pandas as pd
import time

# Configuration
API_KEY = "5130b00ad14fd07408a66ad29d21f8ae"
MOVIE_LIST_PATH = 'model/movie_list.pkl'
SIMILARITY_PATH = 'model/similarity.pkl'

# Function to fetch movie poster with retries (no visible errors)
def fetch_poster(movie_id, max_retries=3):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"

    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                data = response.json()
                poster_path = data.get("poster_path")
                if poster_path:
                    return "https://image.tmdb.org/t/p/w500" + poster_path
                else:
                    return "https://via.placeholder.com/500x750?text=No+Image"
            elif response.status_code == 429:
                # Rate limit hit, wait before retrying
                time.sleep(2)
            else:
                break
        except (requests.ConnectionError, requests.Timeout, Exception):
            # Silently catch all network issues
            time.sleep(1)

    # Final fallback if all attempts fail
    return "https://via.placeholder.com/500x750?text=No+Image"


# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_names = []
    recommended_posters = []
    added_titles = set()

    i = 1  # skip the selected movie itself
    while len(recommended_names) < 5 and i < len(distances):
        idx = distances[i][0]
        title = movies.iloc[idx]['title']
        movie_id = movies.iloc[idx]['movie_id']

        if title not in added_titles:
            poster_url = fetch_poster(movie_id)
            recommended_names.append(title)
            recommended_posters.append(poster_url)
            added_titles.add(title)
        i += 1

    # Fill remaining slots with placeholders if needed
    while len(recommended_names) < 5:
        recommended_names.append("No Recommendation")
        recommended_posters.append("https://via.placeholder.com/500x750?text=No+Image")

    return recommended_names, recommended_posters


# Streamlit UI Setup
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")
st.markdown("Select a movie you like and get recommendations!")

# Load data
try:
    movies = pickle.load(open(MOVIE_LIST_PATH, 'rb'))
    similarity = pickle.load(open(SIMILARITY_PATH, 'rb'))

    if not isinstance(movies, pd.DataFrame):
        st.error("Invalid format for movie list. Expected a pandas DataFrame.")
        st.stop()

    if 'title' not in movies.columns or 'movie_id' not in movies.columns:
        st.error("Movie data must include 'title' and 'movie_id' columns.")
        st.stop()

except FileNotFoundError as e:
    st.error(f"Required file not found: {e}")
    st.stop()
except Exception as e:
    st.error(f"Error loading model files: {e}")
    st.stop()

# Dropdown for selecting a movie
selected_movie = st.selectbox("Choose a movie you like:", movies['title'].values)

# Show recommendations
if st.button("Show Recommendations"):
    with st.spinner("Fetching recommendations..."):
        names, posters = recommend(selected_movie)

    st.subheader("Recommended Movies:")
    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            st.image(poster, use_container_width=True)