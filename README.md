01. Source code of app is ./src and this app listen on port 8080
02. Dockerfile to containerize above app is: ./Dockerfile and name Docker image after push to Docker hub: 081995/pythonapp:latest
03. Kubernetes manifests to deploy above app in: ./k8s. Those manifests create 2 pods and exposed TCP port 80 
    In case we would like to expose to the world wide with hostname http://abc.xyz, how to
    do it ? 
    => Use Kubernetes Ingress. I will create a Ingress with the Endpoint is service (svc1) and buy a domain for master node with cloud or add the host with on-premise system
    Manifests Ingress like below: 
    ```
    apiVersion: extensions/v1beta1
    kind: Ingress
    metadata:
    name: app
    namespace: default
    spec:
    rules:
        # custom domain name
    - host: pythonapp.test
        http:
        paths:
        - path: /
            backend:
            serviceName: http-test-svc
            servicePort: 80
    ```

04. Jenkins is my choice.
Dev: 
    - Jenkinsfile: ./jenkins/jenkinsfile_dev.jenkinsfile
    - Configuration: This Jenkins job will point to "develop" branch. This job is started daily or any new commit to "develop" branch. If everything test is OK, develop branch will create a merge request to merge  to "release" branch.
Stagging: 
    - Jenkinsfile: ./jenkins/jenkinsfile_stg.jenkinsfile
    - Configuration: This Jenkins job will point to "release" branch. This job is started by manual. If everything test is OK, release branch will create a merge request to merge to "master" branch.
Production: 
    - Jenkinsfile: ./jenkins/jenkinsfile_prd.jenkinsfile
    - Configuration: This Jenkins job will point to "master" branch. This job is started by manual

05. 
For the resource of K8s cluster: Resources are a key ingredient that can greatly affect response times. If do not enough resource, response times will be high or maybe application is stuck.
    - Inorder to monitor the resource of K8s cluster: I think we can you Prometheus and Grafana to monitor.
        * The Prometheus will collect the metrics and Grafana will show it with graph format.
    - Performance of Application: I think we can use Datadog.
        * Datadog enables you to analyze and isolate dependencies, remove bottlenecks, reduce latency, track errors, and increase code efficiency to optimize your application.
    - Log monitor: I think we can use Graylog
        * Graylog is an open-source and free log file-based system having a graphical user interface. It includes a query and search function that allows you to filter log records according to your convenience. This application includes a dashboard to see the detailed record.