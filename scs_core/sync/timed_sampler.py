"""
Created on 18 Aug 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from abc import abstractmethod

from scs_core.sync.interval_timer import IntervalTimer


# --------------------------------------------------------------------------------------------------------------------

class TimedSampler(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, interval, sample_count=None):
        """
        Constructor
        """
        self.__timer = IntervalTimer(interval)
        self.__sample_count = sample_count


    # ----------------------------------------------------------------------------------------------------------------

    @abstractmethod
    def sample(self):
        pass


    def samples(self):
        if self.__sample_count is None:
            while self.__timer.true():
                yield self.sample()

        else:
            for _ in self.__timer.range(self.__sample_count):
                yield self.sample()


    # ----------------------------------------------------------------------------------------------------------------

    def reset_timer(self):
        self.__timer = IntervalTimer(self.__timer.interval)


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def timer(self):
        return self.__timer


    @property
    def sample_count(self):
        return self.__sample_count


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "TimedSampler:{timer:%s, sample_count:%s}" % (self.__timer, self.__sample_count)