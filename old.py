import concurrent.futures

import requests

url = 'http://localhost:3000/users'


def get_page(page_number):
    response = requests.get(url, params={'page': page_number, })
    return response.json()


with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for i in range(100):
        futures.append(executor.submit(get_page, i))

    all_pages = []
    for future in concurrent.futures.as_completed(futures):
        all_pages.append(future.result())


# print(all_pages)
