from kubernetes import client, config
import logging
import utils.helpers as helpers

logger = logging.getLogger("kube.svc")

service_fields = ["name", "namespace", "hostname"]
ingress_fields = ["name", "namespace"]

def list_svc_by_labels(label_selector="", type="", filter=""):
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

    #return result
    return filter_data(filter=filter, data=result, fields=service_fields )


def list_ing_name_by_labels(label_selector="", filter="", fields="name"):
    metadata = list_ing_by_labels(label_selector=label_selector)

    return filter_data(filter=filter, data=metadata, fields=ingress_fields)
                

def filter_data(data=None, filter="", fields=None):
    result = []
    for item in data.items:
        if item.metadata and item.metadata.name:
            if filter == "" or filter == None:
                logger.debug("Appending without filter")
                values = {}
                if field == "hostname" :
                    value = item.status
                    values[field] = value
                else:
                    value = getattr(item.metadata, field)
                    values[field] = value
                result.append(values)
            else:
                logger.debug("Filtering list")
                filter_map = helpers.create_filter_dict(filter)
                valid_values = {}
                for key, value in filter_map.items():
                    logger.debug(f"Looking for key {key} containing value {value}")
                    a_value = getattr(item.metadata, f"{key}")
                    if value in a_value:
                        valid_values[key] = a_value
                if len(filter_map) == len(valid_values):
                    logger.info("Append valid values")
                    values = {}
                    for field in fields:
                        if field == "hostname" :
                            try:
                                value = (item.status.load_balancer.ingress[0]).hostname
                                values[field] = value
                            except TypeError as error:
                                logger.error(f"Failed to set value for hostname at {key}")
                        else:
                            value = getattr(item.metadata, field)
                            values[field] = value
                    result.append(values)

                else:
                    logger.debug(f"Failed to match element with key {key} and value {value}")

    return result


def list_ing_by_labels(label_selector="", filter="") :
    """ List services in all namespaces by labels

    Parameters:

    lablabel_selectorels (str): Comma separated string of labels with values

    Example:
    label_selector=\"kubernetes.io/name=monitoring-grafana,kubernetes.io/minikube-addons=heapster\"
    

    Returns:
    list: Of dictcs with matching ingresses
    
    """
    logger.info("Initializing kubeconfig")
    config.load_kube_config()
    ext = client.ExtensionsV1beta1Api()

    if label_selector:
        logger.info(f"Fetching all ingresses matching labels {label_selector}")
        response = ext.list_ingress_for_all_namespaces(label_selector=label_selector)
    else:
        logger.warning("Label selector is empty, returning all ingresses")
        response = ext.list_ingress_for_all_namespaces()
        logger.debug(f"Found: {response}")

    return response        