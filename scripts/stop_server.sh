#!/bin/bash

echo "performing: stop_server" >> /tmp/custom.log

supervisorctl stop all
service nginx stop
