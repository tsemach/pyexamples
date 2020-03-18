from setuptools import setup

setup(
   name='pyexamples',
   version='0.0.1',
   description='A collection of python examples',
   author='Tsemach Mizrachi',
   author_email='tsemach.mizrachi@gmail.com',
   packages=['pyexamples'],  #same as name
   install_requires=['aiohttp>=2.3.1'], #external packages as dependencies
)