import kube.discovery as svc
import kubernetes

def test_list_service_by_label_valid_label_selector():
    label_selector = "component=apiserver,provider=kubernetes"

    result = svc.list_svc_by_labels(label_selector=label_selector)

    assert result != None
    assert type(result) == kubernetes.client.models.v1_service_list.V1ServiceList

def test_list_service_by_label_empty_label_selector():
    label_selector = ""

    
    result = svc.list_svc_by_labels(label_selector=label_selector)

    assert result != None
    assert type(result) == kubernetes.client.models.v1_service_list.V1ServiceList