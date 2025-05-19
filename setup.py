from setuptools import setup, find_packages

setup(
    name="solanasentiment",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'sqlalchemy',
        'alembic',
        'psycopg2-binary',
    ],
)
