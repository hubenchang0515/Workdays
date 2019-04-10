import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Workdays",
    version="0.0.1",
    author="Plan C",
    author_email="hubenchang0515@outlook.com",
    description="A simple library about checking workdays and holidays",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hubenchang0515/Workdays",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Anti 996",
        "Operating System :: OS Independent",
    ],
)