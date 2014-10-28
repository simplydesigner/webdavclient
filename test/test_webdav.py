import pytest
import os
from webdav.client import Client, WebDavException

def options():
    server = os.environ["WEBDAV_SERVER"]
    prefix = "{server}{separate}".format(server=server.upper(), separate="_")

    options = dict()
    connection_attributes = ["hostname", "login", "password"]
    for attribute in connection_attributes:
        key = "{prefix}{attribute}".format(prefix=prefix, attribute=attribute.upper())
        options[attribute] = os.environ[key]

class TestAuthenticate:

    #@staticmethod
    def test_simple(self):

        client = Client(options=options())
        assert client.check()



