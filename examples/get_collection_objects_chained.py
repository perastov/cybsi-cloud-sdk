#!/usr/bin/env python3
import os

from cybsi.cloud import Client, Config
from cybsi.cloud.pagination import chain_pages

if __name__ == "__main__":
    api_url = os.environ.get("CLOUD_BASE_URL", "https://cybsi.cloud")
    api_key = os.environ.get("CLOUD_API_KEY", "api_key")
    config = Config(api_url, api_key)

    with Client(config) as client:
        collection_id = "example-collection"
        start_page, _ = client.iocean.objects.filter(
            collection_id=collection_id,
        )
        for item in chain_pages(start_page):
            # Do something with an item
            pass