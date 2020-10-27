#!/bin/bash

echo "performing: start_server" >> /tmp/custom.log

supervisorctl reread
supervisorctl update
supervisorctl start all
service nginx start
