from setuptools import setup, find_packages

setup(
	name="my_cli_tool",
	version="0.1",
	packages=find_packages(where="src"),
	package_dir={"": "src"},
	entry_points={
		"console_scripts": [
			"my_cli_tool=main:main",
		],
	},
)