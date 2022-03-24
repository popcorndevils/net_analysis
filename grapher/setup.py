from setuptools import setup, find_packages

setup(
    name = "grapher",
    version = "0.0.2",
    description = "This is a test",
    author = "Behn Heart",
    author_email = "popcorndevils@gmail.com",
    url = "http://www.google.com",
    packages = find_packages(),
    install_requires = [
        "pandas",
        "networkx",
        "bokeh",
        "ipywidgets",
        "pytest"
    ]
)
