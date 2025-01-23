import pytest
import vcr
from archiwrap import ArchivesClient

@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": ["authorization"],
        "record_mode": "once",
        "cassette_library_dir": "tests/fixtures/cassettes"
    }

@pytest.fixture
def client():
    """Provide a test client instance."""
    return ArchivesClient()

@pytest.fixture
def authenticated_client():
    """Provide an authenticated test client instance."""
    return ArchivesClient(api_key="test_key")
