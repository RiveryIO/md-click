from setuptools import setup, find_packages

with open('requirements.txt', 'r') as req:
    install_requires = req.readlines()

setup(
    name='md-click',
    version='1.0',
    include_package_data=False,
    zip_safe=True,
    packages=find_packages(),
    py_modules=[
        'md-click'
    ],
    install_requires=install_requires,
    entry_points="""
        [console_scripts]
        mdclick=md_click.main:cli
    """
)
