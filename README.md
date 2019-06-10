# turbo-octo-umbrella

## Rappi Machine Learning Engineer Challenge

Repository organization:

* build: A Dockerfile that includes libraries that are used to train the model
* train: Training scripts and model serialization
* flask: Model Exposed via Flask API
* seldon-model: Seldon model image build process and tests scripts. Seldon core deployment porcess.
* seldon-helm-charts: Three example seldon deployments (single-model, ab-test and hpa-single model)
