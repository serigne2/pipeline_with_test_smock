

# Chargement de Données dans MySQL avec Tests Mock

## Objectif

L'objectif de ce projet est de créer une utilité en Python qui permet de charger des données d'un DataFrame Pandas dans une base de données MySQL. Une attention particulière est portée sur la mise en place de tests unitaires robustes en utilisant des mocks pour simuler les connexions à la base de données, ce qui permet de tester le comportement de l'application sans nécessiter une connexion réelle à une base de données MySQL.

## Description

Ce projet comprend une fonction `load_data` qui facilite le chargement de données dans une base de données MySQL. Elle utilise SQLAlchemy pour gérer les connexions à la base de données et Pandas pour manipuler les données. En parallèle, des tests unitaires sont développés pour s'assurer que la fonction se comporte comme attendu, en utilisant des mocks pour simuler les interactions avec la base de données.

## Fonctionnalités

- **Chargement de données** : Permet de transférer des données d'un DataFrame Pandas vers une table MySQL.
- **Intégration avec SQLAlchemy** : Utilisation de SQLAlchemy pour une gestion simplifiée des connexions et transactions SQL.
- **Tests unitaires avec mocks** : Utilisation de la bibliothèque `unittest.mock` pour tester la fonction sans avoir besoin d'une base de données MySQL réelle.

## Installation

Pour utiliser ce projet, clonez le dépôt et installez les dépendances nécessaires :

```bash
git clone https://github.com/votre-nom-utilisateur/projet-mysql-mock.git
cd projet-mysql-mock
pip install -r requirements.txt
```

## Utilisation

Voici comment vous pouvez utiliser la fonction `load_data` pour charger des données dans MySQL :

```python
import pandas as pd
from src.load import load_data

# Exemple de données
data = {
    'date': ['2021-01-01', '2021-01-02'],
    'price': [100.0, 200.0]
}
df = pd.DataFrame(data)

# Charger les données dans MySQL
load_data(df, db_name='nom_de_votre_base_de_donnees', table_name='nom_de_votre_table')
```

## Tests

Les tests unitaires sont inclus pour vérifier le bon fonctionnement de la fonction `load_data`. Les tests utilisent des mocks pour simuler les connexions à la base de données.

Pour exécuter les tests :

```bash
pytest tests/test_load.py
```

## Structure du Projet

Voici la structure du projet :

```
Voici la section "Structure du Projet" pour votre README :




├── data/
│   └── input_data.csv  # Fichier CSV réel pour l'extraction des données
│
├── src/
│   ├── extract.py      # Module pour l'extraction des données
│   ├── transform.py    # Module pour la transformation des données
│   ├── load.py         # Module pour le chargement des données dans MySQL
│   └── utils.py        # Fonctions utilitaires pour le pipeline ETL
│
├── tests/
│   ├── test_extract.py   # Tests unitaires pour le module d'extraction
│   ├── test_transform.py # Tests unitaires pour le module de transformation
│   ├── test_load.py      # Tests unitaires pour le module de chargement
│   └── test_utils.py     # Tests unitaires pour les fonctions utilitaires
│
├── config.py            # Fichier de configuration pour les paramètres du projet
└── main.py              # Script principal pour exécuter le pipeline ETL
```



## Dépendances

Ce projet nécessite les bibliothèques Python suivantes :

- `pandas`
- `SQLAlchemy`
- `mysql-connector-python` ou `PyMySQL`

Vous pouvez installer ces dépendances avec la commande suivante :

```bash
pip install -r requirements.txt
```

## Contributions

Les contributions sont les bienvenues ! Si vous trouvez un bug ou avez une suggestion d'amélioration, n'hésitez pas à ouvrir une issue ou à soumettre une pull request.

---

N'oubliez pas de remplacer `"votre-nom-utilisateur"` par votre nom d'utilisateur GitHub et d'ajuster les détails spécifiques à votre projet. Ce README présente clairement l'objectif, la description, et les instructions essentielles pour utiliser et tester le projet.