import pickle
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import re
import string


def remove_noise(tweet_tokens, stop_words=()):
    """
    :param tweet_tokens: tweet tokens
    :param stop_words: list of stop words
    :return: returns the word without extra characters -> cleaned words
    """

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        # clean all the tokens
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)
        token = re.sub("(@[A-Za-z0-9_]+)", "", token)

        if tag.startswith("NN"):
            # noun
            pos = 'n'
        elif tag.startswith('VB'):
            # verb
            pos = 'v'
        else:
            # adjective
            pos = 'a'
        # lemmantize the words
        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())

    return cleaned_tokens


class SentimentClassifier():
    def __init__(self):
        """
        Initialize SentimentClassifier class
        """
        f = open('classifier.h5', 'rb')

        self.classifier = pickle.load(f)

        f.close()

    def predict(self, phrase: str) -> str:
        """
        Predict if the phrase is positive or negative. This model was found to be about 75% accurate 
        :param phrase: phrase being predicted on
        :return: returns Positive if the phrase is predicted as a positive connotation, else Negative
        """
        token = remove_noise(word_tokenize(phrase))
        predictionVal = self.classifier.classify(
            dict([t, True] for t in token))
        return predictionVal
