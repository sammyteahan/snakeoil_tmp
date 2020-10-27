#!/bin/bash

app_dir=/srv/snakeoil

echo "performing: cleanup" >> /tmp/custom.log

rm -rf $app_dir
mkdir -p $app_dir
chown -R ubuntu: $app_dir
