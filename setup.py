# -*- coding: utf-8 -*-
from distutils.core import setup
LONGDOC = """
Please go to http://202.196.37.147:18080/zutnlp-knowledge/lda-SubjectAnalysis.git
"""

setup(
    name='textrank4zh',
    version='0.3',
    description='Extract keywords and abstract Chinese article',
    long_description=LONGDOC,
    author='MaTongTong , HuXiWei',
    author_email='1143298661@qq.com',
    url='http://202.196.37.147:18080/zutnlp-knowledge/lda-SubjectAnalysis.git',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python :: 3.6.4',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='NLP,Chinese,Keywords extraction, Abstract extraction',
    install_requires=['jieba >= 0.35', 'numpy >= 1.7.1', 'networkx >= 1.9.1'],
    packages=['textrank4zh'],
    package_dir={'textrank4zh':'textrank4zh'},
    package_data={'textrank4zh':['*.txt',]},
)