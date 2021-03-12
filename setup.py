from setuptools import setup, find_packages
from md_click import __version__

with open('requirements.txt', 'r') as req:
    install_requires = req.readlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='md-click',
    description="A command line tool for automatically generating .md files from click's CLI command.",
    author='Rivery',
    version="1.0.2",
    include_package_data=False,
    zip_safe=True,
    packages=find_packages(),
    py_modules=[
        'md-click'
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RiveryIo/md-click",
    project_urls={
        "Bug Tracker": "https://github.com/RiveryIo/md-click/issues",
        "Documentation": "https://riveryio.github.io/md-click"
    },
    install_requires=install_requires,
    entry_points="""
        [console_scripts]
        mdclick=md_click.main:cli
    """,
    license_files=("LICENSE", ),
    license="BSD 3.0",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Documentation",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: Markdown"
    ],
    python_required=">=3.6",
)
