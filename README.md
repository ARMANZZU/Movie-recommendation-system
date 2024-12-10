# Movie Recommendation System

## Overview
The **Movie Recommendation System** is a Flask-based web application that recommends movies based on user input. It combines Python libraries, machine learning techniques, and the OMDb API to deliver personalized movie suggestions along with detailed movie information.

## Features
- **Input Matching**: Uses text similarity to match user input with movie titles.
- **Recommendation Engine**: Suggests movies based on genre, keywords, and other metadata.
- **OMDb Integration**: Fetches movie details like posters, genre, and plot for enhanced recommendations.
- **Interactive UI**: A user-friendly HTML interface for seamless interaction.

## Technologies Used
- **Backend**: Python, Flask
- **Frontend**: HTML, Jinja templates
- **Libraries**:
  - **Pandas**: Data manipulation
  - **Numpy**: Data processing
  - **Scikit-learn**: Cosine similarity for recommendations
  - **TfidfVectorizer**: Feature extraction
  - **Seaborn & Matplotlib**: For potential data visualizations
- **API**: OMDb API for movie details

## How It Works
1. User inputs their favorite movie.
2. The application matches the input with movie titles using text similarity.
3. Recommendations are generated based on metadata such as genres, keywords, and cast.
4. OMDb API fetches detailed information (e.g., poster, plot) about recommended movies.
