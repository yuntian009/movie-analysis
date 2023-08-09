import pandas as pd


def clean_data(users, ratings, movies) -> pd.DataFrame:
    data = pd.merge(pd.merge(ratings, users), movies)
    data.drop('Unnamed: 3', axis=1, inplace=True)
    return data


def mean_rate_by_gender(df: pd.DataFrame) -> pd.DataFrame:
    result = df.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
    ratings_by_title = df.groupby('title').size()
    active_titles = ratings_by_title.index[ratings_by_title >= 250]
    mean_ratings = result.loc[active_titles]
    return mean_ratings


def female(df: pd.DataFrame) -> pd.DataFrame:
    result = df.sort_values(by='F', ascending=False)
    return result[:10]


def male(df: pd.DataFrame) -> pd.DataFrame:
    result = df.sort_values(by='M', ascending=False)
    return result[:10]


def compute_diff(df: pd.DataFrame) -> None:
    df['Difference'] = abs(df['M'] - df['F'])
