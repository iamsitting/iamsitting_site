# Setup

## Certificate

First, get a certificate. I like the certbot letsencryot combo.
Let's install certbot.

```
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python-certbot-nginx 
```

## Nginx Configuration

First let's add a couple lines to iamsittingsite nginx conf file.
```
# /etc/nginx/sites-available/site_config (or /etc/nginx/conf.d)

location /.well-known {
    root /path/to/project_root; #BASE_DIR of Django project
}
```

Now, let's run the certbot command
```
sudo certbot --authenticator webroot --installer nginx
# provide email
# choose correct domain
# provide webroot (the path under .well-known above)
```

Now, these lines should've have been added to you nginx conf file:
```
listen 443 ssl; # managed by Certbot
ssl_certificate /path/to/fullchain.pem; # managed by Certbot
ssl_certificate_key /path/to/privkey.pem; # managed by Certbot
include /path/to/options-ssl-nginx.conf; # managed by Certbot
ssl_dhparam /path/ssl-dhparams.pem; # managed by Certbot

if ($scheme != "https") {
        return 301 https://$host$request_uri;
    } # managed by Certbot

```


## AWS Configuration

Notice, that we are now listening on port 443.
So we need to add this port to the security group on AWS.
Go to AWS Console > Instance > Security group > Add Rule > HTTPS

## Django Configuration

Now let's add a few lines to the Django settings file.
```
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
SECURE_SSL_REDIRECT = True
```

Lastly, run the certbot dry-run renewal code:
```
sudo certbot renew --dry-run
```

Now the site is secured!
