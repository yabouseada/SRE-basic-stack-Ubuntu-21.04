# SRE-basic-stack-Ubuntu-21.04
CLI fore clear ubuntu desktop v21.04

## Directories
```
mkdir ~/Studies
mkdir ~/Work
```

## Req
```
sudo apt-get update
```

## Git config
```
sudo apt-get install git-all
git config --global user.name "yabouseada"
git config --global user.email "y.abouseada@gmail.com"
```

## Insomnia
```
echo "deb [trusted=yes arch=amd64] https://download.konghq.com/insomnia-ubuntu/ default all" \
    | sudo tee -a /etc/apt/sources.list.d/insomnia.list

sudo apt-get update
sudo apt-get install insomnia
```

## SSH-Keygen
```
ssh-keygen -t rsa -b 4096 -C "y.abouseada@gmail.com"
```

## Docker
```
sudo snap install docker
```

## Hyper
```
sudo apt install gdebi
wget - O hyper_3.0.2 https://releases.hyper.is/download/deb
sudo gdebi deb
````

## Visual Studio Code
```
sudo snap install --classic code # or code-insiders
```

## Discord
```
sudo snap install discord
```

## Telegram
```
sudo snap install telegram-desktop
```
