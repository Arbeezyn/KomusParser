import requests
from bs4 import BeautifulSoup

cookies = {
    'cookiesession1': '678A3F62230CC2A10053F908EE520CD7',
    'dtCookie': 'v_4_srv_3_sn_825B2F843193030D879C5A331DC24201_perc_100000_ol_0_mul_1_app-3A40c41a8250581be2_1_rcs-3Acss_0',
    'JSESSIONID': '071ec936-48b7-4cd0-96a3-8bb8476b689b.hybris13p.komus.net',
    'USER_ID': '1079215126',
    'CURRENT_REGION': '1',
    'USER_ID': '1079215126',
    'CONFIRMED_REGION': '1',
    'qrator_ssid': '1696319248.585.TWfdGsKDd0OmSvj0-p68s1ocke1onsrvt8np0n4j7hflcr7f8',
    'qrator_jsid': '1702313494.606.4Nbwxn5OWxnTsaId-mcfa35u194tt8mrlulermts47vbco9bs',
}

headers = {
    'authority': 'www.komus.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # 'cookie': 'cookiesession1=678A3F62230CC2A10053F908EE520CD7; dtCookie=v_4_srv_3_sn_825B2F843193030D879C5A331DC24201_perc_100000_ol_0_mul_1_app-3A40c41a8250581be2_1_rcs-3Acss_0; JSESSIONID=071ec936-48b7-4cd0-96a3-8bb8476b689b.hybris13p.komus.net; USER_ID=1079215126; CURRENT_REGION=1; USER_ID=1079215126; CONFIRMED_REGION=1; qrator_ssid=1696319248.585.TWfdGsKDd0OmSvj0-p68s1ocke1onsrvt8np0n4j7hflcr7f8; qrator_jsid=1702313494.606.4Nbwxn5OWxnTsaId-mcfa35u194tt8mrlulermts47vbco9bs',
    'dnt': '1',
    'referer': 'https://www.komus.ru/?from=bread',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
}

params = {
    'from': 'menu-v1-vse_kategorii',
}


def getCategory(link):
    response = requests.get(
        f'{link}', params=params, cookies=cookies, headers=headers
    )
    soup = BeautifulSoup(response.text, 'html.parser')

    for categories__amount in soup.find_all(class_='categories__amount'):
        categories__amount.decompose()

    categories = soup.find_all(class_='categories__name')

    category_names = []
    category_links = []

    for category in categories:
        category_name = category.text.strip()
        category_link = "https://www.komus.ru/"+category.get('href')
        category_names.append(category_name)
        category_links.append(category_link)

    pure_links = []
    for link in category_links:
        response = requests.get(
            link,
            params=params,
            cookies=cookies, headers=headers
        )
        soup = BeautifulSoup(response.text, 'html.parser')

        if soup.find(class_='product-plain__name js-product-variant-name'):
            pure_links.append(link)
        if soup.find(class_='categories__name'):
            getCategory(link)

    return response.status_code, pure_links
