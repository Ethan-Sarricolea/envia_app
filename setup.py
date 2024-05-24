from setuptools import setup, find_packages

setup(
    name='EnviApp',
    version='1.3.0',
    description='App para colaboradores y administracion de Envia',
    url='https://github.com/Ethan-Sarricolea/envia_app.git',
    author='Sarricolea Cortés Ethan Yahel',
    author_email='esarricolea@gmail.com',
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