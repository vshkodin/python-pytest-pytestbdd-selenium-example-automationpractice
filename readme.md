### Example of UI Testing Framework with screenshots and Report using Python, Pytest, Pytest-BDD,  Selenium, and Allure.
### How to Build/Run locally:
#### clone repo:
```
git clone https://github.com/vsshk/python-pytest-pytestbdd-selenium-example-automationpractice.git
cd python-pytest-pytestbdd-selenium-example-automationpractice
```
#### Dependencies 
1. In order to run you have to install Python3.6+
2. You need to have pip installed
3. install python3 - pip  https://www.python.org/downloads/
4.install allure reports https://docs.qameta.io/allure/ 
5. Chrome Browser https://www.google.com/chrome
6. Chrome driver https://chromedriver.chromium.org/downloads
7. Getting dependencies:
```
$ pip install virtualenv
$ python3 virtualenv env
$ env/Scripss/activate (for win)
$ source env/bin/activate (for mac-linux)
$ pip install -r requirements.txt
```

8. Update chromepath=r'your\path\chromedriver.exe'  in conftest.py 
#### Running  tests
* Headful is default run
```
& pytest 
```
* in order to run Headless 
```
& pytest --headless true
```
#### Report
* get report:
```
allure serve report
```
