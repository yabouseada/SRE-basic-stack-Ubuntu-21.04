import os
# # SRE-basic-stack-Ubuntu-21.04
# CLI fore clear ubuntu desktop v21.04
print('This is a script for sre installation')


print('********************************************')
# ## Directories
print("First we are going to create the directories")
# ```
# mkdir ~/Studies
# mkdir ~/Work
# ```
dir1 = 'mkdir ~/Studies'
dir2 = 'mkdir ~/Work'

os.system(dir1)
os.system(dir2)
print('********************************************')

# ## Req
# ```
# sudo apt-get update
# ```

apt = 'sudo apt-get update'
os.system(apt)

print('********************************************')
# ## Git config
# ```
# sudo apt-get install git-all
# git config --global user.name "yabouseada"
# git config --global user.email "\gitEmail"
# ```
gitName = input("Enter Your Github Name:  ")
gitEmail = input("Enter Your Github Email:  ")
git1 = 'sudo apt-get install git-all'
git2 = f'git config --global user.name "{gitName}"'
git3 = f'git config --global user.email "{gitEmail}"'
os.system(git1)
os.system(git2)
os.system(git3)

print('********************************************')


# ## Insomnia
# ```
# echo "deb [trusted=yes arch=amd64] https://download.konghq.com/insomnia-ubuntu/ default all" \
#     | sudo tee -a /etc/apt/sources.list.d/insomnia.list

# sudo apt-get update
# sudo apt-get install insomnia
# ```
insm1 = 'echo "deb [trusted=yes arch=amd64] https://download.konghq.com/insomnia-ubuntu/ default all" \
    | sudo tee -a /etc/apt/sources.list.d/insomnia.list'
insm2 = 'sudo apt-get update'
insm3 = 'sudo apt-get install insomnia'

os.system(insm1)
os.system(insm2)
os.system(insm3)
print('********************************************')
# ## SSH-Keygen
# ```
# ssh-keygen -t rsa -b 4096 -C "y.abouseada@gmail.com"
# ```
ssh= f'ssh-keygen -t rsa -b 4096 -C "{gitEmail}"'
os.system(ssh)
print('********************************************')
# ## Docker
# ```
# sudo snap install docker
# ```
docker= 'sudo snap install docker'

os.system(docker)

print('********************************************')

# ## Hyper
# ```
# sudo apt install gdebi
# wget - O hyper_3.0.2 https://releases.hyper.is/download/deb
# sudo gdebi deb
# ````
hy1='sudo apt install gdebi'
hy2='wget - O hyper_3.0.2 https://releases.hyper.is/download/deb'
hy3='sudo gdebi deb'

print('********************************************')
# ## Visual Studio Code
# ```
# sudo snap install --classic code # or code-insiders
# ```
vC= 'sudo snap install --classic code # or code-insiders'
os.system(vC)

print('********************************************')
# ## Discord
# ```
# sudo snap install discord
# ```
disc= 'sudo snap install discord'
os.system(disc)

print('********************************************')
# ## Telegram
# ```
# sudo snap install telegram-desktop
# ```
telegram= 'sudo snap install telegram-desktop'
os.system(telegram)