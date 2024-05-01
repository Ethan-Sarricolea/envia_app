from setuptools import setup, find_packages

setup(
    name='EnviApp',
    version='1.1.1',
    description='App de envia para colaboradores y administracion de negocio',
    url='https://github.com/Ethan-Sarricolea/envia_app.git',
    author='Sarricolea Cortés Ethan Yahel',
    author_email='esarricolea@email.com',
    packages=find_packages(),  # Busca automáticamente todos los paquetes y módulos de Python en el directorio actual
    classifiers=[
        'Programming Language :: Python :: 3.11.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'mi_ejecutable = main:main',  # Entrada para el ejecutable
        ],
    },
    python_requires='>=3.6',  # Versión mínima de Python requerida
)