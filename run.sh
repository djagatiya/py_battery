#!/bin/bash

# crontab config
# * * * * * sudo -u djagatiya /home/djagatiya/py_battery/run.sh

export DISPLAY=:1 
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
cd /home/djagatiya/py_battery
/home/djagatiya/miniconda3/envs/py_battery_env/bin/python run_single.py