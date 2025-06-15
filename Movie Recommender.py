import pandas as pd
movies_path = "/home/hammadali08/Downloads/ml-latest-small/movies.csv"
ratings_path = "/home/hammadali08/Downloads/ml-latest-small/ratings.csv"

movies = pd.read_csv(movies_path, low_memory=False)
ratings = pd.read_csv(ratings_path, low_memory=False)

rating_stats = ratings.groupby('movieId').agg(
    vote_count=('rating', 'count'),
    vote_average=('rating', 'mean')
).reset_index()

metadata = pd.merge(movies, rating_stats, on='movieId')

C = metadata['vote_average'].mean()
m = metadata['vote_count'].quantile(0.90)

print("=== Movie Recommendation Preferences ===")
min_rating = float(input("Minimum average rating (Like 3.5): "))
min_votes = int(input("Minimum number of votes (Like 50): "))
preferred_genres = input("Preferred genres (comma-separated, Like Action,Drama,Adventure,Romance): ").split(',')

preferred_genres = [genre.strip().lower() for genre in preferred_genres]
filtered = metadata[
    (metadata['vote_average'] >= min_rating) &
    (metadata['vote_count'] >= min_votes) &
    (metadata['genres'].str.lower().str.contains('|'.join(preferred_genres)))
].copy()

def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    return (v / (v + m) * R) + (m / (m + v) * C)

filtered['score'] = filtered.apply(weighted_rating, axis=1)
filtered = filtered.sort_values('score', ascending=False)

print("\nTop Recommended Movies:")
print(filtered[['title', 'genres', 'vote_count', 'vote_average', 'score']].head(15))