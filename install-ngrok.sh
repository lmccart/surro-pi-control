sudo cp ngrok.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable ngrok.service
sudo systemctl start ngrok.service