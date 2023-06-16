from setuptools import setup, find_packages
!git clone https://github.com/lahavfrid/DroneProject
setup(
    name='YourPackageName',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'dependency1',
        'dependency2',
    ],
    author='Roei krinitz, Lahav fridlend, Alon Spector',
    author_email='your@email.com',
    description='Description of your project',
    url='https://github.com/lahavfrid/DroneProject',
)
