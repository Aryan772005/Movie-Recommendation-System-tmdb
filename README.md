Live link - https://movie-recommendation-system-tmdb-sz2csvfycz5596jnr3q9cy.streamlit.app/
run the live link to test

 
 
 
 
 
 <img width="1911" height="917" alt="image" src="https://github.com/user-attachments/assets/0eef3f76-c009-4ad5-a3c4-5989768615d2" />



 Live link - https://movie-recommendation-system-tmdb-sz2csvfycz5596jnr3q9cy.streamlit.app/
run the live link to test
# Aryan's Recommendation System

This project is a personal learning experience in machine learning and data science. The goal was to build a movie recommendation system using real movie data and deploy it as a simple Streamlit web app.

## What I learned

- Loading and exploring movie datasets
- Building similarity-based recommendations using a numeric similarity matrix
- Working with pickle files to store and load preprocessed data
- Fetching movie posters from TMDB and displaying them in a UI
- Designing a user-friendly Streamlit interface
- Managing Git and publishing the project to GitHub

## How it was made

1. Collected movie metadata and credit data from the TMDB dataset.
2. Preprocessed the data and built a similarity matrix between movies.
3. Stored the processed movie data and similarity matrix in `movies.pkl` and `similarity.pkl`.
4. Created a single-file Streamlit app in `app.py` to load the data, let users select a movie, and show recommended movies.
5. Added a clean UI with a dark theme, a sidebar, and poster cards.

## Features

- Select any movie from a dropdown list
- Generate five recommended movies based on similarity
- Display movie poster images and titles
- Optional TMDB API key support for poster loading
- Fallback poster loading from public TMDB pages when no API key is available

## Files included

- `app.py` — main Streamlit application
- `movies.pkl` — preprocessed movie data
- `similarity.pkl` — precomputed similarity matrix
- `tmdb_5000_movies.csv` — raw movie dataset
- `tmdb_5000_credits.csv` — raw credits dataset
- `movie_recommender.ipynb` — exploratory notebook used while learning

## How to run

1. Install dependencies:
   ```bash
   pip install streamlit requests
   ```
2. Run the app:
   ```bash
   streamlit run app.py
   ```

## Final note

This project was built to practice machine learning and data science concepts while also creating a clean and professional web interface. It is a learning project, and the main focus was on making the recommendation logic work together with a smooth user experience.
