#!/bin/bash

supervisorctl reread
supervisorctl update
supervisorctl start all
service nginx start
