"""
Export the biblipgraphy from Zotero and put into into thesis.bib
Script from https://github.com/Stadt-Geschichte-Basel/zotero-bib-to-gh/tree/master/.github/workflows
"""

FILE_NAME = 'thesis.bib'

import asyncio
from os import environ

import aiofiles
import httpx
import stamina
from logzero import logger


@stamina.retry(on=httpx.HTTPError, attempts=3)
async def fetch_url(client, url, headers):
    response = await client.get(url=url, headers=headers)
    response.raise_for_status()
    logger.info(f"{url} returned {response.status_code} after {response.elapsed}")
    return response


async def follow_and_extract(client, url, headers):
    request = await fetch_url(client, url, headers)
    try:
        next_url = request.links["next"].get("url")
        return request.text + await follow_and_extract(client, next_url, headers)
    except KeyError:
        return request.text


async def download_and_write_bib(
    client, zotero_headers, zotero_url, file_name=FILE_NAME
):
    zotero_connection = await fetch_url(client, zotero_url, zotero_headers)

    if zotero_connection.status_code == 403:
        logger.error("Access to library not granted.")
        return
    
    biblatex_file_content = await follow_and_extract(
        client, url=zotero_url, headers=zotero_headers
    )

    async with aiofiles.open(f"{file_name}", "w") as file:
        await file.write(biblatex_file_content)
        logger.info(f"{file_name} updated")


async def main():
    timeout = httpx.Timeout(10.0, connect=60.0)
    async with httpx.AsyncClient(timeout=timeout) as client:
        zotero_user_id = environ.get("ZOTERO_USER_ID")
        if zotero_user_id is None:
            logger.error("ZOTERO_USER_ID not set in GitHub secrets")
            return

        zotero_bearer_token = environ.get("ZOTERO_BEARER_TOKEN")
        if zotero_bearer_token is None:
            logger.error("ZOTERO_BEARER_TOKEN not set in GitHub secrets")
            return

        zotero_headers = {"Authorization": f"Bearer {zotero_bearer_token}"}
        zotero_user_url = (
            f"https://api.zotero.org/users/{zotero_user_id}/items?v=3&format=biblatex"
        )

        await download_and_write_bib(client, zotero_headers, zotero_user_url, file_name=FILE_NAME)


# Entry point for the script
if __name__ == "__main__":
    asyncio.run(main())