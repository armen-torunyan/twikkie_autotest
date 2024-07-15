REM installing the pipenv, pytest, selenium
echo  Starting installation
pip install pytest
timeout 1
pip -m pip install --upgrade pip
timeout 1
pip install selenium
timeout 1
pip install pytest-html
timeout 1
pip install pytest-xdist
timeout 1
pip install pytest-timeout
timeout 1
pip install requests
timeout 1
pip install jsonpath
timeout 1
pip install allure-pytest
timeout 1
pip install psycopg2
timeout 1
pip install unipath
timeout 1
pip install webdriver-manager
timeout 1
pip install beautifulsoup4
timeout 1
echo  Installation Finished
