# local-airflow
Deploying Apache Airflow using docker and kubernetes locally using **Docker-Desktop**

## 1. Environment :
- Windows 11
- [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) 
- [Docker-Desktop](https://www.docker.com/products/docker-desktop/) 
- Helm Charts
- [Lens](https://k8slens.dev/) 

## 2. How To :
### a. Installing Kubernetes :
1. Open your Docker-Desktop
2. Go to Setting(gear icon) and go to Kubernetes tab
3. Enable Kubernetes and wait until finish
4. Check if Kubernetes installed properly :
   - Type
     ```
     kubectl version
     ```
   - It will show
      ```
      Client Version: v1.31.4
      Kustomize Version: v5.4.2
      Server Version: v1.31.4
      ```
### b. Installing Helm Chart :
You can read it [here](https://helm.sh/docs/intro/install/)
```
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```
1. Check if helm already installed : `helm version`
It will show you `version.BuildInfo{Version:"v3.17.0", GitCommit:"301108edc7ac2a8ba79e4ebf5701b0b6ce6a31e4", GitTreeState:"clean", GoVersion:"go1.23.4"}`
### c. Installing Lens :
You can install from the link above.
#### How to use Lens
1. Open Lens
2. Add KubeConfigs

![alt text](https://github.com/AnomP29/local-airflow/blob/main/pic/Screenshot%202025-02-08%20185452.png)

3. Choose `config` File in `C:\Users\{your_user_name}\.kube`
4. Your lens SideBar will show new option

![alt text](https://github.com/AnomP29/local-airflow/blob/main/pic/Screenshot%202025-02-08%20190001.png)

### d. Installing/Deploying Airflow HelmCharts PODS:
1. Add airflow to the local Helm repository
`helm repo add apache-airflow https://airflow.apache.org`
2. Update Helm repository to ensure it is up to date after adding airflow
`helm repo update`
3. Install the airflow into a Kubernetes pod
`helm install airflow apache-airflow/airflow --namespace airflow --create-namespace --debug`
Notes : the namespace 'airflow' you can change based on your own will
4. Wait until installation is finished, then open Lens. 
Expand `docker-desktop -> Workloads` and click overview
Don't forget to choose `namespace`

![alt text](https://github.com/AnomP29/local-airflow/blob/main/pic/Screenshot%202025-02-08%20191113.png)

All Pods should Running, mark with green 

**NOW YOUR AIRFLOW READY IS TO USE**

But Before you can open `Airflow Webserver` you need to forwarding Port. Here is the code is : \
`kubectlport-forward svc/airflow-webserver 8080:8080 --namespace local-airflow` \

Open your Local browser and go to this address : \
`http://localhost:8080/` \
![alt text](https://github.com/AnomP29/local-airflow/blob/main/pic/Screenshot%202025-02-08%20191853.png)

