#!/bin/ bash
echo 'installing chalkboard-barnacle now'
chmod +x expire.sh
cp chalkboard.service chalkboard-expire.service chalkboard-resonator.service /etc/systemd/system
cp avahi-resonator.service /etc/avahi/services/
systemctl enable chalkboard.service chalkboard-resonator.service chalkboard-expire.service
systemctl start chalkboard.service chalkboard-resonator.service chalkboard-expire.service
systemctl | grep AKA
