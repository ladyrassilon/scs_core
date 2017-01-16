'''
Created on 9 Aug 2016

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
'''

import _csv
import sys


# --------------------------------------------------------------------------------------------------------------------

class Histogram(object):
    '''
    classdocs
    '''

    __HEADER_BIN = ".bin"
    __HEADER_COUNT = ".count"


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, minimum, maximum, bin_count, path):
        '''
        Constructor
        '''
        self.__minimum = minimum
        self.__maximum = maximum
        self.__bin_count = bin_count

        self.__path = path

        self.__counts = [0] * bin_count
        self.__max_count = int(0)

        self.__delta = (maximum - minimum) / bin_count


    def __len__(self):
        return self.__bin_count


    # ----------------------------------------------------------------------------------------------------------------

    def append(self, datum):
        # reject out-of-range
        if datum < self.__minimum or datum > self.__maximum:
            raise ValueError("datum out of range:%f" % datum)

        # compute index...
        offset = datum - self.__minimum
        index = int(offset // self.__delta)

        # update counts...
        self.__counts[index] += 1

        if self.__counts[index] > self.__max_count:
            self.__max_count = int(self.__counts[index])

        return index, self.__counts[index]


    def to_csv(self, filename = None):
        file = sys.stdout if filename is None else open(filename, "w")
        writer = _csv.writer(file)

        writer.writerow((self.__path + Histogram.__HEADER_BIN, self.__path + Histogram.__HEADER_COUNT))

        for i in range(self.bin_count):
            writer.writerow((format(self.__bin(i), '.6f'), self.__counts[i]))

        if filename is not None:
            file.close()


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def bins(self):
        return [self.__bin(i) for i in range(self.__bin_count)]


    @property
    def minimum(self):
        return self.__minimum


    @property
    def maximum(self):
        return self.__maximum


    @property
    def bin_count(self):
        return self.__bin_count


    @property
    def path(self):
        return self.__path


    @property
    def delta(self):
        return self.__delta


    @property
    def max_count(self):
        return self.__max_count


    @property
    def counts(self):
        return self.__counts


    # ----------------------------------------------------------------------------------------------------------------

    def __bin(self, index):
        return self.__minimum + (index * self.__delta)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "Histogram:{minimum:%0.6f, maximum:%0.6f, bin_count:%d, delta:%0.6f, max_count:%d, counts:%s, path:%s}" % \
                    (self.minimum, self.maximum, self.bin_count, self.delta, self.max_count, self.counts, self.path)
