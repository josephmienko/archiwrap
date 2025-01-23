from typing import Any, Dict, Optional
import requests
from .exceptions import ArchiWrapError
from .utils.case_conversion import convert_keys_to_snake_case

class ArchivesClient:
    def __init__(
        self,
        api_key: str,
        base_url: str = "https://catalog.archives.gov/api/v2"
    ):
        if not api_key:
            raise ArchiWrapError("API key is required for v2 API")
            
        self.api_key = api_key
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": "ArchiwrapClient/1.0",
            "x-api-key": api_key
        })

    def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        **kwargs
    ) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            # Set headers for JSON request
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": "ArchiwrapClient/1.0"
            }
            kwargs['headers'] = {**kwargs.get('headers', {}), **headers}
            
            response = self.session.request(method, url, params=params, **kwargs)
            
            # Check content type before attempting to parse JSON
            content_type = response.headers.get('content-type', '')
            if 'application/json' not in content_type:
                raise ArchiWrapError(
                    "API returned non-JSON response",
                    response_data={
                        "content_type": content_type,
                        "status_code": response.status_code,
                        "url": url
                    }
                )
                
            if response.status_code == 400:
                raise ArchiWrapError("Invalid parameter", response_data={"status_code": 400})
                
            response.raise_for_status()
            
            try:
                return convert_keys_to_snake_case(response.json())
            except (ValueError, requests.exceptions.JSONDecodeError) as e:
                raise ArchiWrapError(
                    "Invalid JSON response",
                    response_data={
                        "content_type": content_type,
                        "status_code": response.status_code,
                        "error": str(e),
                        "url": url
                    }
                )
                
        except requests.exceptions.RequestException as e:
            raise ArchiWrapError(f"Request failed: {str(e)}")

    def search(self, **kwargs) -> Dict[str, Any]:
        """
        Search the National Archives catalog.
        
        Args:
            **kwargs: Search parameters to pass to the API
            
        Returns:
            Dict[str, Any]: Search results
        """
        endpoint = "search"  # Match existing VCR cassettes
        return self._request("GET", endpoint, params=kwargs)
