from setuptools import setup, find_packages

setup(
    name='openhedgehog',
    version='1.0',
    packages=find_packages("src"),
    package_dir={'': 'src'},
    zip_safe=False,
    install_requires=["Django>=1.9"],
    url='http://github.com/ornoone/openhedgehog.git',
    license='LGPL',
    author='darius BERNARD <darius@xornot.fr>',
    author_email='darius@xornot.fr',
    description='easy and efficient money manager in web interface'
)
