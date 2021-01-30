from classifier import SentimentClassifier


def test_classifer():
    """
    Test the classifier works
    """
    model = SentimentClassifier()
    badPhrase = "Fuck you bitch"
    assert model.predict(badPhrase) == 'Negative'

    goodPhrase = "You look good"
    assert model.predict(goodPhrase) == 'Positive'
