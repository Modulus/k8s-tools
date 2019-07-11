import pytest
from utils import helpers

def test_extract_zone_id():
	id = "Z2FIOTQIPYWL1"
	zone_id = f"/hostedzone/{id}"
	
	result = helpers.extract_zone_id(id=zone_id)
	assert result != None
	assert result == id

