#!/bin/bash

find ./static -mindepth 1 -not -name '.gitkeep'| xargs rm -rf
./manage.py collectstatic --noinput
./manage.py syncdb --noinput
