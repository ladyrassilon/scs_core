"""
Created on 21 Mar 2017

@author: Bruno Beloff (bruno.beloff@southcoastscience.com)
"""

from scs_core.osio.client.rest_client import RESTClient
from scs_core.osio.data.user import User


# --------------------------------------------------------------------------------------------------------------------

class UserManager(object):
    """
    classdocs
    """

    # ----------------------------------------------------------------------------------------------------------------

    def __init__(self, http_client, api_key):
        """
        Constructor
        """
        self.__rest_client = RESTClient(http_client, api_key)


    # ----------------------------------------------------------------------------------------------------------------

    def find(self, user_id):
        path = '/v1/users/' + user_id

        # request...
        self.__rest_client.connect()

        try:
            response_jdict = self.__rest_client.get(path)
        except RuntimeError:
            response_jdict = None

        self.__rest_client.close()

        user = User.construct_from_jdict(response_jdict)

        return user


    def find_members_of_org(self, org_id):
        pass


    # ----------------------------------------------------------------------------------------------------------------

    def update(self, user):
        pass                    # TODO: implement update(..)


    # ----------------------------------------------------------------------------------------------------------------

    def __str__(self, *args, **kwargs):
        return "UserManager:{rest_client:%s}" % self.__rest_client