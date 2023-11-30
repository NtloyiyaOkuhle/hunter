import requests
import time
import asyncio
import aiohttp
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def outer_func(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')
    return inner_function

GREEN = outer_func('\033[92m')
YELLOW = outer_func('\033[93m')
RED = outer_func('\033[91m')

def confirm_authorization():
    while True:
        auth = input('\033[93m[WARNING] This tool is intended for ethical purposes only. Are you authorized to perform this test? (yes/no): ').lower()
        if auth == 'yes':
            return True
        elif auth == 'no':
            logger.error('[!] Unauthorized access. Exiting...')
            return False
        else:
            logger.warning('Please type "yes" if you are authorized or "no" to exit.')

def read_websites():
    with open('websites.txt', 'r') as file:
        websites = file.read().splitlines()
    return websites

async def fetch(session, url, username):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.text()
                if username in data:
                    logger.info(f"POSITIVE MATCH: Username '{username}' detected in URL: {url}")
                else:
                    logger.info(f"POSITIVE MATCH: Username '{username}' not detected in URL: {url}, could be a FALSE POSITIVE.")
    except aiohttp.ClientError as e:
        logger.error(f"Error accessing {url}: {str(e)}")

async def search_async(username, websites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in websites:
            try:
                formatted_url = url.replace('{username}', username)
                task = fetch(session, formatted_url, username)
                tasks.append(task)
            except ValueError:
                logger.error(f"Invalid URL: {url}")
        
        await asyncio.gather(*tasks)

def search(username, websites):
    logger.info(f"[+] Searching for username: {username}")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(search_async(username, websites))
    loop.close()

if __name__ == '__main__':
    authorized = confirm_authorization()
    if authorized:
        username = input('\033[92m{+} Enter username to DOX: ')
        website_urls = read_websites()
        search(username, website_urls)