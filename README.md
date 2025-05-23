My Movie Recommendation System
Welcome to my Movie Recommendation System! This project is a simple, interactive web application built with Streamlit that helps you discover new movies. Just pick a movie you like, and the system will suggest five similar ones.

🌟 Features
Easy Movie Selection: A simple dropdown lets you choose any movie from the dataset.

Smart Recommendations: Get 5 movie suggestions based on content similarity.

Poster Display: (Optional) See movie posters directly in the app.

Robust & User-Friendly: Designed for smooth operation with built-in error handling.

🛠️ Technologies Used
Python

Streamlit: For the interactive web interface.

Pandas: For handling and processing movie data.

Scikit-learn: (Used in the background for similarity calculations).

Requests: To fetch movie posters from external APIs.

The Movie Database (TMDb) API: Provides movie data and posters.

🚀 Getting Started
Follow these steps to set up and run the application on your local machine.

Prerequisites
Make sure you have:

Python 3.7+ installed

pip (Python package installer)

1. Clone My Repository
First, get a copy of this project:

git clone https://github.com/your-username/your-movie-recommendation-repo.git
cd your-movie-recommendation-repo

(Remember to replace your-username/your-movie-recommendation-repo.git with the actual URL of your GitHub repository!)

2. Set Up Your Environment
It's a good idea to use a virtual environment:

python -m venv venv
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

3. Install Required Libraries
Install all the necessary Python packages:

pip install streamlit pandas scikit-learn requests

4. Prepare Your Data Files
This application needs two specific files: movie_data.csv and similarity.pkl. These are generated from your data processing notebook (like movie_recommendation.ipynb).

Generate the files: Run all cells in your movie_recommendation.ipynb notebook to create movie_data.csv and similarity.pkl.

Place them correctly: Create a new folder named model in the root of your project. Then, move movie_data.csv and similarity.pkl into this model folder.

Your project structure should look like this:

your-movie-recommendation-repo/
├── app.py
├── movie_recommendation.ipynb  (your data processing notebook)
├── venv/                       (your Python virtual environment)
└── model/
    ├── movie_data.csv
    └── similarity.pkl

▶️ How to Run the Application
Activate your virtual environment:

# On Windows
.\venv\Scripts\activate

Navigate to your project's root directory (where app.py is).

Start the Streamlit app:

streamlit run app.py

Your web browser should automatically open the app at http://localhost:8501.

🖼️ Important Note on Movie Posters (TMDb API Key)
The app tries to fetch real movie posters from The Movie Database (TMDb). If you're seeing "Connection error" messages or no posters, it's likely an issue with your network, firewall, or the TMDb API key.

Get Your TMDb API Key:

Sign up for a free account at themoviedb.org.

Go to your Account Settings -> API and request a v3 API key.

Copy this key.

Add Your Key to app.py:
Open app.py and find the line TMDb_API_KEY = "YOUR_API_KEY". Replace "YOUR_API_KEY" with your actual key.

TMDb_API_KEY = "your_actual_tmdb_v3_api_key_here"

Bypass Poster Fetching (Troubleshooting/Default):
If you're still facing connection issues for posters, I've included a bypass. By default, it's set to True in app.py to ensure the app runs smoothly. This will show placeholder images instead of real posters.

BYPASS_POSTER_FETCHING = True # Set to False if you want to try fetching real posters

If you want to try fetching real posters, change this to False after ensuring your API key is correct and troubleshooting any network/firewall issues.

📂 Project Structure
.
├── app.py                      # The main Streamlit web application
├── movie_recommendation.ipynb  # (Optional) Jupyter Notebook for data preparation
├── venv/                       # Python virtual environment
└── model/                      # Contains pre-processed data files
│   ├── movie_data.csv          # Cleaned movie data
│   └── similarity.pkl          # Movie similarity matrix
└── README.md                   # This file!

💡 Future Ideas
Add a search bar for movies.

Display more movie details (genre, year, rating).

Explore different recommendation algorithms.

Deploy the app online for others to use!
