import requests

YA_TOK = ''


def create_folder(fr_name):
    headers = {'Authorization': 'OAuth ' + YA_TOK}
    params = {'path': '/' + fr_name}
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    resp = requests.put(url, params=params, headers=headers)
    return resp


def check_folder(fr_name):
    headers = {'Authorization': 'OAuth ' + YA_TOK}
    params = {'path': '/' + fr_name}
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    resp = requests.get(url, params=params, headers=headers)
    return resp


if __name__ == '__main__':
    print(create_folder('boogy'))
    print(check_folder('boogy'))
