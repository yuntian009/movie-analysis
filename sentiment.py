import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from nltk.corpus import stopwords
from sklearn.metrics import confusion_matrix, classification_report
import nltk
nltk.download('stopwords')


df = pd.read_csv('data/IMDB_Dataset.csv')
df['sentiment_num'] = df['sentiment'].apply(lambda x: 1 if x == 'positive' else -1)

stop_words = set(stopwords.words('english'))
char_names = ['one', 'also']


def remove_stopwords(text):
    filtered_text = []
    for word in text.split():
        if (word.lower() not in stop_words) & (word.lower() not in char_names):
            filtered_text.append(word)
    return ' '.join(filtered_text)


df['review'] = df['review'].apply(remove_stopwords)


def remove_punctuation(text):
    final = "".join(u for u in text if u not in ("?", ".", ";", ":",  "!", '"'))
    return final


df['review'] = df['review'].apply(remove_punctuation)

# random split train and test data
# X_train, X_test, y_train, y_test = \
#     train_test_split(df['review'], df['sentiment_num'], test_size=0.2)

index = df.index
df['random_number'] = np.random.randn(len(index))
train = df[df['random_number'] < 0.8]
test = df[df['random_number'] >= 0.8]

# count vectorizer:
vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
train_matrix = vectorizer.fit_transform(train['review'])
test_matrix = vectorizer.transform(test['review'])

# Logistic Regression
lr = LogisticRegression(max_iter=1000)

X_train = train_matrix
X_test = test_matrix
y_train = train['sentiment']
y_test = test['sentiment']

lr.fit(X_train, y_train)
predictions = lr.predict(X_test)

# find accuracy, precision, recall:
new = np.asarray(y_test)
confusion_matrix(predictions, y_test)

print(classification_report(predictions, y_test))