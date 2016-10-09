from setuptools import setup, find_packages


version = open('packaging/VERSION').read().strip()
requirements = open('packaging/requirements.txt').read().split("\n")
test_requirements = open('packaging/requirements-test.txt').read().split("\n")

setup(
    name='ansible-prngmgr-inventory',
    version=version,
    author='Workonline Communications',
    author_email='communications@workonkonline.co.za',
    description='An ansible dynamic inventory module to fetch peering session data from prngmgr',
    long_description='',
    license='LICENSE',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
    ],
    packages=find_packages(
        include=[
            'prngmgr_inventory'
        ],
        exclude=[]
    ),
    entry_points={
        'console_scripts': ['prngmgr-inventory=prngmgr_inventory.command_line:main']
    },
    include_package_data=True,

    url='https://github.com/wolcomm/ansible-prngmgr-inventory',
    download_url='https://github.com/wolcomm/ansible-prngmgr-inventory/%s' % version,

    install_requires=requirements,
    tests_require=test_requirements,
    test_suite='nose.collector'
)
