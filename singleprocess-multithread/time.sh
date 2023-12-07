#!/bin/bash

time_exploits() {
    local option=$1
    local number=$2

    (time python3 ./thrower.py $number $option) 2>&1 | grep "real" | awk '{print $2}' | tr -d '\n'
}

exploit_options=("network" "crypto")
numbers=(10 100 500 1000)

printf "%-10s %-10s %-10s\n" "Option" "Number" "Time"

for option in "${exploit_options[@]}"; do
    for number in "${numbers[@]}"; do
        time=$(time_exploits $option $number)
        printf "%-10s %-10s %-10s\n" "$option" "$number" "$time"
    done
done
