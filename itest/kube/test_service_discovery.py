import kube.discovery as svc
import kubernetes
def test_list_service_by_label_valid_label_selector_and_filter():
    filter = "name:nginx"
    result = svc.list_svc_by_labels(label_selector=None, filter=filter)

    assert result != None
    assert result.items != None
    assert len(result.items) > 0

    assert result.items[0].metadata.name == "kubernetes"
    

def test_list_service_by_label_valid_label_selector():
    label_selector = "component=apiserver,provider=kubernetes"

    result = svc.list_svc_by_labels(label_selector=label_selector)

    assert result != None
    assert result.items != None
    assert len(result.items) > 0

    assert result.items[0].metadata.name == "kubernetes"
    

def test_list_service_by_label_empty_label_selector():
    label_selector = ""

    
    result = svc.list_svc_by_labels(label_selector=label_selector)

    assert result != None
    assert result.items != None
    assert len(result.items) > 0