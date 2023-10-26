#!/bin/bash

start "" python3 server/main.py
sleep 1
start "" python3 client/main.py