from setuptools import setup

setup(
    name="pricepluscost",
    version="0.2.0",
    packages=['pricepluscost',],
    entry_points={
        "console_scripts": [
            "ppc = pricepluscost.database.entrypoint:ppc",
        ]
    },
)