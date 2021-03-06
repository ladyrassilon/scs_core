"""
Created on 1 Jan 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""


# --------------------------------------------------------------------------------------------------------------------

class GPLoc(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    @classmethod
    def __deg(cls, composite):
        whole_deg = float(composite[:2])
        mins = float(composite[2:])

        deg = whole_deg + (mins / 60)

        return round(deg, 7)


    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, lat, ns, lng, ew):
        """
        Constructor
        """
        self.__lat = lat                # string - ddmm.mmmmm
        self.__ns = ns                  # string - { N | S}

        self.__lng = lng                # string - dddmm.mmmmm
        self.__ew = ew                  # string - { E | W }


    # ----------------------------------------------------------------------------------------------------------------

    def has_position(self):
        return self.deg_lat() is not None and self.deg_lng() is not None


    # ----------------------------------------------------------------------------------------------------------------

    def deg_lat(self):
        if self.__lat is None or self.__ns is None:
            return None

        deg = GPLoc.__deg(self.__lat)

        if self.__ns == "S":
            deg = -deg

        return deg


    def deg_lng(self):
        if self.__lng is None or self.__ew is None:
            return None

        deg = GPLoc.__deg(self.__lng)

        if self.__ew == "W":
            deg = -deg

        return deg


    # ----------------------------------------------------------------------------------------------------------------

    @property
    def lat(self):
        return self.__lat


    @property
    def ns(self):
        return self.__ns


    @property
    def lng(self):
        return self.__lng


    @property
    def ew(self):
        return self.__ew


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "GPLoc:{lat:%s, ns:%s, lng:%s, ew:%s}" % (self.lat, self.ns, self.lng, self.ew)
