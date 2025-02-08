# local-airflow
Deploying Apache Airflow using docker and kubernetes locally using **Docker-Desktop**

## 1. Environment :
- Windows 11
- WSL2 (https://learn.microsoft.com/en-us/windows/wsl/install)
- Docker-Desktop (https://www.docker.com/products/docker-desktop/)
- Helm Charts

## 2. How To :
### a. Installing Kubernetes :
1. Open your Docker-Desktop
2. Go to Setting(gear icon) and go to Kubernetes tab
3. Enable Kubernetes and wait until finish

### b. Check if Kubernetes installed properly :
1. Type ```kubectl version```
2. It will show
   ```
   Client Version: v1.31.4
   Kustomize Version: v5.4.2
   Server Version: v1.31.4
   ```
    
