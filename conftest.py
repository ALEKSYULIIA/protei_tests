import pytest
from function_project import Nominatim

@pytest.fixture(scope="module")
def geo():
   return Nominatim()