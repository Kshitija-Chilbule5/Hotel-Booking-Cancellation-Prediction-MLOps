from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="HotelBookingCancellationPrediction",
    version="0.1",
    author="KshitijaChilbule",
    packages=find_packages(),
    install_requires = requirements,
)