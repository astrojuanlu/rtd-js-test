import setuptools

setuptools.setup(
    name="rtd-js-test",
    version="0.0.1",
    author="Juan Luis Cano",
    author_email="juanlu001@gmail.com",
    description="Test for https://github.com/rtfd/readthedocs.org/issues/4367",
    url="https://github.com/Juanlu001/rtd-js-test",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "plotly",
        "ipywidgets",
        "notebook",
        "nbsphinx",
        "jupyter_sphinx",
    ]
)
