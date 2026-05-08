from setuptools import setup, find_packages
from typing import List

# function to bring all packages r libraries present in requirements.txt
hypen_e = "-e ."
def find_requirement(file_path:str)->List[str]:

    requir =[]
    with open(file_path) as file:
        requir = file.readlines()
        requirement = [req.replace("\n","") for req in requir]
        if hypen_e in requirement:
            requirement.remove(hypen_e)
    return requirement

setup(
    name = "Ml end to end project",
    version = "0.0.1",
    author="Amjad Hussain",
    author_email="engramjad.hu@gmail.com",
    packages=find_packages(),
    install_requires=find_requirement("requirements.txt")

)