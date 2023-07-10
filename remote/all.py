from xmlrpc.server import SimpleXMLRPCServer
from kubernetes import client, config
import json
import ssl

file = "/home/review2/kube/config"
ca_cert = "/path/to/ca_cert.pem"

def get_pod_metrics_and_info():
    config.load_kube_config(file)
    client.Configuration.verify_ssl = True
    client.Configuration.ssl_ca_cert = ca_cert
    api = client.CustomObjectsApi()
    v1 = client.CoreV1Api()

    namespace = "bookman"
    plural = "pods"

    resource = api.list_namespaced_custom_object(
        group="metrics.k8s.io",
        version="v1beta1",
        namespace=namespace,
        plural=plural
    )

    pod_metrics = []
    for pod in resource["items"]:
        pod_name = pod["metadata"]["name"]
        cpu_usage = pod['containers'][0]["usage"]["cpu"].replace('n','')
        memory_usage = pod['containers'][0]["usage"]["memory"].replace('Ki','')
        pod_metrics.append([pod_name, cpu_usage, memory_usage, "Alive"])

    pod_info = []
    ret = v1.list_pod_for_all_namespaces(watch=False)
    for pod in ret.items:
        if 'replicas-deployment' in pod.metadata.name:
            pod_ip = pod.status.pod_ip
            pod_namespace = pod.metadata.namespace
            pod_name = pod.metadata.name
            pod_status = pod.status.phase
            pod_info.append({"pod_name": pod_name, "pod_ip": pod_ip, "namespace": pod_namespace, "status": pod_status})

    return {"pod_metrics": pod_metrics, "pod_info": pod_info}

def get_pod_metrics_and_info_json():
    result = get_pod_metrics_and_info()
    return json.dumps(result)

# SSL 証明書検証を無効化
ssl._create_default_https_context = ssl._create_unverified_context

with SimpleXMLRPCServer(('192.168.100.89', 8000)) as server:
    server.register_function(get_pod_metrics_and_info_json, "get_pod_metrics_and_info")
