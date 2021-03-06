#!/bin/bash
# usage: ./add_tags.sh <RPi IP address>
IP=$1
PORT=5000

curl --header "Content-Type: application/json" \
	 --request POST \
	 --data "{\"Tag\": \"165.177.144.27\", \"Name\": \"Michael Pocta\", \"Status\": \"0\"}" \
	 http://$IP:$PORT/add_user
echo ""

curl --header "Content-Type: application/json" \
	 --request POST \
	 --data "{\"Tag\": \"126.227.175.133\", \"Name\": \"David Toussaint\", \"Status\": \"0\"}" \
	 http://$IP:$PORT/add_user
echo ""