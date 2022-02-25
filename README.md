# DATA

## ABOUT

Core metadata for cataloging system generation: parameters and data.

Les données qui permettent la création et l'initialisation de la base de données, l'indexation mais aussi toutes les règles d'affichage de filtrage et de requetage.

Data est le dossier qui contient toutes les données et paramétrages de départ: 
elles sont toutes au format csv puis insérée dans la base de données à l'initialisation

## CONTENT

### RAW

Versions initiales du recensement au format XLS et au format CSV

### EXPORT

- Export des modèles depuis la BDD:
    - meta/rules
    - references
    - models: 
      - datasets
      - organizations
      - comments
      - logs
      - users
    - templates
  
### IMPORT

#### Rules

Les données méta décrivent l'ensemble des champs qui définissent un modèle, toutes les règles qui s'attachent aux champs définitoires d'un modèle. C'est el point d'entrée du paramétrage des contenus.

En effet le fichier `rules.csv` liste tous les champs de données pour tous les modèles présents dans la BDD et dicte la manière d':

- insérer/modifier/supprimer les données dans la base
- indexer les données dans ElasticSearch
- valider les données
- afficher les données 
- afficher les filtres

#### References

Ces données correspondent aux nomenclatures à respecter pour ajouter une valeur à un champ descriptif d'un jeu de données ou d'une organisation.
Pour décrire un jeu de données on utilse plusieurs champs tel que le nom l'url et le sujet, les règles de ce que peut contenir le champ "sujet" est défini grace aux références qui détaille les valeurs acceptées pour le champ sujet.

  - une liste de tous les champs dans les valeurs sont controlées appelée `références`:

    > Exemple: un dataset possède un champ descriptif "Nature et Usage", celui ci accepte seulement les valeurs :Biodiversité, Indicateurs géographiques et socio-démographiques, Agents Physiques, Pesticides
    
Le fichier csv rules puis la table `references` liste toutes les champs dont les valeurs sont controlées par un référentiel.

table `references`
  | field_slug   | table_name|field_label_fr  | field_label_en|
  |------------|-----------|----------------|---------------|
  |nature      | ref_nature| Nature et Usage| Use and Nature|



  - pour chaque référence controlée on trouve la liste des valeurs acceptées en anglais et en francais aggrémenté d'une uri si référentiel sémantique appelée `ref_<nom_du_champ>`:

    > Exemple : Le champ Nature et Usage
    
stocké dans la table `ref_nature`

|field_label_fr  | field_label_en| uri                 |
|----------------|---------------|---------------------|
|Biodiversité    | Biodiversity  |                     |
|Agents Physiques| Physical Agents  |                     |
|Indicateurs géographiques et socio-démographiques|Géographical and socio-demographical indicators||
| Pesticides     | Pesticides |http://purl.obolibrary.org/obo/ENVO_01000371|


#### Templates

Les Templates sont générés via un script dans `scripts/import`
ils permettent l'ajout de jeux de données multiples en chargeant un fichier 
pour importer dans la base via une methode disponible via l'API:

|  Model         | API call                   | Available LANG |
|----------------|----------------------------|----------------|
| Dataset        | post /dataset/upload       | fr/en          |
| Organization   | post /organization/upload  | fr/en          |

#### Models

Les modèles servent à peupler la base de données à l'initialisation mappés et controlés avec les rules
- organizations
- datasets
- commments
- logs
- users
- roles

## SCHEMAS

## MODELS
