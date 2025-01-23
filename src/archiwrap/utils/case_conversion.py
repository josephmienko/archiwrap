import re
from typing import Any, Dict, List, Union

def to_snake_case(s: str) -> str:
    """Convert a string to snake_case.
    
    Args:
        s: Input string in any case format
        
    Returns:
        String converted to snake_case
        
    Examples:
        >>> to_snake_case("mixedCASSE")
        'mixed_casse'
        >>> to_snake_case("UPPERCASE") 
        'uppercase'
    """    # Handle empty strings
    if not s:
        return s
        
    # First, handle special case of all uppercase
    if s.isupper():
        return s.lower()
    
    # Then handle regular camelCase/PascalCase conversion
    # This regex pattern matches:
    # 1. A lowercase letter followed by an uppercase letter
    # 2. A lowercase letter followed by multiple uppercase letters
    pattern = re.compile(r'([a-z])([A-Z])')
    result = pattern.sub(r'\1_\2', s)
    return result.lower()
def convert_keys_to_snake_case(obj: Union[Dict, List, Any]) -> Union[Dict, List, Any]:
    """Recursively convert dictionary keys from camelCase to snake_case."""
    if isinstance(obj, dict):
        return {to_snake_case(k): convert_keys_to_snake_case(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_keys_to_snake_case(item) for item in obj]
    return obj
