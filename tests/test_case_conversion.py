import pytest
from archiwrap.utils.case_conversion import to_snake_case, convert_keys_to_snake_case

@pytest.mark.parametrize("input_str, expected", [
    ("camelCase", "camel_case"),
    ("PascalCase", "pascal_case"),
    ("snake_case", "snake_case"),
    ("UPPERCASE", "uppercase"),
    ("mixedCASSE", "mixed_casse"),
    ("", ""),  # Empty string
    ("already_snake", "already_snake"),
    ("multipleCAPS", "multiple_caps")
])
def test_to_snake_case(input_str: str, expected: str) -> None:
    """Test various string conversions to snake_case."""    
    assert to_snake_case(input_str) == expected

def test_convert_keys_complex_nested():
    """Test conversion of complex nested structures."""
    test_input = {
        "topLevel": {
            "nestedObject": {
                "deeplyNestedValue": 123
            },
            "arrayOfObjects": [
                {"itemOne": 1},
                {"itemTwo": 2}
            ],
            "mixedTypes": [
                {"nestedItem": "value"},
                123,
                "plainString",
                ["nestedArray"]
            ]
        }
    }
    
    expected = {
        "top_level": {
            "nested_object": {
                "deeply_nested_value": 123
            },
            "array_of_objects": [
                {"item_one": 1},
                {"item_two": 2}
            ],
            "mixed_types": [
                {"nested_item": "value"},
                123,
                "plainString",
                ["nestedArray"]
            ]
        }
    }
    
    result = convert_keys_to_snake_case(test_input)
    assert result == expected

def test_convert_keys_edge_cases():
    """Test edge cases for key conversion."""
    test_cases = [
        # Non-dict/list values should be returned as-is
        (123, 123),
        ("string", "string"),
        (None, None),
        # Empty containers should be handled properly
        ({}, {}),
        ([], []),
        # Mixed nested structures
        (
            ["string", {"camelCase": 123}, [{"nestedKey": "value"}]],
            ["string", {"camel_case": 123}, [{"nested_key": "value"}]]
        )
    ]
    
    for input_val, expected in test_cases:
        assert convert_keys_to_snake_case(input_val) == expected