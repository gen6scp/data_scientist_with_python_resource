# setup.py (with dependencies)

setup(
    name="text_analysis",
    version="0.1.0",
    description="A package for counting word occurrences in text files.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.18.0',
        'pandas>=1.0.0'
    ],
)
