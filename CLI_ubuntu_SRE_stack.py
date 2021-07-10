
#!/bin/python

import os
import sys

class SREStack:

    # Init and config
    def __init__(self):
        print("SREStack CLI started please wait for input requests")
        

    def userConfig(self):
        username = input("Type your username: ")
        email = input("Type your email: ")

        gitUsernameConfigCommand = "git config --global user.name \"" + username + "\""
        gitEmailConfigCommand = "git config --global user.email \"" + email + "\""

        os.system(gitUsernameConfigCommand)
        os.system(gitEmailConfigCommand)

        return(True)
        
    # Execute each function as intended
    def exec(self):
        self.userConfig()
        return(True)

instancedClass = SREStack()

instancedClass.exec()



# # SRE-basic-stack-Ubuntu-21.04
# CLI fore clear ubuntu desktop v21.04

# ## Directories
# ```
# mkdir ~/Studies
# mkdir ~/Work
# ```

# ## Req
# ```
# sudo apt-get update
# ```

# ## Git config
# ```
# sudo apt-get install git-all
# git config --global user.name "yabouseada"
# git config --global user.email "y.abouseada@gmail.com"
# ```
# ## SSH-Keygen
# ```
# ssh-keygen -t rsa -b 4096 -C "y.abouseada@gmail.com"
# ```

# ## Docker
# ```
# sudo snap install docker
# ```

# ## Hyper
# ```
# sudo apt install gdebi
# wget - O hyper_3.0.2 https://releases.hyper.is/download/deb
# sudo gdebi deb
# ````

# ## Visual Studio Code
# ```
# sudo snap install --classic code # or code-insiders
# ```

# ## Discord
# ```
# sudo snap install discord
# ```

# ## Telegram
# ```
# sudo snap install telegram-desktop
# ```
