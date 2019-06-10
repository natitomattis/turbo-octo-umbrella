# ML Titanic Model Builder Image

## Create a docker image to train the model

```bash
docker build -t trainer .
```

## Train the model

```bash
cd ..
docker run -t -i -w /app -v "$(pwd)"/train:/app --rm trainer:latest python3 train.py
```

The model trained will be located into train/model folder, with the name *sk.pkl*

## Make a prediction

```bash
cd ..
docker run -t -i -w /app -v "$(pwd)"/train:/app --rm trainer:latest python3 predict.py
```
