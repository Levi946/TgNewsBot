import requests

from exception import CantConnectToServer


def get_html_page(url: str) -> str:
    headers = _get_user_agent()
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.text
    raise CantConnectToServer


def _get_user_agent() -> dict[str, str]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 OPR/100.0.0.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
                  'application/signed-exchange;v=b3;q=0.9',
    }
    return headers


if __name__ == '__main__':
    print(get_html_page('https://ria.ru/export/rss2/archive/index.xml'))
