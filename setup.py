from setuptools import setup

from mytodo import __app_name__, __version__

setup(
    name=__app_name__,
    version=__version__,
    packages=[f"{__app_name__}"],
    entry_points={
        "console_scripts": [
            f"{__app_name__}={__app_name__}.__main__:main"
        ]
    }
)