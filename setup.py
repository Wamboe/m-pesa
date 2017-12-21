from setuptools import setup

setup(
    name = 'mpesa',
    version = '0.0.2',
    description = 'a pip installable mpesa package',
    #url = '',
    author = 'Sheila Wambui Karienye',
    author_email = 'sheila.karienye@gmail.com',
    keywords = 'mpesa API module',
    packages = ['mpesa'],
    install_requires = ['pip', 'requests'],
    python_requires='>=2.6',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2'
        'Programming Language :: Python :: 2.7'
        'Programming Language :: Python :: 3'
        'Programming Language :: Python :: 3.4'
        'Programming Language :: Python :: 3.5'
        'Programming Language :: Python :: 3.6'
    ]
)