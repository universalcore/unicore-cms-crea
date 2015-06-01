from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'requirements.txt'), 'r') as fp:
    requires = filter(None, fp.readlines())

setup(name='unicore-cms-gem',
      version='0.2.0',
      description='GEM Pyramid Frontend Site for Universal Core ',
      long_description='GEM Pyramid Frontend Site for Universal Core ',
      classifiers=[
      "Programming Language :: Python",
      "Framework :: Pyramid",
      "Topic :: Internet :: WWW/HTTP",
      "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Praekelt Foundation',
      author_email='dev@praekelt.com',
      url='http://github.com/universalcore/unicore-cms-gem',
      license='BSD',
      keywords='web pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="unicorecmsgem",
      entry_points="""\
      [paste.app_factory]
      main = unicorecmsgem:main
      """,
      message_extractors={'.': [
      ('**.py', 'python', None),
      ('**.pt', 'chameleon', None),
      ]},
      )
