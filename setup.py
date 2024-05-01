from setuptools import setup, find_packages

setup(
    name='in_parallel_package',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'tqdm',
        'concurrent-futures; python_version<"3.2"'
    ],
    python_requires='>=3.6',
    description='A simple utility for running functions in parallel.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourgithub/in_parallel_package',  # Optional
)
