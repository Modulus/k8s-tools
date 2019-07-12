import pytest
from utils import helpers

def test_extract_zone_id():
	id = "Z2FIOTQIPYWL1"
	zone_id = f"/hostedzone/{id}"
	
	result = helpers.extract_zone_id(id=zone_id)
	assert result != None
	assert result == id

def test_create_filter_dict_simple_filter_works():
	filter = "name:jenkins"

	filter_map = helpers.create_filter_dict(filter)

	assert filter_map != None
	assert type(filter_map) == dict
	assert len(filter_map) == 1
	assert "name" in filter_map
	assert filter_map["name"] == "jenkins"



def test_create_filter_dict_complex_filter_works():
	filter = "name:jenkins;ingress-controller:nginx"

	result = helpers.create_filter_dict(filter)

	assert type(result) == dict
	assert len(result) == 2
	assert result["name"] == "jenkins"

	assert result["ingress-controller"] == "nginx"

def test_create_fitler_dict_multiple_values_works():
	filter="foo:bar;ingress:nginx;food:burger;person:leeroy"

	result = helpers.create_filter_dict(filter)

	assert type(result) == dict
	assert len(result) == 4
	assert result["foo"] == "bar"
	assert result["ingress"] == "nginx"
	assert result["food"] == "burger"
	assert result["person"] == "leeroy"

empty_data = [
    ("", None),
    (None, None)
]

@pytest.mark.parametrize("value,expected", empty_data)
def test_filter_helper_no_filter(value, expected):
	filter_map = helpers.create_filter_dict(value)

	assert filter_map == expected