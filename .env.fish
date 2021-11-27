source venv-pkimber-net/bin/activate.fish
if command -q k3d
  echo "Using Kubernetes"
  set -x KUBECONFIG (k3d get-kubeconfig)
  set -x DATABASE_HOST (kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  set -x DATABASE_PASS "postgres"
  set -x DATABASE_PORT (kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services kb-dev-db-postgresql)
  set -x REDIS_HOST (kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
  set -x REDIS_PORT (kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services kb-redis-master)
  echo "KUBECONFIG:" $KUBECONFIG
else
  set -x DATABASE_HOST ""
  set -x DATABASE_PASS ""
  set -x DATABASE_PORT ""
  set -x REDIS_HOST "localhost"
  set -x REDIS_PORT "6379"
end

set -x ALLOWED_HOSTS "abc,xyz"
set -x DATABASE_NAME "dev_www_pkimber_net_$USER"
set -x DJANGO_SETTINGS_MODULE "settings.dev_patrick"
set -x DOMAIN "www.pkimber.net"
set -x HOST_NAME "http://localhost:8000"
set -x LOG_FOLDER ""
set -x LOG_SUFFIX "dev"
set -x MONITOR_SERVER_URL "http://monitor.kbsoftware.co.uk:8200"
set -x NORECAPTCHA_SECRET_KEY "your secret key"
set -x NORECAPTCHA_SITE_KEY "your site key"
set -x SECRET_KEY "the_secret_key"
set -x SPARKPOST_API_KEY "your-api-key"
set -x USE_OPENID_CONNECT "False"

source .private

echo "DATABASE_NAME:" $DATABASE_NAME
echo "DATABASE_HOST:" $DATABASE_HOST
echo "DATABASE_PASS:" $DATABASE_PASS
echo "DATABASE_PORT:" $DATABASE_PORT
echo "DJANGO_SETTINGS_MODULE": $DJANGO_SETTINGS_MODULE
echo "REDIS_HOST:" $REDIS_HOST
echo "REDIS_PORT:" $REDIS_PORT
echo "USE_OPENID_CONNECT": $USE_OPENID_CONNECT
