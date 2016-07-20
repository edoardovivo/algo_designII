from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("two_sat_cython.pyx")
)