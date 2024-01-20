import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

data = {
    'movie': ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5'],
    'genre': ['Action', 'Drama', 'Comedy', 'Action|Drama', 'Comedy|Romance']
}

movies_df = pd.DataFrame(data)
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['genre'])


cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def get_movie_recommendations(movie_title, cosine_sim=cosine_sim):
    movie_index = movies_df[movies_df['movie'] == movie_title].index[0]
    sim_scores = list(enumerate(cosine_sim[movie_index]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    movie_indices = [i[0] for i in sim_scores]
    return movies_df['movie'].iloc[movie_indices[1:4]]

input_movie = 'Movie1'
recommendations = get_movie_recommendations(input_movie)
print(f"Recommended movies for '{input_movie}':")
print(recommendations)
