from setuptools import setup

requires = ["pydantic", "aiohttp", "requests"]
 
setup(
    name="school_mosreg_api",
    version="0.8.5",
    description="SchoolMosregAPI by DSOP",
    url="https://github.com/Den4ikSuperOstryyPer4ik/SchoolMosregRuAPI",
    download_url="https://github.com/Den4ikSuperOstryyPer4ik/SchoolMosregRuAPI/releases/latest",
    author="Den4ikSuperOstryyPer4ik",
    license="GNU GPLv3",
    keywords="school mosreg api ru python school-mosreg-api school-mosreg-ru-api",
    project_urls={"Source": "https://github.com/Den4ikSuperOstryyPer4ik/SchoolMosregRuAPI"},
    package_data={
        "school_mosreg_api": ["py.typed"],
    },
    requires=requires
)
