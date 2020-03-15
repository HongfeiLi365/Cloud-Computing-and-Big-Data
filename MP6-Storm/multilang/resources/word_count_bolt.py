import storm
# Counter is a nice way to count things,
# but it is a Python 2.7 thing
from collections import Counter


class CountBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context

        storm.logInfo("Counter bolt instance starting...")

        # Hint: Add necessary instance variables and classes if needed

    def process(self, tup):
        # TODO
        # Task: word count
        # Hint: using instance variable to tracking the word count
        pass
        # End


# Start the bolt when it's invoked
CountBolt().run()
