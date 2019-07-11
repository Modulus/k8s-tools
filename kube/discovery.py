from kubernetes import client, config
import logging


logger = logging.getLogger("kube.svc")

def list_svc_by_labels(label_selector):
    """ List services in all namespaces by labels

    Parameters:

    label_selector (str): Comma separated string of labels with values

    Example:
    label_selector=\"kubernetes.io/name=monitoring-grafana,kubernetes.io/minikube-addons=heapster\"
    

    Returns:
    list: Of dictcs with matching services
    
    """
    logger.info("Initializing kubeconfig")

    config.load_kube_config()

    v1 = client.CoreV1Api()

    if label_selector:
        logger.info(f"Fetching all service with matching labels {label_selector}")
        result = v1.list_service_for_all_namespaces(label_selector=label_selector)

        logger.info(f"found: {result}")
    else:   
        logger.warning("Label selector is empty, returning all services")
        logger.info(f"Fetching all service with matching labels {label_selector}")
        result = v1.list_service_for_all_namespaces()

        logger.info(f"found: {result}")     

    return result




def list_ing_by_labels(label_selector) :
    """ List services in all namespaces by labels

    Parameters:

    lablabel_selectorels (str): Comma separated string of labels with values

    Example:
    label_selector=\"kubernetes.io/name=monitoring-grafana,kubernetes.io/minikube-addons=heapster\"
    

    Returns:
    list: Of dictcs with matching ingresses
    
    """
    config.load_kube_config()

    v1 = client.CoreV1Api()

    ext = client.ExtensionsV1beta1Api()

    if label_selector:
        response = ext.list_ingress_for_all_namespaces()
    else:
        response = ext.list_ingress_for_all_namespaces(label_selector=label_selector)

    return response        