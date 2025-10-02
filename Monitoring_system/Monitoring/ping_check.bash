#!/bin/bash
while true; do
    if ping -c 1 8.8.8.8 > /dev/null; then
        echo "$(date): Server OK"
    else
        echo "$(date): Server injoignable !" >> alert.log
    fi
    sleep 30
done