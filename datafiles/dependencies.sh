#!/usr/bin/env bash

sudo apt-get update
# sudo apt-get install \
#     apt-transport-https \
#     ca-certificates \
#     curl \
#     gnupg-agent \
#     software-properties-common
#
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
# sudo apt-get update
# sudo apt-get install docker-ce docker-ce-cli containerd.io

# For skipping installation dialog
echo iptables-persistent iptables-persistent/autosave_v4 boolean true | sudo debconf-set-selections
echo iptables-persistent iptables-persistent/autosave_v6 boolean true | sudo debconf-set-selections
sudo apt install iptables-persistent -y


while ! (ps -ef | grep "[d]ocker" | awk {'print $2'});
do
  echo "Waiting for docker daemon file..."
  sleep 5
done
