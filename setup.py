from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='object-freezer',
    version='0.0.1',
    description='Python module for freezing objects',
    author='Shunichiro Nomura',
    author_email='nomura@space.t.u-tokyo.ac.jp',
    install_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    url='https://github.com/shunichironomura/freezer',
    license='MIT',
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests',
    zip_safe=False)