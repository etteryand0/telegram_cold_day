import requests

class Bot:
    def __init__(self, token, admin, chat_id):
        self.token = (token,)
        self.admin = (admin,)
        self.chat_id = (chat_id,)


    def send_msg(self, text):
        traceback = self._send_request(self.chat_id, text)

        return traceback

    
    def debug_error(self, e):
        traceback = self._send_request(self.admin, e)

        return traceback


    def _send_request(self, chat_id, text):
        uri = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=Markdown'.format(
                self.token[0],
                chat_id[0],
                text)

        try:
            req = requests.get(uri.replace(' ', '+'))
        except requests.exceptions.ConnectionError as e:
            return e
        
        return req.status_code