from setuptools import setup, find_packages

setup(
    author="ctitus@bnl.gov",
    python_requires=">=3.7",
    description="Software to wrap Tiled Catalogs",
    install_requires=["tiled", "numpy", "databroker"],
    packages=find_packages(),
    name="tiled_wrapper",
    #use_scm_version=True
    )
