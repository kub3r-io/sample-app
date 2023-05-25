#!/bin/bash

action=$1

if [ $action == "login" ]
  then
  img "$@"
elif [ $action == "build" ]
  then
  img "$@"
elif [ $action == "push" ]
  then
  img "$@"
elif [ $action == "tag" ]
  then
  img "$@"
else
  echo "Sorry this docker method is not available!"
fi
