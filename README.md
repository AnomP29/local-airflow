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