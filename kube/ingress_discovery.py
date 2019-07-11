from kubernetes import client, config

config.load_kube_config()

v1 = client.CoreV1Api()

ext = client.ExtensionsV1beta1Api()

response = ext.list_ingress_for_all_namespaces()

print(response)

def list_ing_by_labels(label_selector)