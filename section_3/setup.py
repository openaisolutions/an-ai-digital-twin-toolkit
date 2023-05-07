from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="DigitalTwinGuide",
    version="0.1",
    author="Your Name",
    author_email="youremail@example.com",
    description="A guide for developing digital twins",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/DigitalTwinGuide",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "numpy==1.20.1",
        "pandas==1.2.2",
        "matplotlib==3.3.4",
        "seaborn==0.11.1",
        "scipy==1.6.1",
        "scikit-learn==0.24.1",
        "requests==2.25.1",
        "beautifulsoup4==4.9.3",
        "lxml==4.6.2",
        "selenium==3.141.0",
        "cucumber==6.10.4",
        "jira==3.0.1",
        "simulink==2.4.0",
        "teamcenter==0.0.6"
    ]
)
