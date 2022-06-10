![image](https://user-images.githubusercontent.com/33993344/173132242-05da74c1-724b-4817-8d74-1a0d4967a974.png)




# estudos
#aws-java-sdk-174.jar
#hadoop-aws-273.jar
#delta-core_212-070.jar

docker build . -t senior2017/taxi-pipe:1.9
docker tag taxi-pipe:1.0 senior2017/taxi-pipe:1.0
docker push senior2017/taxi-pipe:1.0

docker rmi $(docker images --filter "dangline=true" -q --no-trunc) -f

kubectl get all -n spark



kubectl create clusterrolebinding permissive-binding \
  --clusterrole=cluster-admin \
  --user=admin \
  --user=kubelet \
  --group=system:serviceaccounts
