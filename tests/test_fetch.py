from unittest.mock import patch
from src.fetch import fetch_title


@patch("src.fetch.requests.get")
def test_fetch_title(mock_get):
    mock_get.return_value.text = "Mocked HTML content here!"

    result = fetch_title("http://example.com")

    assert result == "Mocked HTML content "
    mock_get.assert_called_once_with("http://example.com")
