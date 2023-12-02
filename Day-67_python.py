# Implement a basic recommendation system for movies.
print("\nRuban Gino Singh - Day 67 of #100DaysOfCode\n")

print("Python program to Implement a Basic Recommendation for Movies\n")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity

# Load MovieLens dataset (download from https://grouplens.org/datasets/movielens/)
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

movie_ratings = pd.merge(ratings, movies, on='movieId')
user_movie_ratings = movie_ratings.pivot_table(index='userId', columns='title', values='rating')
user_movie_ratings = user_movie_ratings.fillna(0)
train_data, test_data = train_test_split(user_movie_ratings, test_size=0.2, random_state=42)
user_similarity = cosine_similarity(train_data)
user_similarity_df = pd.DataFrame(user_similarity, index=train_data.index, columns=train_data.index)

def get_movie_recommendations(user_id, num_recommendations=5):
    user_ratings = train_data.loc[user_id]
    similar_users = user_similarity_df[user_id]
    
    weighted_avg_ratings = train_data.mul(similar_users, axis=0).sum(axis=1) / (similar_users.sum() + 1e-10)

    unrated_movies = user_ratings[user_ratings == 0].index

    recommendations = weighted_avg_ratings[unrated_movies].sort_values(ascending=False).head(num_recommendations)
    
    return recommendations.index

user_id = 1
recommendations = get_movie_recommendations(user_id, num_recommendations=5)

print(f"Top 5 movie recommendations for User {user_id}:")
for i, movie_title in enumerate(recommendations, start=1):
    print(f"{i}. {movie_title}")

# --------------------------------------------------------- #