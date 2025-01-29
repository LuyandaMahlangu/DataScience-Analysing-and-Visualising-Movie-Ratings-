import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
names = '/Users/luyandamahlangu/Desktop/Projects/RottenTomatoesMovies.csv'
df= pd.read_csv(names)

# Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(subset=['audience_rating'], inplace=True)
df['audience_rating'] = pd.to_numeric(df['audience_rating'], errors='coerce')

# Summary Statistics
mean_rating = df['audience_rating'].mean()
median_rating = df['audience_rating'].median()
mode_rating = df['audience_rating'].mode()[0]

# Streamlit App
st.title("Movie Ratings Analysis Dashboard")

st.subheader("Summary Statistics")
st.write(f"**Mean Rating:** {mean_rating:.2f}")
st.write(f"**Median Rating:** {median_rating:.2f}")
st.write(f"**Mode Rating:** {mode_rating:.2f}")

# Histogram of Ratings
st.subheader("Distribution of Movie Ratings")
fig, ax = plt.subplots(figsize=(10, 6))
sns.histplot(df['audience_rating'], bins=20, kde=True, ax=ax)
st.pyplot(fig)

# Top-Rated Movies
st.subheader("Top 10 Highest-Rated Movies")
top_movies = df[df['audience_rating'] > 90].sort_values(by="audience_rating", ascending=False)
st.write(top_movies[['movie_title', 'audience_rating']].head(10))

# Genre Analysis
df['genre'] = df['genre'].astype(str)  # Convert to string if needed
df_exploded = df.explode('genre')  # Split multiple genres into separate rows
genre_ratings = df_exploded.groupby('genre')['audience_rating'].mean().sort_values(ascending=False)

st.subheader("Top 10 Genres by Average Rating")
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x=genre_ratings.index[:10], y=genre_ratings.values[:10], ax=ax)
plt.xticks(rotation=90)
st.pyplot(fig)



