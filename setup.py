from setuptools import setup, find_packages

if __name__ == '__main__':

    setup(
        name='xetmap',
        description='Libreria que te proporciona direcciones reales de Estados Unidos',
        license='MIT',
        url='https://github.com/MrXetwy21/XetMap',
        version='1.4',
        author='MrXetwy21',
        author_email='Xetwy21@gmail.com',
        packages=find_packages(),
        include_package_data=True,
        long_description=open('README.md', encoding='utf-8').read(),
        long_description_content_type='text/markdown',
        classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities"
        ],
        install_requires=["names"],
        python_requires='>=3.10',
        
    )

