from setuptools import setup, find_packages

setup(
    name='Prototipo',
    version='1.0.1',
    #description='Una breve descripción de mi paquete',
    #long_description='Una descripción más detallada de mi paquete',
    author='Sarricolea Cortés Ethan Yahel',
    author_email='esarricolea@email.com',
    #url='https://github.com/tu_usuario/mi_paquete',
    packages=find_packages(),  # Busca automáticamente todos los paquetes y módulos de Python en el directorio actual
    classifiers=[
        'Programming Language :: Python :: 3.11.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Versión mínima de Python requerida
)
