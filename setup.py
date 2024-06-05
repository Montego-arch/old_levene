from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in old_levene/__init__.py
from old_levene import __version__ as version

setup(
	name="old_levene",
	version=version,
	description="old app for levene",
	author="Montego",
	author_email="mmanuelmiles@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
