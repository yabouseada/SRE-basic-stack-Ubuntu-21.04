
#!/bin/python

import os
import sys

class SREStack:

    # Init and config
    def __init__(self):
        print("SREStack CLI started please wait for input requests")
        self.username = input("Type your gitHub username: ")
        self.email = input("Type your gitHub email: ")
    

    def userConfig(self):
      

        gitName = f'git config --global user.name "{self.username}"'
        gitMail = f'git config --global user.email"{self.email}"'
       
        gitConfig=[gitName,gitMail]
        return(gitConfig)
         
    # Execute each function as intended
 
    
    def test(self):
        user_array= (self.userConfig())
        for user in user_array:
            print(user)
        
        return(True)


instancedClass = SREStack()

instancedClass.test()
      



# # SRE-basic-stack-Ubuntu-21.04
# CLI fore clear ubuntu desktop v21.04
instancedClass = SREStack()

instancedClass.test()
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
