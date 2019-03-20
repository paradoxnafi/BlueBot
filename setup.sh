#!/bin/sh

# Basic requirments
apt update
apt install python3 python3-dev python3-pip wget -y

# Talkey module for text to speech
pip3 install talkey speech_recognition

# Voice Engine
apt install festival pidgin-festival festival-freebsoft-utils -y
wget http://ftp.us.debian.org/debian/pool/main/f/festvox-us-slt-hts/festvox-us-slt-hts_0.2010.10.25-2_all.deb
dpkg -i festvox-us-slt-hts_0.2010.10.25-2_all.deb