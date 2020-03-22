import heapq
from collections import Counter

import storm


class TopNFinderBolt(storm.BasicBolt):
    # Initialize this instance
    def initialize(self, conf, context):
        self._conf = conf
        self._context = context

        storm.logInfo("TopNFinder bolt instance starting...")

        # TODO:
        # Task: set N
        self.N = conf['N']
        self._counter = Counter()
        # End

        # Hint: Add necessary instance variables and classes if needed

    def process(self, tup):
        '''
        TODO:
        Task: keep track of the top N words
        Hint: implement efficient algorithm so that it won't be shutdown before task finished
              the algorithm we used when we developed the auto-grader is maintaining a N size min-heap
        '''
        word = tup.values[0]
        ct = int(tup.values[1])
        if len(word) > 0:
            self._counter[word] += ct
            topn = self._counter.most_common(self.N)
            s = ""
            for w, c in topn:
                s = s + w +', '
            s = s[:-2]
            storm.logInfo("Emitting %s:%s" % ("top-N", s))
            storm.emit(["top-N", s])
        # End


# Start the bolt when it's invoked
TopNFinderBolt().run()
