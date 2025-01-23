import pytest
from archiwrap.exceptions import ArchiWrapError

def test_archiwrap_error_basic():
    """Test basic error message handling."""
    error_msg = "Test error message"
    with pytest.raises(ArchiWrapError) as exc_info:
        raise ArchiWrapError(error_msg)
    assert str(exc_info.value) == error_msg

def test_archiwrap_error_with_response():
    """Test error handling with API response data."""
    error_data = {
        "status": 400,
        "message": "Bad Request",
        "details": "Invalid parameter value"
    }
    with pytest.raises(ArchiWrapError) as exc_info:
        raise ArchiWrapError("API Error", response_data=error_data)
    assert "API Error" in str(exc_info.value)
    assert hasattr(exc_info.value, "response_data")
