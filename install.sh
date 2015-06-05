cp chalkboard.service chalkboard-resonator.service /etc/systemd/system
cp avahi-resonator.service /etc/avahi/services/
systemctl enable chalkboard.service chalkboard-resonator.service
systemctl start chalkboard.service chalkboard-resonator.service
systemctl | grep AKA