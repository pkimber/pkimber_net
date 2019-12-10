source venv-pkimber-net/bin/activate.fish
set -x KUBECONFIG (k3d get-kubeconfig)
set -x ALLOWED_HOSTS "abc,xyz"
set -x DATABASE_HOST (kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
set -x DATABASE_NAME "dev_www_pkimber_net_$USER"
set -x DATABASE_PASS "postgres"
set -x DATABASE_PORT (kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services kb-dev-db-postgresql)
set -x DATABASE_USER "postgres"
set -x DJANGO_SETTINGS_MODULE "settings.dev_$USER"
set -x DOMAIN "www.pkimber.net"
set -x MONITOR_DISABLE_SEND True
set -x MONITOR_SERVER_URL "http://monitor.kbsoftware.co.uk:8200"
set -x NORECAPTCHA_SECRET_KEY "your secret key"
set -x NORECAPTCHA_SITE_KEY "your site key"
set -x REDIS_HOST (kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
set -x REDIS_PORT (kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services kb-redis-master)
set -x SECRET_KEY "the_secret_key"
set -x SPARKPOST_API_KEY "your-api-key"
set -x USE_OPENID_CONNECT True
source .private
echo "KUBECONFIG:" $KUBECONFIG
echo "DATABASE_NAME:" $DATABASE_NAME
echo "DATABASE_HOST:" $DATABASE_HOST
echo "DATABASE_PORT:" $DATABASE_PORT
echo "REDIS_HOST:" $REDIS_HOST
echo "REDIS_PORT:" $REDIS_PORT
echo "USE_OPENID_CONNECT:" $USE_OPENID_CONNECT
