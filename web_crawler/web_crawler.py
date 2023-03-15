import time

import asyncio
import itertools
import sys
from typing import List
from urllib.parse import urljoin, urlparse, urlunparse


import httpx
from bs4 import BeautifulSoup

start = time.time()
class LinkQueue:
    def __init__(self):
        self.links = []

    def feed(self, token):
        if token.name == "a":
            href = token.get("href")
            if href is not None:
                self.links.append(href)


def get_links(base_url, page):
    domain_url = base_url._replace(path="", query=None)

    queue = LinkQueue()
    soup = BeautifulSoup(page, "html.parser")
    for link in soup.find_all("a"):
        queue.feed(link)

    links = []
    for link in queue.links:
        parsed_link = urlparse(link)
        if not parsed_link.scheme and not parsed_link.netloc:
            url = urljoin(base_url.geturl(), link)
            parsed_link = urlparse(url)
        if not parsed_link.scheme:
            parsed_link = parsed_link._replace(scheme=base_url.scheme)
        if not parsed_link.netloc:
            parsed_link = parsed_link._replace(netloc=base_url.netloc)
        if not parsed_link.path:
            parsed_link = parsed_link._replace(path="/")
        parsed_link = parsed_link._replace(fragment="")
        url = urlunparse(parsed_link)
        if url.startswith(domain_url.geturl()):
            links.append(url)
    return links


async def crawl(pages: List[str], current_depth: int, max_depth: int):
    print(f"Current Depth: {current_depth}, Max Depth: {max_depth}")
    if current_depth > max_depth:
        print("Reached Max Depth")
        return

    tasks = []
    async with httpx.AsyncClient(timeout=30.0) as client:
        for page in pages:
            print(f"getting: {page}")
            response = await client.get(page)
            body = response.content
            links = get_links(urlparse(page), body.decode())
            print(f"Following: {links}")
            tasks.append(crawl(links, current_depth + 1, max_depth))

    await asyncio.gather(*tasks)


async def main():
    if len(sys.argv) != 2:
        print("Usage: python program_name <url>")
        sys.exit(1)

    url = sys.argv[1]
    await crawl([url], 1, 2)


if __name__ == "__main__":
    asyncio.run(main())
end = time.time()

print("The time of execution of above program is :",
      (end-start) * 10**3, "ms")