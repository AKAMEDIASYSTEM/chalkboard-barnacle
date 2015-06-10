#! /bin/bash
# Define a timestamp function
timestamp() {
  date +"%T"
}

curl -d "utterance= timestamp()" localhost
