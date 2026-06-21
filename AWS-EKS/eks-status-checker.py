# Queries and shows the statuses of EKS clusters.

import boto3

client = boto3.client('eks')
clusters = client.list_clusters()['clusters']

for cluster in clusters:
    print(f"ClusterName: {cluster}")

    response = client.describe_cluster(name=cluster)

    cluster_info = response['cluster']
    cluster_status = cluster_info['status']
    cluster_endpoint = cluster_info['endpoint']
    cluster_version = cluster_info['version']

    print(f"ClusterStatus: {cluster_status}")
    print(f"ClusterEndpoint: {cluster_endpoint}")
    print(f"ClusterVersion: {cluster_version}")

    print("###################################################")
