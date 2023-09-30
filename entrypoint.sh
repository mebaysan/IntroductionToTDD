#! /bin/bash

gunicorn 'main:create_app()' --bind 0.0.0.0:5000 -w 4