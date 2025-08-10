mosquitto_sub -h 192.168.3.130 -u mqtt -P welkom -t "aircos/#" -v -W 2 | \
grep -o '^[^ ]*' | sort -u | \
while read topic; do
    echo "Clearing $topic"
    mosquitto_pub -h 192.168.3.130 -u mqtt -P welkom -t "$topic" -n -r
done
