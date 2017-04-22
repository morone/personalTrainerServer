from setuptools import setup

setup(
    name='personalTrainerServer',
    packages=['personalTrainerServer'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)
