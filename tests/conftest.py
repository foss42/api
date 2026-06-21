import pytest
from fastapi.testclient import TestClient

import sys
import os

# Add src to sys.path so we can import from it
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import app

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
