from setuptools import setup, find_packages

setup(name="browserstack.REST.Wrapper",
      version="1.0",
      description="Python wrapper for Browserstack API",
      author="Bhavesh Sharma",
      author_email="bhavesh.sharma.mnc@gmail.com",
      url="http://github.com/bhaveshbhu/browserstackRESTApi.Wrapper",
      packages=find_packages(),
      keywords="browserstack python api",
      zip_safe=True,
      install_requires=[
      "simplejson>=3.3.2",
      "requests>=2.2.0",
      ]
      )
