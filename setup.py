from distutils.core import setup

setup(
    name="Sax-REST",
    version="0.1",
    author="Daniel Santos",
    author_email="dsantosp12@gmail.com",
    packages=["app"]
    include_packages_data=True,
    url="http://github.com/dsantosp12/Sax-REST",
    description=""
    install_requires=[
        "flask",
        "peewee"
    ]
)
