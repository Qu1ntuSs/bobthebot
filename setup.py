from setuptools import setup

setup(name='bobthebot',
      version='0.5',
      description='The funniest joke in the world',
      author='Jakob Maier',
      author_email='d33pshitter@gmail.com',
      license='MIT',
      packages=['bobthebot'],
	  scripts=['bin/funniest-joke', 'bin/unfunniest-joke.py'],
	  install_requires=['markdown'],
      zip_safe=False)