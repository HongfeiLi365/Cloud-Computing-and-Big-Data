# import os
# from os.path import join
from time import sleep

# from streamparse import Spout
import storm


class FileReaderSpout(storm.Spout):

    def initialize(self, conf, context):
        self._conf = conf
        self._context = context
        self._complete = False

        storm.logInfo("Spout instance starting...")

        # TODO:
        # Task: Initialize the file reader

        with open(self._conf['filepath']) as f:
            lines = f.readlines()
            lines = [x.strip() for x in lines]
        self.lines = lines
        self.pos=0
        self.max_pos = len(lines) - 1
        # End

    def nextTuple(self):
        # TODO:
        # Task 1: read the next line and emit a tuple for it
        # Task 2: don't forget to sleep for 1 second when the file is entirely read to prevent a busy-loop
        
        if self.pos <= self.max_pos:
            sentence = self.lines[self.pos]
            self.pos = self.pos + 1
            storm.logInfo("Emiting %s" % sentence)
            storm.emit([sentence])
            if self.pos > self.max_pos:
                sleep(1)
        else:
            sleep(1)
        
        # End


# Start the spout when it's invoked
FileReaderSpout().run()
