import sys
import requests
import pytest

def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    assert version_info.minor == 8

def python_version():
    return sys.version_info

def requests_version():
    return requests.__version__

def pytest_version():
    return pytest.__version__
