from setuptools import setup

# Informazioni sul pacchetto
setup(
    name="nome-pacchetto",
    version="numero-versione",
    description="breve-descrizione",
    author="nome-autore",
    author_email="email-autore",
    url="url-repository",
    packages=[],  # Elenco dei pacchetti e moduli
    install_requires=["dipendenza1", "dipendenza2"],  # Dipendenze esterne
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Versione minima di Python richiesta
)
