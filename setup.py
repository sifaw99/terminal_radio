from setuptools import setup, find_packages
import io

def required(sfx=""):
    with io.open(f"requirements{sfx}.txt", encoding="utf-8") as f:
        return f.read().splitlines()
setup(name='tmuxradio',
      version='0.2.31',
      description='Playing globe radio station from terminal',
      long_description=open('README.txt').read() + "\n\n" + open('CHANGELOG.txt').read(),
      long_description_content_type='text/markdown', 
      url='http://github.com/sifaw99/terminal_radio',
      author='Lahcen Ouchary',
      author_email='lahcen.ouchary@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=required(),
      entry_points={
        "console_scripts": [
            "tmuxradio = src.main:main",
            "radio = src.main:main",
        ]
    },
      zip_safe=False)