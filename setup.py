import re
import setuptools


def get_property(
        prop: str,
        project: str
) -> str:

    result = re.search(
        r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop),
        open(project + '/_version.py').read())

    return result.group(1)


project_name = 'reinspy'

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=project_name,
    version=get_property('__version__', project_name),
    author="Gene Dan",
    author_email="genedan@gmail.com",
    description="reinspy - a Python Reinsurance Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/genedan/reinspy",
    project_urls={
        "Documentation": "https://reinspy.com/docs"
    },
    install_requires=[
        'chainladder',
        'numpy',
        'pandas',
        'rich'
    ],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires='>=3.10.0',
)