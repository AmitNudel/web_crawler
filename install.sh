#!/bin/sh

# python3 pip
if [ -x "$(command dpkg -s python3-pip)" ]; then
    sudo apt install python3-pip
fi
#requests library
if [ -x "$(python3 -c "import requests")" ]; then
    pip install requests
fi
#html5 library
if [ -x "$(python3 -c "import html5lib")" ]; then
    pip install html5lib
fi
#bs4 library
if [ -x "$(python3 -c "import bs4")" ]; then
    pip install bs4
fi
#validators library
if [ -x "$(python3 -c "import validators")" ]; then
    pip install validators
fi