from setuptools import setup
setup(name = "fixer-demo",
      version = '0.2',
      description = 'getting rates with the help of fixer' ,
      url = 'https://github.com/arian-hadi/fixer-Demo.git',
      author = 'Arian Hadi',
      author_email = 'arianhadi2003@gmail.com',
      license = 'MIT',
      packages = ['fixer'],
      install_requires = ['requests'],
      zip_safe = False)