from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

messages = [
    "Win a free prize now",
    "Claim your cash reward",
    "Are we meeting tomorrow?",
    "Please send me the notes"
]

labels = ["spam", "spam", "normal", "normal"]

model = make_pipeline(
    CountVectorizer(),
    MultinomialNB()
)

model.fit(messages, labels)

print(model.predict(["Are you free tomorrow?"]))