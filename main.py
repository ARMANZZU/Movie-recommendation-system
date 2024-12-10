import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies_data = pd.read_csv('C:\ML\movie recommend using flask\movies.csv')

print("Data loaded successfully!\n")

selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']

vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

similarity = cosine_similarity(feature_vectors)

movie_name = input('Enter your favourite movie name: ')

list_of_all_titles = movies_data['title'].tolist()

find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
if not find_close_match:
    print("Sorry, no close match found. Please try again.")
else:
    close_match = find_close_match[0]

    index_of_the_movie = movies_data[movies_data.title == close_match].index.values[0]

    similarity_scores = list(enumerate(similarity[index_of_the_movie]))

    sorted_similar_movies = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    print("\nMovies suggested for you based on your favourite movie '" + movie_name + "':\n")

    i = 1
    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies_data.iloc[index]['title']
        if i <= 5:
            print(f"{i}. {title_from_index}")
            i += 1
