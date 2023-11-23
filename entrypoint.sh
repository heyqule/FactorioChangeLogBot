#!/bin/bash
while :
do
    sleep 24*60*60 &  # We sleep in the background to make the script interruptable via SIGTERM when running in docker
    wait $!
    python main.py
done