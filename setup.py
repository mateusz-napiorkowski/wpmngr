import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wpmngr", # Replace with your own username
    version="0.0.1",
    author="Mateusz Napiorkowski",
    author_email="mateusz.napiorkowski0@gmail.com",
    description="Wallpaper manager for Xfce",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mateusz-napiorkowski/wpmngr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.6',
)