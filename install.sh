#!/bin/sh

git clone https://github.com/tjlagrow/CIS-422-Group-Project-1.git
cd CIS-422-Group-Project-1/
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get install -y nodejs
cd Front_End
npm install
npm run build
cd ..
node Front_End/server
