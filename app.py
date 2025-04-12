import streamlit as st
import pickle
import pandas as pd
import requests
import gzip

@st.cache_data
def load_movies():
    movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
    return pd.DataFrame(movie_dict)

@st.cache_resource
def load_similarity():
    with gzip.open('similarity.pkl.gz', 'rb') as f:
        return pickle.load(f)

@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=94677bbcaa3bada84863ff8078e11bdb&language=en-US'
    )
    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"


movies = load_movies()
similarity = load_similarity()

def recommend_movie(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    rec_movies = []
    rec_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        rec_movies.append(movies.iloc[i[0]].title)
        rec_movie_posters.append(fetch_poster(movie_id))
    return rec_movies, rec_movie_posters

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select the movie!',
    movies['title'].values
)

if st.button('Recommend movie!'):
    names, posters = recommend_movie(selected_movie_name)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])
