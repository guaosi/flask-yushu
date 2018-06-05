import requests
class HTTP():
    @staticmethod
    def get(url,return_json=True):
        r=requests.get(url)
        if r.status_code==200:
            # 这里的json()转的是dict
            return r.json() if return_json else r.text
        return {} if return_json else ''