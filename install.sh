sudo apt update
sudo apt -y upgrade

sudo apt install -y python3-pip

sudo apt install -y build-essential libssl-dev libffi-dev python3-dev

pip3 install --upgrade pip

./download_data.sh

export PATH="$HOME/.cargo/bin:$PATH"
export PATH="/home/ubuntu/.local/bin:$PATH"
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh


pip3 install -r requirements.txt


sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi
