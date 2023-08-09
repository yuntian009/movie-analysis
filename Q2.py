import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import textwrap

dataframe = pd.read_csv('data/movies.csv')

sns.scatterplot(x='budget', y='gross', data=dataframe)
plt.savefig('results/q2_2.png', bbox_inches='tight')

plt.cla()

top_10_directors = dataframe['director'].value_counts().nlargest(10)
wrapped_director_names = ['\n'.join(textwrap.wrap(name, width=15)) for name in top_10_directors.index]
sns.barplot(x=top_10_directors.values, y=wrapped_director_names)
plt.title('Top 10 Directors by Number of Movies')
plt.xlabel('Number of Movies')
plt.ylabel('Director')
plt.savefig('results/q2_3.png', bbox_inches='tight')

plt.cla()

woody_allen_movies = dataframe[dataframe['director'] == 'Woody Allen']
fig, ax = plt.subplots()
ax.plot(woody_allen_movies['name'], woody_allen_movies['budget'], label='Budget')
ax.plot(woody_allen_movies['name'], woody_allen_movies['gross'], label='Gross')
ax.set_title("Woody Allen's Movies: Budget vs Gross")
ax.set_xlabel('Movie Title')
ax.set_ylabel('Amount (in millions)')
ax.legend()
plt.xticks(rotation=90)
plt.savefig('results/q2_4.png', bbox_inches='tight')

plt.cla()

top_10 = dataframe.nlargest(10, 'gross')[['name', 'budget', 'gross']].set_index('name')
fig, axs = plt.subplots(nrows=2, figsize=(10, 10))
axs[0].set_xlim(0, 3000000000)
sns.barplot(x=top_10['gross'], y=top_10.index, ax=axs[0])
axs[0].set_title('Plot 1')
sns.barplot(x=top_10['budget'], y=top_10.index, ax=axs[1])
axs[1].set_xlim(0, 3000000000)
axs[1].set_title('Plot 2')
fig.suptitle('Top 10 Highest Revenue Movie and its budget')
plt.savefig('results/q2.png', bbox_inches='tight')
