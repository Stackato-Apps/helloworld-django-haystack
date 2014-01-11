elasticsearch example
=====================

This is a sample Django application to demonstrate the [new
elasticsearch service](https://github.com/ActiveState/stackato-service-elasticsearch.git)
for Stackato v3.0.1. It uses [the haystack project](http://haystacksearch.org/)
for implementing a search backend.

# Deploying locally

    $ sudo apt-get install -y elasticsearch
    $ ./manage.py syncdb
    $ gem install foreman
    $ foreman start

# Deploying to Stackato

    $ stackato push -n

# Testing

After pushing the application to Stackato, run

    $ stackato run ./manage.py syncdb

Then go to /admin, log in with the administrative credentials and create some notes.
After you're done, go to /search and search to your heart's content.
