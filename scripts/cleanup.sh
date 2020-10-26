#!/bin/bash

app_dir=/srv/snakeoil

rm -rf $app_dir
mkdir -p $app_dir
chown -R ubuntu: $app_dir
