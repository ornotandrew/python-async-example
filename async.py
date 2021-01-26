import asyncio  # python standard lib

import aiohttp  # new-age version of "requests"

url = 'http://localhost:3000/users'


async def get_page(client, page_number):
    response = await client.get(url, params={'page': page_number})
    return await response.json()


async def get_all_pages():
    async with aiohttp.ClientSession() as client:
        return await asyncio.gather(*[get_page(client, i + 1) for i in range(100)])

# Create an event loop and run our code on it
all_pages = asyncio.run(get_all_pages())
# print(all_pages)
