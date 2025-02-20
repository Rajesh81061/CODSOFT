import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets with corrected paths
movies = pd.read_csv(r"C:\Users\Rajesh\movie recommendation\movies.csv")
ratings = pd.read_csv(r"C:\Users\Rajesh\movie recommendation\ratings.csv")

# Create a pivot table of user ratings for movies
pivot_table = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)

# Compute cosine similarity
similarity_matrix = cosine_similarity(pivot_table)
similarity_df = pd.DataFrame(similarity_matrix, index=pivot_table.index, columns=pivot_table.index)

# Function to get recommendations with movie names
def get_recommendations(user_id, similarity_df, ratings, movies, num_recommendations=5):
    if user_id not in similarity_df.index:
        print("User ID not found in dataset.")
        return pd.DataFrame()  # Return empty DataFrame if user is not in dataset

    similarity_scores = similarity_df.loc[user_id].sort_values(ascending=False)
    similar_users = similarity_scores.iloc[1:num_recommendations + 1].index

    movie_recommendations = pd.DataFrame(columns=['movieId', 'title'])

    for similar_user in similar_users:
        user_ratings = ratings[ratings['userId'] == similar_user]
        user_ratings = user_ratings.merge(movies, on='movieId')
        top_movies = user_ratings.sort_values(by='rating', ascending=False)[['movieId', 'title']].head(num_recommendations)
        
        # Append recommendations and ensure uniqueness
        movie_recommendations = pd.concat([movie_recommendations, top_movies]).drop_duplicates(subset=['movieId'])

    return movie_recommendations.head(num_recommendations)

# Example usage
user_id = 1  # Replace with an actual userId from ratings dataset
recommendations = get_recommendations(user_id, similarity_df, ratings, movies)
print(recommendations)
