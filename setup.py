from setuptools import setup, find_packages
from bootstrap5form.meta import VERSION

setup(
    name='django-bootstrap5-form',
    version=str(VERSION),
    description="django-bootstrap5-form",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords='bootstrap5,django',
    author='gwasser',
    author_email='garret@wassiverse.com',
    url='http://github.com/gwasser/django-bootstrap5-form',
    license='MIT',
    test_suite='runtests.runtests',
    install_requires = [
        "django>=3,<4",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
