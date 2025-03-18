# msci-ip-task

1. Python Script (ip-tool.py)
The script should be able to:

- Report the configured IP networks.
- Check for collisions in IP ranges.
- Accept the --checkcollision argument.

2. Dockerfile

The Dockerfile will build an image to run the ip-tool.py script.

3. Kubernetes Deployment

kubectl apply -f ip-tool-deploy.yaml

4. Steps to Deploy
- Build the Docker Image:

docker build -t <your_docker_registry>/ip-tool:latest .

- Push the Image to a Registry:

Push the image to a Docker registry, such as Docker Hub or a private registry:

docker tag <your_docker_registry>/ip-tool:latest
docker login <your_docker_registry>
docker push <your_docker_registry>/ip-tool:latest

- Deploy on Kubernetes:

kubectl apply -f ip-tool-deploy.yaml

- Check the IP Networks and Collisions:

To report IP networks from a running container, you can exec into the pod:

kubectl exec -it <pod_name> -- python3 ip-tool.py --report

To check for collisions, first collect the IP networks from all containers, store them in a file, and use the --checkcollision flag:

kubectl exec -it <pod_name> -- python3 ip-tool.py --checkcollision /output/ip_networks.txt
