from setuptools import setup

def readme():
	with open('README.md') as f:
		return f.read()

setup(name='bobthebot',
      version='1.0',
      description='The funniest joke in the world',
	  long_description=readme(),
	  url='https://github.com/Qu1ntuSs/bobthebot',
      author='Jakob Maier',
      author_email='d33pshitter@gmail.com',
      license='MIT',
	  entry_points = {'console_scripts': ['funniest-joke=bobthebot.command_line:main']},
      packages=['bobthebot'],
	  scripts=['bin/funniest-joke'],
	  install_requires=['markdown'],
	  include_package_data=True,
      zip_safe=False)