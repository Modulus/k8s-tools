import kube.discovery as svc
import kubernetes
import pytest


empty_data = [
    ("", ""),
    (None, "")
]

def test_list_ingress_by_label_valid_label_selector():
    label_selector = "app=nginx"

    result = svc.list_ing_by_labels(label_selector=label_selector)

    assert result != None

@pytest.mark.parametrize("value, expected", empty_data)
def test_list_ingress_by_label_invalid_label_selector(value, expected):


    result = svc.list_ing_by_labels(label_selector=value)

    assert result != None    