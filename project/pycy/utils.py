import base64
from persistqueue import PDict


class BasicAuthMixin(object):
    class SendChallenge(Exception):
        pass

    def get_authenticated_user(self, check_credentials_func, realm):
        try:
            return self.authenticate_user(check_credentials_func, realm)
        except self.SendChallenge:
            self.send_auth_challenge(realm)

    def send_auth_challenge(self, realm):
        hdr = 'Basic realm="%s"' % realm.replace('\\', '\\\\').replace('"', '\\"')
        self.set_status(401)
        self.set_header('www-authenticate', hdr)
        self.finish()
        return False

    def authenticate_user(self, check_credentials_func, realm):
        auth_header = self.request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Basic '):
            raise self.SendChallenge()

        auth_data = auth_header.split(None, 1)[-1]
        auth_data = base64.b64decode(auth_data).decode('ascii')
        username, password = auth_data.split(':', 1)

        challenge = check_credentials_func(username)
        if not challenge:
            raise self.SendChallenge()

        if challenge == password:
            self._current_user = username
            return True
        else:
            raise self.SendChallenge()
        return False


class BasicCythonWrapper(object):
    def __init__(self, *args, **kwargs):
        self.qstore_path = kwargs.get('qstore_path', 'data')
        self.qstore_name = kwargs.get('qstore_name', 'qStore')

    def renew(self):
        self.handler = None
        self.init()

    def go_live(self):
        self.is_live = True
        q_store = PDict(self.qstore_path, self.qstore_name)
        q_store[self.q_prefix + 'is_live'] = True

    def go_fake(self):
        self.is_live = False
        q_store = PDict(self.qstore_path, self.qstore_name)
        q_store[self.q_prefix + 'is_live'] = False

    def start_loading(self):
        self.is_loading = True

    def end_loading(self):
        self.is_loading = False
