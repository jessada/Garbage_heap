from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(["exac_annotation.py","exac_annotation_sqlite.py"])
)
