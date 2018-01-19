#!/bin/bash
#
# This bash script is the entrypoint for the docker image that runs Chrome (headless).
#
# It configures the container for WebDriver, and then starts the Python application.
#
source /opt/bin/functions.sh

export GEOMETRY="$SCREEN_WIDTH""x""$SCREEN_HEIGHT""x""$SCREEN_DEPTH"

function shutdown {
  kill -s SIGTERM $NODE_PID
  wait $NODE_PID
}

SERVERNUM=$(get_server_num)

rm -f /tmp/.X*lock

cd /opt/dynamicip/scraping-example
source .virtualenv/bin/activate

xvfb-run -n $SERVERNUM --server-args="-screen 0 $GEOMETRY -ac +extension RANDR" \
  python scraper.py &
NODE_PID=$!

trap shutdown SIGTERM SIGINT
wait $NODE_PID