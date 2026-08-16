from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path : str) -> List[str]:
    
    #This function will return the requirements
    
    requirements = []
    
    with open('requirements.txt') as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            
    return requirements
        
setup(
    name = 'student-project',
    version = '0.0.1',
    author = 'Sumit Maurya',
    author_email = 'mauryasumit620@gmail.com',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)