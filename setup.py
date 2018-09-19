from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='',
    long_description=readme,
    author='Taku MURAKAMI',
    author_email='murakami.taku.17@shizuoka.ac.jp',
    url='https://github.com/murakami17/Interlayer',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

