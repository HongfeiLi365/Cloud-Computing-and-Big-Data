import storm
# Counter is a nice way to count things,
# but it is a Python 2.7 thing
from collections import Counter


class CountBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        self._counter = Counter()
        storm.logInfo("Counter bolt instance starting...")

        # Hint: Add necessary instance variables and classes if needed

    def process(self, tup):
        # TODO
        # Task: word count
        # Hint: using instance variable to tracking the word count
        word = tup.values[0]
        self._counter[word] += 1
        count = self._counter[word]
        storm.logInfo("Emitting %s:%s" % (word, count))
        storm.emit([word, count])
        # End


# Start the bolt when it's invoked
CountBolt().run()
