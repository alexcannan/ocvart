from setuptools import setup, find_namespace_packages

setup(
    name='ocvart',
    version='1',
    python_requires='>=3.8',
    author='Alex Cannan',
    author_email='alexfcannan@gmail.com',
    packages=find_namespace_packages(include=['ocvart.*']),
    long_description="OCVART: OpenCV Art",
    install_requires=[
        "scikit-video",
        "opencv-python"
    ]
)

