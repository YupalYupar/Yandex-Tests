import requests

YA_TOK = ''


def creat_folder(fr_name):
    headers = {'Authorization': 'OAuth' + YA_TOK}
    params = {'path': '/' + fr_name}
    url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
    resp = requests.put(url, headers=headers, params=params)
    return resp


def check_folder(fr_name):
    headers = {'Authorization': 'OAuth' + YA_TOK}
    params = {'path':'/' + fr_name}
    url = 'https://cloud-api.yandex.net:443/v1/disk/resources'
    res = requests.get(url, headers=headers, params=params)
    return res


if __name__ == '__main__':
    print(creat_folder('boogy'))
    print(check_folder('boogy'))
