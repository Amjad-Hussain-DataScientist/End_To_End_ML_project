#!/bin/bash
if [ ! -f /var/swapfile ]; then
  fallocate -l 2G /var/swapfile
  chmod 600 /var/swapfile
  mkswap /var/swapfile
  swapon /var/swapfile
  echo "/var/swapfile swap swap defaults 0 0" >> /etc/fstab
fi