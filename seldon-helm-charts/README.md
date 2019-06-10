# Seldon Deployment via Helm Charts

## Set Up the cluster

Grant a cluster-wide super-user role to our user, using Role-Based Access Control (RBAC). On GCP this is achieved with:

```bash
kubectl create clusterrolebinding kube-system-cluster-admin \
    --clusterrole cluster-admin \
    --serviceaccount kube-system:default \
    --user $(gcloud info --format="value(config.account)")
```

Create namespace seldon

```bash
kubectl create namespace seldon
kubectl config set-context $(kubectl config current-context) --namespace=seldon
```

Install helm locally and tiller

```bash 
sudo snap install helm --classic
kubectl --namespace kube-system create serviceaccount tiller
kubectl create clusterrolebinding tiller \
    --clusterrole cluster-admin \
    --serviceaccount=kube-system:tiller
helm init --service-account tiller
```

## Deploy Seldon Core

Clone seldon core repository, and cd into the root folder. Deploy seldon core-operator

```bash
helm install ./helm-charts/seldon-core-operator/ \
              --name seldon-core \
              --set usageMetrics.enabled=true \
              --namespace seldon-system
```

Deploy ambassador as Ingress

```bash
helm install stable/ambassador \
             --name ambassador \
             --set crds.keep=false
```

## Deploy Seldon Analytics

Use seldon analytics helm chart in order to deploy analytics service

```bash
helm install ./helm-charts/seldon-core-analytics \
              --name seldon-core-analytics \
              --set grafana_prom_admin_password=password \
              --set persistence.enabled=false \
              --repo https://storage.googleapis.com/seldon-charts\
              --namespace seldon
```

Forward the ports:

```bash
kubectl port-forward $(kubectl get pods -n seldon -l app=grafana-prom-server -o jsonpath='{.items[0].metadata.name}') -n seldon 3000:3000
```

Open http://localhost:3000 to log into Grafana using your set password.

## Deploy Single Model

Create a release of the deployment

```bash
helm repo add seldon-repo https://storage.googleapis.com/seldon-charts
helm dependencies update ./single-model
helm install --name my-release ./single-model
```

### Test via CURL

Get ambassador IP

```bash
kubectl get svc
```

```bash
curl http://[AMBASSDOR_IP]/seldon/seldon/my-release/api/v0.1/predictions \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"data": {"ndarray": [['3', '1', '4', '2', '0', '2', '0', '0', '1']]}}'
```

### Test via Contract

In order to make queries to the api, we will use seldon-core-api-tester that is a library created by seldon which receives the following arguments

* --ambassador-path: the path where the API is exposed (/seldon/[seldonDeployment])
* -n N_REQUESTS
* -p print request and response

```bash
pipenv install --python 3.6 seldon-core
pipenv run seldon-core-api-tester -n 1 -p --ambassador-path /seldon/seldon/nati contract.json 35.199.112.111 80
```
