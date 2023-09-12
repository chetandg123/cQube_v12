
# cQubeTesting

###  Prerequisites:
 - Open the Terminal
 - Google Chrome need to be installed in the server.
   - Steps to install the Google Chrome
      ```
     wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
     sudo apt install ./google-chrome-stable_current_amd64.deb
     Check chrome brower version using command -> google-chrome -version
      ```
   - Navigate to the directory where Script Folder has been downloaded or cloned 
      ```
      cd cQube_v5/
      git checkout cQube_v5
      git pull
      ```
 - Chrome driver need to be downloaded and placed in the cQubeTesting/Driver/ folder.
 - Steps to Download the chrome driver 

 	Note: Based on the Chrome browser version need to download chrome driver ```https://sites.google.com/chromium.org/driver/```

 
- ### Steps to execute the test script
    ```
     cd cQube_v5/
     sudo apt update
     sudo apt install python3-pip
    ```
 - Execute the Requirement.txt in the terminal (Requirement.txt file is present in the cQubeTesting Folder) [mandatory]
    ```
        sudo pip3 install -r Requirement.txt
    ```
 - Fill the config.ini file (config.ini file present in the cQube_v5/Configurations/ Folder)
     ```		
    [config]
    url=   #Fill the domain name provided in the config.yml file ex: https://domain_name
    ```  
#  Navigate to cQubeTesting Folder directory in the terminal
  ### Steps to Execute the Scripts - Open the terminal and enter the below commands
  ```
  pytest -v -s --capture=tee-sys Testcases/test_dashboard.py --html=Reports/dashboard.html
  pytest -v -s --capture=tee-sys Testcases/test_loginpage.py --html=Reports/loginpage.html
  pytest -v -s --capture=tee-sys Testcases/test_homepage.py --html=Reports/homepage.html
  pytest -v -s --capture=tee-sys Testcases/test_nas.py --html=Reports/nas.html
  pytest -v -s --capture=tee-sys Testcases/test_nishtha.py --html=Reports/nishtha.html
  pytest -v -s --capture=tee-sys Testcases/test_diksha_etb.py --html=Reports/diksha_etb.html
  pytest -v -s --capture=tee-sys Testcases/test_pm_poshan.py --html=Reports/pm_poshan.html
  pytest -v -s --capture=tee-sys Testcases/test_udise.py --html=Reports/udise.html
  pytest -v -s --capture=tee-sys Testcases/test_pgi.py --html=Reports/pgi.html
  pytest -v -s --capture=tee-sys Testcases/test_review_meetings.py --html=Reports/review_meetings.html
  
  ```



##### Note : After execution of scripts,the report will be generated and saved in the Reports folder