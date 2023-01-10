import pandas as pd
import streamlit as st
import pickle
import pandas
import requests
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_id) :
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=4702314f8b1c942afb29e1e0243b88a9&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie) :
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1: 6]
    rec = []
    rec_p = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        rec.append(movies.iloc[i[0]].title)
        rec_p.append(fetch_poster(movie_id))
    return rec, rec_p


st.title("Movie Recommendation System")

sel_mov_name = st.selectbox(
    'Select a movie you have watched: ' ,
    movies['title'].values
)

if st.button('Recommend') :
    names, posters = recommend(sel_mov_name)
    col1, col2, col3, col4, col5 = st.columns([2,2,2,2,2])
    with col1 :
        st.text(names[0])
        st.image(posters[0])
    with col2 :
        st.text(names[1])
        st.image(posters[1])
    with col3 :
        st.text(names[2])
        st.image(posters[2])
    with col4 :
        st.text(names[3])
        st.image(posters[3])
    with col5 :
        st.text(names[4])
        st.image(posters[4])



st.text("-Developed by : Pankaj Chowdhury, B.Engg (J.U.)")
st.text("Details : This web application is based on  the concept of Vectorization in Machine Learning. Using this,it is used to determine the five most similar movies to the one provided.")
