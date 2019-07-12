import kube.discovery as svc
import kubernetes
import pytest


empty_data = [
    ("", ""),
    (None, "")
]


def test_list_ing_by_namels_and_filter_valid_filter():
    filter = "name:jenkins"

    result = svc.list_ing_name_by_labels(label_selector="", filter=filter)

    assert result != None
    assert type(result) == list
    assert len(result) > 0

    for element in result:
        assert "name" in element
        assert "jenkins" in element["name"]

def test_list_ingress_by_label_valid_label_selector():
    label_selector = "app=nginx-ingress"

    result = svc.list_ing_by_labels(label_selector=label_selector)

    assert result != None
   # assert result.items != None
    # assert "nginx-ingress" in result.items[0].metadata.name 
    #assert len(result.items) > 0    

def test_get_ingress_name_no_labels():
    result = svc.list_ing_name_by_labels()

    assert result != None

@pytest.mark.parametrize("value,expected", empty_data)
def test_list_ingress_by_label_invalid_label_selector(value, expected):


    result = svc.list_ing_by_labels(label_selector=value)

    assert result != None    
    #assert result.items != None
   # assert len(result.items) > 0