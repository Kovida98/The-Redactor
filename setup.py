from setuptools import setup, find_packages

setup(
	name='project1',
	version='1.0',
	author='Kovida Mothukuri',
	authour_email='kovida.mothukuri-1@ou.com',
	packages=find_packages(exclude=('tests', 'docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)
