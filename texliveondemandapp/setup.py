from setuptools import setup,find_packages

with open("README.md", encoding="utf8") as f:
    readme = f.read()

setup_args = dict(name = "texliveondemandapp",
      version = "0.1",
      packages=find_packages(),
      url="https://github.com/fhswf",
      description="simple texlive ondemand app",
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      license="GNU-AGPL",
      include_package_data=True,
      #package_data = {
      #  'public': ['*'],
      #}
    )

setup_args['install_requires'] = install_requires = []
with open('requirements.txt') as f:
    for line in f.readlines():
        req = line.strip()
        if not req or req.startswith(('-e', '#')):
            continue
        install_requires.append(req)

if __name__ == '__main__':
    setup(**setup_args)