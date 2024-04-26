from setuptools import setup, find_packages

setup(
    name='Envia App',
    version='1.0.5',
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
    python_requires='>=3.6',  # Versión mínima de Python requerida
)