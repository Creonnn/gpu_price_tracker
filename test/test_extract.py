import pytest
from tools.extract import Extract
from tools.scraper import get_5090_memexp_ids
import pandas as pd
import asyncio

def test_get_5090_memexp_ids():
    base_url = "https://www.memoryexpress.com"
    path = "/Category/VideoCards"
    filter_id = "FilterID=825f91ad-c322-6b30-5411-a027616f0c32"
    paths = asyncio.run(get_5090_memexp_ids(base_url, path, filter_id))
    # Return object is a list
    assert isinstance(paths, list)
    # Objects in the list are strings
    assert all([isinstance(id, str) for id in paths])

def test_extract():
    pass


if __name__ == "__main__":
    pass