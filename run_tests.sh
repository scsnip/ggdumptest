#!/bin/bash

PYTHONPATH=`pwd`:`pwd`/tests:$PYTHONPATH
cd ./tests/
py.test -v ./*.py
exit $?
