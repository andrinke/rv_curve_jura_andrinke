import setuptools

setuptools.setup(
    name="rv_curve_jura",
    version="0.1",
    author="Andrin Kessler",
    author_email="andrin.mattia@gmail.com",
    description="Plot all RV curves you want!",
    packages=setuptools.find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrinke/rv_curve_jura_andrinke",
    install_requires=["numpy","matplotlib"],
    classifiers=["Programming Language :: Python :: 3"],
)