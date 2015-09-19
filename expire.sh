#! /bin/bash
# Define a timestamp function
timestamp() {
  date +"%T"
}

curl -d "utterance=$(timestamp)" http://0.0.0.0
# USE THE FOLLOWING LINE FOR SPECIAL PORTS
# curl -d "utterance=$(timestamp)" http://0.0.0.0:8888
