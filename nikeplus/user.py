from xml.etree.ElementTree import ElementTree


class User(object):
    """User"""
    def __init__(self, etree=None):
        self.etree = etree

    @property
    def email(self):
        try:
            return self.etree.find('email').text
        except AttributeError:
            pass

    @property
    def gender(self):
        try:
            return self.etree.find('gender').text
        except AttributeError:
            pass
