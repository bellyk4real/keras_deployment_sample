#! python env
docker build -t kdeploy:1.0 .

#Now we will create a container by running this image
docker run -p 1234:1234 -t kdeploy:1.0

# push docker image to dockerhub
docker push kodumah/kdeploy:1.0

# Deploy the YAML File
$ kubectl create -f kodumah/kdeploy.yaml