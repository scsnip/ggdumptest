#!/bin/bash

export PYTHONPATH=`pwd`:`pwd`/tests:$PYTHONPATH
echo $PYTHONPATH
cd ./tests/
py.test -v ./*.py
exit $?
