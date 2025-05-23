My Movie Recommendation System

Welcome to my Movie Recommendation System! This is a simple web app built with Streamlit that helps you find new movies. Just pick a movie, and it suggests five similar ones.

🌟 Features

Easy to Use: Simple movie selection dropdown.

Smart Recommendations: Get 5 similar movie suggestions.

Optional Posters: Can show movie posters (requires TMDb API Key).

Reliable: Built with error handling for smooth use.

🛠️ Technologies Used

Python

Streamlit

Pandas

Scikit-learn

Requests

The Movie Database (TMDb) API

🚀 Getting Started
Here's how to get the app running on your computer:

Prerequisites
You'll need Python 3.7+ and pip.

▶️ How to Run the Application
Activate your virtual environment (if not already active).

Go to your project's main directory (where app.py is).

Run the app:

streamlit run app.py

Your browser will open the app at http://localhost:8501.

🖼️ Important Note on Movie Posters

The app tries to get movie posters from TMDb. If you see "Connection error" or no posters, it's usually a network/firewall issue or an incorrect TMDb API key.

Get Your TMDb API Key: Sign up at themoviedb.org, go to Account Settings -> API, and get a v3 API key.

Add Key to app.py: Put your key in app.py where it says TMDb_API_KEY = "YOUR_API_KEY".

Bypass Posters: If you still have issues, set BYPASS_POSTER_FETCHING = True in app.py. This will show placeholder images instead of trying to fetch real posters.

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
Add a movie search bar.

Show more movie details.

Try different recommendation methods.

Deploy the app online.

