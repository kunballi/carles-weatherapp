# Local Kubernetes Manifests

These manifests run the same app from `docker-compose.yml` inside Minikube.

The app images use Docker Hub names under the `kunballi` account:

- `kunballi/weather-ui`
- `kunballi/weather-auth`
- `kunballi/weather-service`

Secrets are synced from Vault by External Secrets Operator.

Before deploying, make sure ESO is installed and the Vault login secret exists
in the `weather-app` namespace. Do not commit real passwords to Git.

```powershell
kubectl create secret generic vault-userpass `
  -n weather-app `
  --from-literal=password=YOUR_VAULT_PASSWORD
```

ESO will use `secret-store.yaml` and `external-secret.yaml` to create the
runtime Kubernetes Secret named `app-secrets`.

Apply everything:

```powershell
kubectl apply -f k8s/
```

Open the UI locally:

```powershell
kubectl port-forward svc/ui -n weather-app 3000:3000
```

Then visit:

```text
http://localhost:3000
```
