#!/bin/bash

run_job() {
    local input_number=$1
    local output_file="output_${input_number}.txt"
    ./hello_world "$input_number" > "$output_file"
}

export -f run_job

parallel --jobs 10 run_job ::: {0..9}