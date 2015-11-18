from setuptools import setup

setup(name='pid',
    description='Abstract module for a \
    Proportional-Integral-Derivative Controller',
    url='https://github.com/cjduncana/PID-Controller',
    packages=['pid'],
    zip_safe=False,
    classifiers=[
    	'Development Status :: 1 - Planning',
    	'License :: OSI Approved :: \
    	GNU General Public License v2 (GPLv2)',
    	'Natural Language :: English',
    	'Programming Language :: Python :: 2.7'
    ],
    test_suite='nose2.collector.collector',)