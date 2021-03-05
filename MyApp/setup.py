from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()
# delete the url info if error, also change version in an update
setup(
  name = "ConsoleHelp",
  version = "0.3.9",
  description = "For all of your console needs!",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  author = "darkdarcool30",
  author_email = "darkdarcool@gmail.com",
#To find more licenses or classifiers go to: https://pypi.org/classifiers/
  license = "GNU General Public License v3 (GPLv3)",
  packages=['ConsoleHelp'],
  classifiers = [
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
  "Operating System :: OS Independent",
],
  zip_safe=True,
  python_requires = ">=3.0",
)
