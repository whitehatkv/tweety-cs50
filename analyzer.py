import nltk
import string

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        
        #positive word set
        self.positives = set()
        with open(positives,'r') as lines:
            for line in lines:
                if not line.startswith(';'):
                    self.positives.add(line.strip())
        lines.close()        
        
        #negative word set
        self.negatives = set()
        file = open(negatives,'r')
        for line in file.readlines():
            if not line.startswith(';'):
                self.negatives.add(line.strip())
        file.close()

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""

        checksum = int(0)
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        for word in tokens:
            if word.lower() in self.positives:
                checksum+=1
            elif word.lower() in self.negatives:
                checksum-=1
            else:
                checksum+=0
        
        return checksum