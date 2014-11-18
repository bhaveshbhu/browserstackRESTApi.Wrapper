#Bhavesh Sharma
#Date : 17-11-14

"""
Python wrapper for Browserstack API
"""


class BrowserStackError(Exception):
    """exception throw"""

    def __init__(self, reason, response=None):
        self.reason = unicode(reason)
        self.response = response

    def __str__(self):
        return self.reason

