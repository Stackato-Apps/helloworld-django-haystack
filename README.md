elasticsearch example
=====================

This is a sample Django application to demonstrate the [new
elasticsearch service](https://github.com/ActiveState/stackato-service-elasticsearch.git)
for Stackato v3.0.1.

# Deploying locally

    sudo apt-get install -y elasticsearch
    ./manage.py syncdb
    gem install foreman
    foreman start

# Deploying to Stackato

    stackato push -n
