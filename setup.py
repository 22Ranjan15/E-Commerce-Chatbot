from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements()->List[str]:
    requirements = []
    try:
        with open('requirements.txt', 'r') as obj:
            lines = obj.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != HYPEN_E_DOT:
                    requirements.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
        
    return requirements

setup(
    name = "Custom E-Commerce Chatbot Application",
    version = "0.0.1",
    author = "Ranjan",
    author_email = "ranjandasbd22@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements()
)