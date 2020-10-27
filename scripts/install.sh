#!/bin/bash

echo "performing: install" >> /tmp/custom.log

export FLASK_ENV=production

cd /srv/snakeoil

# Install python packages
pip3 install -r requirements.txt
pip3 install gunicorn
