from setuptools import setup,find_packages, Extension
from setuptools.command.build_ext import build_ext
import os, sys, subprocess

# Command line flags forwarded to CMake (for debug purpose)
cmake_cmd_args = []
for f in sys.argv:
    if f.startswith('-D'):
        cmake_cmd_args.append(f)

for f in cmake_cmd_args:
    sys.argv.remove(f)

class CMakeExtension(Extension):
    def __init__(self, name, cmake_lists_dir='.', **kwa):
        Extension.__init__(self, name, sources=[], **kwa)
        print("cmake_lists_dir", cmake_lists_dir)
        self.cmake_lists_dir = os.path.abspath(cmake_lists_dir)

class CMakeBuild(build_ext):
    def build_extensions(self):
        # Ensure that CMake is present and working
        try:
            out = subprocess.check_output(['cmake', '--version'])
        except OSError:
            raise RuntimeError('Cannot find CMake executable')

        for ext in self.extensions:
            extdir = os.path.abspath(os.path.dirname(self.get_ext_fullpath(ext.name)))
            cfg = 'Release'
            # cfg = 'Debug'
            cmake_args = [
                f'-DCMAKE_BUILD_TYPE={cfg}',
                # Ask CMake to place the resulting library in the directory
                # containing the extension
                f'-DCMAKE_LIBRARY_OUTPUT_DIRECTORY_{cfg.upper()}={extdir}',
                # Other intermediate static libraries are placed in a
                # temporary build directory instead
                f'-DCMAKE_ARCHIVE_OUTPUT_DIRECTORY_{cfg.upper()}={self.build_temp}',
                # Hint CMake to use the same Python executable that
                # is launching the build, prevents possible mismatching if
                # multiple versions of Python are installed
                f'-DPYTHON_EXECUTABLE={sys.executable}',
                # Add other project-specific CMake arguments if needed
                # ...
            ]

            cmake_args += cmake_cmd_args

            if not os.path.exists(self.build_temp):
                os.makedirs(self.build_temp)

            # Config
            subprocess.check_call(['cmake', ext.cmake_lists_dir] + cmake_args,cwd=self.build_temp)
            # Build
            subprocess.check_call(['cmake', '--build', '.', '--config', cfg], cwd=self.build_temp)


import os
with open(os.path.join(__file__,"README.md"), encoding="utf8") as f:
    readme = f.read()

setup_args = dict(name = "texliveondemand",
      version = "0.1",
      packages=find_packages(),
      url="https://github.com/fhswf",
      description="texlive python bindings",
      long_description=readme,
      long_description_content_type="text/markdown",
      license="GNU-AGPL",
      include_package_data=True,
      #ext_modules = [CMakeExtension("texliveondemand")],
      ext_modules = [Extension("texliveondemand", ["pdftex.c", "xetex.c"])],
      #cmdclass = {'build_ext': CMakeBuild}
    )

if __name__ == '__main__':
    setup(**setup_args)