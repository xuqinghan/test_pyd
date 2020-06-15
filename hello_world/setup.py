#python setup.py build_ext --inplace

from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Hello world app',
    ext_modules=cythonize(["hello.pyx",
                        'hello_py.py',
                        ],
                        annotate=True),
    zip_safe=False,
)