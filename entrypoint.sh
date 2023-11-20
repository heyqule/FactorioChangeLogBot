while :
do
    python main.py
    sleep 900 &  # We sleep in the background to make the screipt interruptible via SIGTERM when running in docker
    wait $!
done