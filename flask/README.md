# Flask Docker Architecture

This is the first approach in order to deploy the model into a container and expose an REST API to access the data. This architecture is not very scalabe but it was very useful to understand the basic structure of a ML application.

## Docker image

Into build folder there are the tools used to create a docker image. Copy the model generated into flask/build folder.

```bash
docker build -t flask-ml-docker build/
```

Run the API and bind it to host port 5000

```bash
docker run --name test-api -p 5000:5000 --rm flask-ml-docker
```

Make a query to the API

```bash
curl http://localhost:5000/predict \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"X": ['3.0', '1.0', '4.0','2.0', '0.0', '2', '0.0', '0.0', '1.0']}'
```

Push the image to a public repository

```bash
docker tag flask-ml-docker:latest natitomattis/flask-ml-docker
docker push natitomattis/flask-ml-docker
```

## K8s deployment

Into k8s folder there are the files that describe a simple deployment of the model, it requires the model docker image pulled into a public docker registry.

```bash
kubectl apply -f k8s
```
