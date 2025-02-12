from setuptools import find_packages
from setuptools import setup
 
with open("README.md") as fp:
    long_description = fp.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="python_project",
    version='0.1',
    url="https://github.com/NatalieZelenka/python_project_template",
    author="Natalie Zelenka",
    author_email="n.zelenka@ucl.ac.uk",
    keywords="data science, data",
    description="Package description here",
    long_description=long_description,
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    python_requires='>=3.6',
    include_package_data=False,
    install_requires=requirements,
)
