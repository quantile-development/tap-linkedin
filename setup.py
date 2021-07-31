import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tap-linkedin",
    version="0.0.1",
    author="Jules Huisman",
    author_email="jules.huisman@quantile.nl",
    description="Singer.io tap for company LinkedIn",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quantile-development/tap-linkedin",
    project_urls={
        "Bug Tracker": "https://github.com/quantile-development/tap-linkedin/issues",
    },
    install_requires=[
        'singer-sdk==0.3.3',
        'requests==2.25.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    packages=['tap_linkedin'],
    entry_points="""
    [console_scripts]
    tap=tap_linkedin.tap:TapLinkedin.cli
    tap-linkedin=tap_linkedin.tap:TapLinkedin.cli
    """,
    python_requires=">=3.8",
)