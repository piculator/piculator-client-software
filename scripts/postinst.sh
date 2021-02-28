#!/bin/sh
set -e
case "$1" in
    install)
        echo "@piculator-client" >> /etc/xdg/lxsession/LXDE-pi/autostart
        ;;

    upgrade|abort-upgrade)
        ;;

    *)
        echo "postinst called with unknown argument \`$1'" >&2
        exit 0
        ;;
esac
