#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages

setup(
    name='labor_force_analysis',
    version='0.2.1',
    description='Woman labor force analysis.',
    author='Ziqi Huang',
    author_email='zikih25@gmail.com',
    license='MIT',
    url='https://github.com/Francesgaba/labor_force_analysis',
    packages=['laborforce_analysis'],
    install_requires=[
        'matplotlib>=3.0.2',
        'numpy>=1.15.2',
        'pandas>=0.23.4',
        'seaborn>=0.11.0',

    ],
)


# In[ ]:




