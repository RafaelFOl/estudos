<p align="center">
<img src="https://user-images.githubusercontent.com/33993344/173132242-05da74c1-724b-4817-8d74-1a0d4967a974.png"
</p>  

 
# Jars necessarios
aws-java-sdk-174.jar
hadoop-aws-273.jar
delta-core_212-070.jar

# criar imagem docker
```
docker build . -t pathDockerHub/taxi-pipe:1.10
docker tag taxi-pipe:1.0 pathDockerHub/taxi-pipe:1.0
docker push pathDockerHub/taxi-pipe:1.0
```

# remover docker images
```
docker rmi $(docker images --filter "dangline=true" -q --no-trunc) -f
```
  

# conceder acesso em todo o cluster (CUIDADO)

```
kubectl create clusterrolebinding permissive-binding \
  --clusterrole=cluster-admin \
  --user=admin \
  --user=kubelet \
  --group=system:serviceaccounts
```
# Interargir com S3 local

necessario instalar o awscli
```
 aws s3api --endpoint-url="http://localhost:4566" list-buckets
```
# Install Jupyter
```
helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
helm repo update

helm install jupyterhub jupyterhub/jupyterhub -n notebook 
```
# Obter ip  Master K8S da porta 433
kubectl get service --all-namespaces

helm install engine spark-operator/spark-operator --namespace spark