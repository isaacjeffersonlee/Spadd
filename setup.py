from setuptools import setup, find_packages

setup(
    name="spadd",
    description="Quick add currently playing spotify song to a user playlist with dmenu/bemenu.",
    version="0.1",
    packages=find_packages(),
    scripts=["spadd/spadd_run.py"],
    entry_points={
        "console_scripts": [
            "spadd = spadd.spadd_run:main",
        ]
    }
)
