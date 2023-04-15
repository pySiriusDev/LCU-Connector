from setuptools import setup


with open('README.md') as file:
    readme = file.read()


setup(
    name='LCU Connector',
    version='1.0.0',
    author='Gabriel Viana',
    author_email='ssiriusbeck@gmail.com',
    description='Easy-to-use wrapper for the League Client API.',
    long_description=readme,
    packages=['lcu_connector'],
    install_requires=['requests', 'psutil'],
    keywords=[
        'league client',
        'league client api',
        'league client api wrapper',
        'api wrapper'
        'league of legends',
        'league of legends api',
        'lcu-driver',
        'lcu driver',
        'lcu-connector',
        'lcu connector'
    ],
    license='MIT'
)
