#!/bin/bash
while :
do
    sleep 7200 &  # We sleep in the background to make the script interruptable via SIGTERM when running in docker
    wait $!
    python -u main.py
done