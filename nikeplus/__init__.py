import urllib
import urllib2
from cookielib import CookieJar
from xml.etree.ElementTree import ElementTree


class NikePlus(object):
    """
    Python wrapper for the unofficial Nike+ API.
    """
    def __init__(self, login=None, password=None, locale='en_us'):
        self.BASE_URL = 'https://secure-nikerunning.nike.com/nikeplus/v2/services/app/'
        self.opener = urllib2.build_opener()
        self.login = login
        self.password = password
        self.locale = locale

        cj = CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    def _request(self, path='', data=None, url=None):
        if not url: url = '%s%s' % (self.BASE_URL, path)
        if data: data = urllib.urlencode(data)
        req = urllib2.Request(url=url, data=data)
        return self.opener.open(req)

    def _valid_tree(self, raw):
        tree = ElementTree(file=raw)
        try:
            if tree.find('status').text == 'success':
                return tree
        except AttributeError:
            pass
        return False

    def authenticate(self):
        self.AUTHENTICATION_URL = 'https://secure-nikeplus.nike.com/services/profileService'
        kwargs = {
            'login': self.login,
            'password': self.password,
            'action': 'login',
            'locale': self.locale,
        }
        return self._valid_tree(self._request(url=self.AUTHENTICATION_URL, data=kwargs))

    def user_data(self):
        path = 'get_user_data.jsp'
        return self._valid_tree(self._request(path))

    def run_list(self):
        path = 'run_list.jsp'
        return self._valid_tree(self._request(path))

    def run(self, id):
        path = 'get_run.jsp'
        return self._valid_tree(self._request(path, {'id': id}))

    def challenge_list(self):
        path = 'get_challenges_for_user.jsp'
        return self._valid_tree(self._request(path))

    def challenge(self, id):
        path = 'get_challenge_detail.jsp'
        return self._valid_tree(self._request(path, {'id': id}))

    def goal_list(self):
        path = 'goal_list.jsp'
        return self._valid_tree(self._request(path))
