#!/bin/bash

chmod u+x "$1"
if [ $? -ne 0 ]; then
    exit 1
fi

pycodestyle "$1"
if [ $? -ne 0 ]; then
    exit 1
fi

mypy "$1"
if [ $? -ne 0 ]; then
    exit 1
fi

git add .
git commit -m "Task $1"
git push
