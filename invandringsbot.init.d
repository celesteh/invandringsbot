#!/bin/sh
### BEGIN INIT INFO
# Provides:          invandringsbot
# Required-Start:    $local_fs
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start/stop invandringsbot
### END INIT INFO

# Set the USER variable to the name of the user to start tightvncserver under
export USER='pi'

eval cd /home/pi/Code/invandringsbot/

case "$1" in
  start)
    sleep 180
    su $USER -c '/usr/bin/python /home/pi/Code/invandringsbot/mainbot.py &'
    echo "Starting invandringsbot"
    ;;
  stop)
    pkill invandringsbot
    echo "invandringsbot stopped"
    ;;
  *)
    echo "Usage: /etc/init.d/BlockAllTwerps {start|stop}"
    exit 1
    ;;
esac
exit 0
