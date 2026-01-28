import pytest
from tools.extract import Extract
import pandas as pd


def test_extract():
    links = ["https://www.canadacomputers.com/en/powered-by-nvidia/268435/msi-geforce-rtx-5090-32g-ventus-3x-oc-rtx-5090-32g-ventus-3x-oc.html"]
    data = Extract(links)

    # Test if df atttibute for Extract object is a pandas DataFrame
    assert isinstance(data, pd.DataFrame)


if __name__ == "__main__":
    pass