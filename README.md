# Days4Innovation

Il faut un environnement Windows pour déployer l'application avec la fonction d'envoi de calendrier par mail.

## Prérequis
Cloner le repository

```sh
$ mkdir Days4Innovation
$ cd Days4Innovation
$ git clone https://github.com/mouhagaye/Days4Innovation.git .
```

- Version de Python utilisée : Python 3.7.1
- Créer un environnement virtuel et y installer les requirements avec :
```sh
pip install -r requirements.txt
```
- Executer le script de création de la base de données MySql

- Modifier les credentials pour accéder à MySql dans app.py en y mettant les votres


## Déploiement


https://www.google.com/settings/security/lesssecureapps

Pour mettre en production utiliser waitress (en l'installant dans l'environnement virtuel) et NGINX.2020 . (cf https://dev.to/thetrebelcc/how-to-run-a-flask-app-over-https-using-waitress-and-nginx-2020-235c)