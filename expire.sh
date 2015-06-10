#! /bin/bash
# Define a timestamp function
timestamp() {
  date +"%T"
}

curl -d "utterance=$(date)" localhost
