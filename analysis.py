import pandas as pd
import data_processing as dp
import matplotlib.pyplot as plt
import numpy as np


def main():
    users = pd.read_csv("data/users.csv", sep=";")
    ratings = pd.read_csv("data/ratings.csv", sep=";")
    movies = pd.read_csv("data/movies_2.csv", sep=";", encoding="latin")

    merged_df = dp.clean_data(users, ratings, movies)
    mean_ratings = dp.mean_rate_by_gender(merged_df)

    top_female_ratings = dp.female(mean_ratings)
    top_male_ratings = dp.male(mean_ratings)
    dp.compute_diff(mean_ratings)
    sorted_by_diff = mean_ratings.sort_values(by='Difference', ascending=False)

    # Set the chart data
    female_ratings = top_female_ratings['F'].values
    male_ratings = top_male_ratings['M'].values
    movie_titles = top_female_ratings.index.values

    # Set the chart parameters
    bar_width = 0.35
    index = np.arange(len(movie_titles))

    # Create a grouped bar chart
    fig, ax = plt.subplots()
    ax.bar(index, female_ratings, bar_width, label='Female')
    ax.bar(index + bar_width, male_ratings, bar_width, label='Male')

    # Set the chart title and labels
    ax.set_title('Top 10 Movies with the Highest Mean Ratings by Gender')
    ax.set_xlabel('Movie Title')
    ax.set_ylabel('Mean Rating')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(movie_titles, rotation=90)
    ax.legend()
    plt.savefig('results/q1_1.png', bbox_inches='tight')

    plt.cla()

    # Select the top 10 most divisive movies
    divisive_movies = sorted_by_diff.head(10)

    # Create a horizontal bar chart
    fig, ax = plt.subplots()
    ax.barh(divisive_movies.index, divisive_movies['Difference'], height=0.8)

    # Set the chart title and labels
    ax.set_title('Top 10 Most Divisive Movies by Gender')
    ax.set_xlabel('Difference in Mean Rating')
    ax.set_ylabel('Movie Title')

    # Invert the y-axis to display movies with highest ratings at the top
    ax.invert_yaxis()
    plt.savefig('results/q1_2.png', bbox_inches='tight')


if __name__ == "__main__":
    main()