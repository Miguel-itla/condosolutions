from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in condosolutions/__init__.py
from condosolutions import __version__ as version

setup(
	name="condosolutions",
	version=version,
	description="Aplicacion para el manejo de condominios.",
	author="CondoSolutions",
	author_email="condosolutions@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
