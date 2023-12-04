from setuptools import setup,find_packages


import os
with open(os.path.join(os.path.dirname(__file__),"README.md"), encoding="utf8") as f:
    readme = f.read()

setup_args = dict(name = "texliveondemandapp",
      version = "0.1",
      packages= ["app.py", "wsgi.py"],
      url="https://github.com/fhswf",
      description="simple texlive ondemand app",
      long_description=readme,
      long_description_content_type="text/markdown",
      license="GNU-AGPL",
      include_package_data=True,
      #package_data = {
      #  'public': ['*'],
      #}
    )

setup_args['install_requires'] = install_requires = []
with open(os.path.join(os.path.dirname(__file__),"requirements.txt")) as f:
    for line in f.readlines():
        req = line.strip()
        if not req or req.startswith(('-e', '#')):
            continue
        install_requires.append(req)

if __name__ == '__main__':
    setup(**setup_args)