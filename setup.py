from distutils.core import setup
setup(
  name = 'scratchapi3',
  author_email = 'example@example.com',
  version = '1.0.0',
  classifiers = [
      "Programming Language :: Python :: 3",
  ],
  description = ' scratchapi3',
  licence = 'MIT',
  instal_requires =['requests','os','linecache'],
  packages = ['scratchapi3'],
  author = 'ninjamar',
  python_require = '>=3.7',
  url = 'https://github.com/ninjamar/scratchapi3'
)
