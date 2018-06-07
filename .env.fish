source venv-pkimber-net/bin/activate.fish
set -x ALLOWED_HOSTS "abc,xyz"
set -x DJANGO_SETTINGS_MODULE "settings.dev_patrick"
set -x DOMAIN "www.pkimber.net"
set -x MONITOR_SERVER_URL "http://monitor.kbsoftware.co.uk:8200"
set -x NORECAPTCHA_SECRET_KEY "your secret key"
set -x NORECAPTCHA_SITE_KEY "your site key"
set -x SECRET_KEY "the_secret_key"
set -x SPARKPOST_API_KEY "your-api-key"
source .private
