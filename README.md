01. Source code of app is ./src and this app listen on port 8080
02. Dockerfile to containerize above app is: ./Dockerfile and name Docker image after push to Docker hub: 081995/pythonapp:latest
03. Kubernetes manifests to deploy above app in: ./k8s. Those manifests create 2 pods and exposed TCP port 80
In case we would like to expose to the world wide with hostname http://abc.xyz, how to
do it ? => 
04. Jenkins is my choose.
Dev: 
    - Jenkinsfile: ./jenkins/jenkinsfile_dev.jenkinsfile
Stagging: 
    - Jenkinsfile: ./jenkins/jenkinsfile_stg.jenkinsfile
Production: 
    - Jenkinsfile: ./jenkins/jenkinsfile_prd.jenkinsfile