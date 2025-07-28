"""
Customs Declaration Plugin Tests
"""
import os
import sys
import pytest

# Add the current directory to the path so we can import our modules
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from dify_integration import process_customs_declaration, dify_main


def test_process_customs_declaration_function_exists():
    """Test that the main function exists"""
    assert callable(process_customs_declaration)


def test_dify_main_function_exists():
    """Test that the Dify main function exists"""
    assert callable(dify_main)


# Additional tests would be added here to test the actual functionality
# For example, testing with sample Excel files, checking output formats, etc.

if __name__ == "__main__":
    pytest.main([__file__])
