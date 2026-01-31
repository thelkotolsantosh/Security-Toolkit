from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='security-toolkit',
    version='1.0.0',
    author='Security Development Team',
    author_email='security@example.com',
    description='A comprehensive toolkit for security professionals and penetration testers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/cybersecurity-toolkit',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'Topic :: System :: Monitoring',
        'Topic :: Security',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    python_requires='>=3.8',
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'cst-scan=cybersecurity_toolkit.cli:port_scan',
            'cst-analyze=cybersecurity_toolkit.cli:analyze_password',
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords='security cybersecurity penetration-testing scanner vulnerability',
)
