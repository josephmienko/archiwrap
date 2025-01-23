from typing import Any, Dict

class ArchiWrapError(Exception):
    """Base exception for all archiwrap errors."""
    
    def __init__(self, message: str, response_data: Dict[str, Any] = None):
        super().__init__(message)
        self.response_data = response_data
        
    def __str__(self):
        if self.response_data:
            return f"{super().__str__()} - {self.response_data}"
        return super().__str__()
