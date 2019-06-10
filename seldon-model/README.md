# Seldon Model Deployment

The first step is wrap your model into seldon framework, this is done by following [this documentation](https://docs.seldon.io/projects/seldon-core/en/latest/python/python_component.html). In this case, the file MLTitanic.py is the model.

## S2I

Source-to-Image (S2I) is a toolkit and workflow for building reproducible container images from source code. S2I produces ready-to-run images by injecting source code into a container image and letting the container prepare that source code for execution.

## Build the model

```bash
cd ..
s2i seldon-deploy seldonio/seldon-core-s2i-python3:0.4 natitomattis/seldon-ml-titanic
```

## Run the model locally

```bash
cd ..
docker run --name seldon-s2i-test -p 5000:5000 -d natitomattis/seldon-ml-titanic
```

## Test the model

### Via CURL

```bash
curl -g http://localhost:5000/predict  --data-urlencode 'json={"data": {"names": ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Cabin", "Lname", "NamePrefix" ],"ndarray": [['3', '1', '4', '2', '0', '2', '0', '0', '1']]}}'
```

### Via API contract

contract.json is a file that exposes the features of the model, seldon will take this description and will make request to the API

```bash
pipenv install --python 3.6 seldon-core
pipenv run seldon-core-tester contract.json localhost 5000 -p
```

## Publish the model

```bash
docker push natitomattis/seldon-ml-titanic
```
