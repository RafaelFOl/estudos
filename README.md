# estudos
#aws-java-sdk-174.jar
#hadoop-aws-273.jar
#delta-core_212-070.jar

docker build . -t taxi-pipe:1.0
docker tag taxi-pipe:1.0 senior2017/taxi-pipe:1.0
docker push senior2017/taxi-pipe:1.0

docker rmi $(docker images --filter "dangline=true" -q --no-trunc) -f
