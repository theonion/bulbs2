# bulbs2 [![Build Status](https://travis-ci.org/theonion/bulbs2.svg?branch=master)](https://travis-ci.org/theonion/bulbs2)

> the next generation of technical debt

`bulbs2` is the very first step in re-architecting the [django-bulbs](https://github.com/theonion/django-bulbs) 
package into a generic, non-presecriptive base of Django installable apps.
 
Rather than have a monolithic series of applications that enforce design choices to all applications that inherit from 
it, `bulbs2` will provide a series of abstract, generic mixins, models, managers and signals that can be directly 
used or subclassed. The objective is to provide a basic means of describing publishable content.

All other extensions (workflows, serializers, search, etc.) should be refactored into separate applications that can 
accompany `bulbs2` at the discretion of the scope of the application.


## Getting the Code

You can clone the code via _git_:

```bash
$ git clone https://github.com/theonion/bulbs2.git
```

Alternatively, if you just want to use it in a Django application, you can install it via _pip_:

```bash
$ pip install -e https://github.com/theonion/bulbs2
```

__Note:__ since this is a far-afield project that may or may not be brought to production, I am refraining from adding 
it to the PyPI index.


## Testing the Code

To run the tests, clone the repository from GitHub (see steps above). You should then create a virtual environment with 
Python 3 and install the project to that:

```bash
$ cd /path/to/virtualenvs
$ virtualenv -p python3 bulbs2
$ source bulbs2/bin/activate
$ cd /path/to/bulbs2
$ pip install -e .
$ pip install "file://$(pwd)#egg=bulbs[dev]"
$ py.test tests
```
