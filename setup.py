from setuptools import setup

import conf

attrs={}

for i in dir(conf):
    if not i.startswith('_'):
        attrs[i] = getattr(conf, i)

attrs['name'] = attrs['pypi_name']


setup(
 py_modules=['jinja2-easy.generator'],
 install_requires=['platformdirs', 'jinja2'],
 **attrs
)
