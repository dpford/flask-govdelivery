from distutils.core import setup

setup(
    # Application name:
    name="flask-govdelivery",

    # Version number (initial):
    version="0.2.0",

    # Application author details:
    author="CFPB",
    author_email="tech@cfpb.gov",

    # Packages
    packages=["flask_govdelivery", "flask_govdelivery.govdelivery"],

    # Include additional files into the package
    include_package_data=True,

    # Dependent packages (distributions)
    install_requires=[
        "flask",
    ],
)
