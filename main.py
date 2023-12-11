import time
import os
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import re
import getCategory

from tkinter import *
from tkinter import ttk

import pandas as pd

import requests

cookies_one = {
    'cookiesession1': '678A3F62230CC2A10053F908EE520CD7',
    'dtCookie': 'v_4_srv_3_sn_825B2F843193030D879C5A331DC24201_perc_100000_ol_0_mul_1_app-3A40c41a8250581be2_1_rcs-3Acss_0',
    'USER_ID': '1079215126',
    'CURRENT_REGION': '1',
    'USER_ID': '1079215126',
    'CONFIRMED_REGION': '1',
    'JSESSIONID': '071ec936-48b7-4cd0-96a3-8bb8476b689b.hybris10p.komus.net',
    'qrator_ssid': '1696405245.663.R6Vhj7xKZzFD2iyw-lhrjkr2nd4f8ltpc4trm20ve6bmmjqdu',
    'qrator_jsid': '1702313494.606.4Nbwxn5OWxnTsaId-j0inkr92tmnbrrhejrt79j7sb0rai1k6',
}

headers_one = {
    'authority': 'www.komus.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'cookiesession1=678A3F62230CC2A10053F908EE520CD7; dtCookie=v_4_srv_3_sn_825B2F843193030D879C5A331DC24201_perc_100000_ol_0_mul_1_app-3A40c41a8250581be2_1_rcs-3Acss_0; USER_ID=1079215126; CURRENT_REGION=1; USER_ID=1079215126; CONFIRMED_REGION=1; JSESSIONID=071ec936-48b7-4cd0-96a3-8bb8476b689b.hybris10p.komus.net; qrator_ssid=1696405245.663.R6Vhj7xKZzFD2iyw-lhrjkr2nd4f8ltpc4trm20ve6bmmjqdu; qrator_jsid=1702313494.606.4Nbwxn5OWxnTsaId-j0inkr92tmnbrrhejrt79j7sb0rai1k6',
    'dnt': '1',
    'referer': 'https://www.komus.ru/katalog/kantstovary/prazdnichnaya-i-pozdravitelnaya-produktsiya/c/266/?listingMode=PLAIN&from=bread&page=1',
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

params_one = {
    'from': 'block-301-1_1',
}

cookies = {
    'cookiesession1': '678A3F62230CC2A10053F908EE520CD7',
    'dtCookie': 'v_4_srv_3_sn_825B2F843193030D879C5A331DC24201_perc_100000_ol_0_mul_1_app-3A40c41a8250581be2_1_rcs-3Acss_0',
    'USER_ID': '1079215126',
    'CURRENT_REGION': '1',
    'USER_ID': '1079215126',
    'CONFIRMED_REGION': '1',
    'JSESSIONID': '071ec936-48b7-4cd0-96a3-8bb8476b689b.hybris10p.komus.net',
    'qrator_ssid': '1696405245.663.R6Vhj7xKZzFD2iyw-lhrjkr2nd4f8ltpc4trm20ve6bmmjqdu',
    'qrator_jsid': '1702313494.606.4Nbwxn5OWxnTsaId-j0inkr92tmnbrrhejrt79j7sb0rai1k6',
}

headers = {
    'authority': 'www.komus.ru',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    # 'cookie': 'cookiesession1=678A3F62230CC2A10053F908EE520CD7; dtCookie=v_4_srv_3_sn_825B2F843193030D879C5A331DC24201_perc_100000_ol_0_mul_1_app-3A40c41a8250581be2_1_rcs-3Acss_0; USER_ID=1079215126; CURRENT_REGION=1; USER_ID=1079215126; CONFIRMED_REGION=1; JSESSIONID=071ec936-48b7-4cd0-96a3-8bb8476b689b.hybris10p.komus.net; qrator_ssid=1696405245.663.R6Vhj7xKZzFD2iyw-lhrjkr2nd4f8ltpc4trm20ve6bmmjqdu; qrator_jsid=1702313494.606.4Nbwxn5OWxnTsaId-j0inkr92tmnbrrhejrt79j7sb0rai1k6',
    'dnt': '1',
    'referer': 'https://www.komus.ru/katalog/kantstovary/prazdnichnaya-i-pozdravitelnaya-produktsiya/c/266/?from=bread',
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
    'listingMode': 'PLAIN',
    'from': 'bread',
    'page': '1',
}

root_folder = 'Канцтовары'


def getLinks(main_link):
    allLinks = []
    pages = requests.get(
        # f'https://www.komus.ru/katalog/ruchki-karandashi-markery/sharikovye-ruchki/c/6388/?listingMode=PLAIN&from'
        # f'=bread&page=0',
        main_link,
        params=params,
        cookies=cookies, headers=headers)
    soup = BeautifulSoup(pages.text, 'html.parser')
    if not soup.find_all(class_="pagination__item js-page-item"):
        lastPage = 1
    else:
        lastPage = soup.find_all(class_="pagination__item js-page-item")[-1].text
    for header_sup in soup.find_all(class_="catalog__header-sup"):
        header_sup.decompose()
    folder_name = soup.find(class_="catalog__header gtm-catalog-title").text.replace('\r\n',
                                                                                     '').strip()

    for i in range(0, int(lastPage)):

        response = requests.get(
            main_link[:-1] + str(i),
            params=params,
            cookies=cookies, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all(class_="product-plain__name js-product-variant-name")

        if links:
            for link in links:
                if link.get('href') in allLinks:
                    break
                allLinks.append('https://www.komus.ru' + link.get('href'))
    return allLinks, folder_name


def getItemInfo(link, folder_name):
    response = requests.get(
        link,
        params=params_one,
        cookies=cookies_one, headers=headers_one
    )
    soup = BeautifulSoup(response.text, 'html.parser')

    title_element = soup.find('h1')
    title = title_element.text if title_element else 'N/A'

    description_element = soup.find(class_="qa-description")
    description = description_element.text.replace(u'\xa0', ' ').replace('\r\n',
                                                                         '').strip() if description_element else 'N/A'

    vendor_element = soup.find(class_="qa-vendor-code")
    vendor = vendor_element.text if vendor_element else 'N/A'

    for popover_element in soup.find_all(class_='product-classification__popover'):
        popover_element.decompose()

    ul_elements = soup.find_all('ul', class_='product-classification')

    result_dict = {}

    for ul_element in ul_elements:
        li_elements = ul_element.find_all('li', class_='product-classification__row--align-start')

        for li_element in li_elements:
            feature = li_element.find('span', class_='product-classification__feature').text.strip().replace('\n',
                                                                                                             ' ').replace(
                u'\xa0', ' ').replace(':', '')
            values = li_element.find('span', class_='product-classification__values').text.strip().replace('\n',
                                                                                                           ' ').replace(
                u'\xa0', ' ').replace(':', '')

            feature = re.sub(' +', ' ', feature)
            values = re.sub(' +', ' ', values)

            result_dict[feature] = values

    images = soup.find_all(class_='product-media__representation-img js-img-gallery__view')
    i = 0
    for image in images:
        i += 1
        image_link = image.get('src')
        if image_link:
            image_response = requests.get(image_link)
            if image_response.status_code == 200:
                if not os.path.exists(f'{root_folder}/{folder_name}/{vendor}'):
                    os.makedirs(f'{root_folder}/{folder_name}/{vendor}')
                with open(f'{root_folder}/{folder_name}/{vendor}/{vendor}-{i}.jpg', 'wb') as f:
                    f.write(image_response.content)

    itemInfo = {
        'title': title,
        'description': description,
        'vendor': vendor,
        'item_info': result_dict
    }

    return itemInfo


main_link = input('Введите ссылку на каталог: ')

allLinks, folder_name = getLinks(main_link)
allItemInfo = []

for link in allLinks:
    allItemInfo.append(getItemInfo(link, folder_name))

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(allItemInfo)

# Save the DataFrame to an Excel file
df.to_excel(f'{root_folder}/{folder_name}/{folder_name}.xlsx', index=False)

window = Tk()
window.title(f"Классно!")
window.geometry("250x200")
window.attributes("-topmost", True)
label = ttk.Label(window, text=f"Страница {folder_name} загружена")
label.pack(anchor=CENTER, expand=1)
window.mainloop()
