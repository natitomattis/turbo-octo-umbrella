# Flask Docker Architecture

This is the first approach in order to deploy the model into a container and expose an REST API to access the data. This architecture is not very scalabe but it was very useful to understand the basic structure of a ML application.

## Docker image

Into build folder there are the tools used to create a docker image, python dependencies are managed by **Pipenv**.

## K8s deployment

Into k8s folder there are the files that describe a simple deployment of the model, it requires the model docker image pulled into a public docker registry.
