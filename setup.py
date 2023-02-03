import re
from sys import argv

from setuptools import setup

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

setup(
    name="school_mosreg_api",
    version="0.1.0",
    description="SchoolMosregAPI by DSOP",
    url="https://github.com/Den4ikSuperOstryyPer4ik/SchoolMosregAPI",
    download_url="https://github.com/Den4ikSuperOstryyPer4ik/SchoolMosregAPI/releases/latest",
    author="Den4ikSuperOstryyPer4ik",
    license="GNU GPLv3",
    keywords="school mosreg api ru python school-mosreg-api school-mosreg-ru-api",
    project_urls={"Source": "https://github.com/Den4ikSuperOstryyPer4ik/SchoolMosregAPI"},
    python_requires="~=3.7",
    packages=["school_mosreg_api"],
    install_requires=requires
)