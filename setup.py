from setuptools import setup

setup(
    name="kwl",
    version="1.0",
    py_modules=["kwl"],
    install_requires=[
        "click",
        "boto3",
        "kubernetes",
        "pyfiglet",
        "click"
    ],
    entry_points="""
        [console_scripts]
        kwl=main:operation
    """,
    )