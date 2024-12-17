import requests
import streamlit as st
from flask import Flask, render_template, request

app = Flask(__name__)

OMDB_API_KEY = 'b4c718e9'

def get_movie_details(movie_name):
    
    search_url = f"http://www.omdbapi.com/?s={movie_name}&apikey={OMDB_API_KEY}"
    search_response = requests.get(search_url)
    search_data = search_response.json()

    if search_data['Response'] == 'True':
    
        related_movies = search_data['Search'][:5] 

        recommended_movies = []
        for movie in related_movies:
            movie_id = movie['imdbID']
            movie_details_url = f"http://www.omdbapi.com/?i={movie_id}&apikey={OMDB_API_KEY}"
            movie_details_response = requests.get(movie_details_url)
            movie_details_data = movie_details_response.json()

            if movie_details_data['Response'] == 'True':
                recommended_movies.append({
                    'title': movie_details_data['Title'],
                    'poster': movie_details_data['Poster'],
                    'year': movie_details_data['Year'],
                    'genre': movie_details_data['Genre'],
                    'plot': movie_details_data['Plot']
                })

        return recommended_movies
    else:
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form['movie_name']
    recommended_movies = get_movie_details(movie_name)

    if recommended_movies:
        return render_template('index.html', movie_name=movie_name, recommended_movies=recommended_movies)
    else:
        message = "Movie not found. Please try another movie."
        return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
