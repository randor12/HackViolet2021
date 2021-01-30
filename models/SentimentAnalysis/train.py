from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk import FreqDist
import re
import string
from nltk import classify
from nltk import NaiveBayesClassifier
import pickle

positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = ["fuck you", "shit", "bitch", "dumb ass", "freak",
                   "weirdo", "you suck", "balls", "loser", 'fucker', 'maybe you should have thought of that asshole',
                   "what an asshole", "why are you fucking retarded", "are you retarded", "get fucked",
                   "why are you a bitch", "fuck", "what the fuck", "what the hell are you doing",
                   "you should go die fucker"] + twitter_samples.strings('negative_tweets.json') + ['you suck balls', 'suck', 'you fucking suck']


stop_words = stopwords.words('english')


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


positive_wrds = []
negative_wrds = []

for tokens in positive_tweets:
    # positive bag of cleaned words
    t = word_tokenize(tokens)
    clean = remove_noise(t, stop_words=stop_words)
    positive_wrds.append(clean)

for tokens in negative_tweets:
    # negative bag of cleaned words

    t = remove_noise(word_tokenize(tokens), stop_words)
    negative_wrds.append(t)


def get_all_wrds(lst):
    """
    :param lst: list of words
    :return: returns the frequency of each word
    """
    for tokens in lst:
        # get all tokens
        for t in tokens:
            # get all words
            yield t


all_pos_wrds = get_all_wrds(positive_wrds)
all_neg_wrds = get_all_wrds(negative_wrds)

freq_dist_pos = FreqDist(all_pos_wrds)
freq_dist_neg = FreqDist(all_neg_wrds)


def get_tweets_for_model(cleaned_lst):
    """
    :param cleaned_lst: cleaned list
    :return dictionary of cleaned list
    """
    for tweet_token in cleaned_lst:
        yield dict([token, True] for token in tweet_token)


pos_token_for_model = get_tweets_for_model(positive_wrds)
neg_token_for_model = get_tweets_for_model(negative_wrds)

pos_token_for_model = list(pos_token_for_model)
neg_token_for_model = list(neg_token_for_model)

pos_dataset = [(tweet_dict, "Positive") for tweet_dict in pos_token_for_model]
neg_dataset = [(tweet_dict, "Negative") for tweet_dict in neg_token_for_model]


train_data = pos_dataset[:len(pos_dataset) // 2] + \
    neg_dataset[:len(neg_dataset) // 2]

test_data = pos_dataset[len(pos_dataset) // 2:] + \
    neg_dataset[len(neg_dataset) // 2:]

f = open('classifier.h5', 'wb')

classifier = NaiveBayesClassifier.train(train_data)

pickle.dump(classifier, f)
f.close()

print('Accuracy: ', classify.accuracy(classifier, test_data) * 100)

custom_tweet = 'This item sucks balls, fucker'
custom_token = remove_noise(word_tokenize(custom_tweet))
predictionVal = classifier.classify(
    dict([token, True] for token in custom_token))
print(custom_tweet, ": ", predictionVal)
custom_tweet = 'That looks great'
custom_token = remove_noise(word_tokenize(custom_tweet))
predictionVal = classifier.classify(
    dict([token, True] for token in custom_token))
print(custom_tweet, ": ", predictionVal)
