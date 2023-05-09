import setuptools

setuptools.setup(
    name="rv_curve_jura",
    version="0.1",
    author="Andrin Kessler",
    author_email="andrin.mattia@gmail.com",
    description="Plot all RV curves you want!",
    packages=setuptools.find_packages(),
    install_requires=["numpy","matplotlib"],
    classifiers=["Programming Language :: Python :: 3"],
)