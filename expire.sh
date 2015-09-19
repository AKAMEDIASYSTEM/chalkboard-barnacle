#! /bin/bash
# Define a timestamp function
timestamp() {
  date +"%T"
}

curl -d "utterance=$(timestamp)" http://0.0.0.0:8888
