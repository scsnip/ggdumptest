#!/bin/bash
# source venv enviroment first=)

export PYTHONPATH=`pwd`:`pwd`/tests:$PYTHONPATH
echo $PYTHONPATH
cd ./tests/
py.test -v ./*.py
exit $?
