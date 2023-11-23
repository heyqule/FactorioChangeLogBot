#!/bin/bash
while :
do
    sleep 21600 &  # We sleep in the background to make the script interruptable via SIGTERM when running in docker
    wait $!
    python main.py
done