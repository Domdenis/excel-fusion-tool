# 🧬 Outil de Fusion Excel Agnostique

Une application web simple et intuitive pour fusionner deux fichiers Excel en fonction de clés de correspondance flexibles.

## 📋 Fonctionnalités

✅ **Upload de fichiers Excel** - Téléchargez deux fichiers XLSX  
✅ **Clés de fusion flexibles** - Créez des clés composées de plusieurs colonnes  
✅ **Sélection intelligente** - Choisissez les colonnes à importer  
✅ **Fusion par left join** - Enrichissez votre base de données  
✅ **Téléchargement instantané** - Récupérez le fichier fusionné  
✅ **Nettoyage automatique** - Normalisation des noms de colonnes  

## 🚀 Démarrage rapide

### Accès en ligne
Cliquez sur le lien de déploiement Streamlit Cloud (voir les badges du dépôt).

### Installation locale

**Prérequis :**
- Python 3.8+
- pip (gestionnaire de paquets Python)

**Étapes :**

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-username/excel-fusion-tool.git
cd excel-fusion-tool

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Lancer l'application
streamlit run app.py
```

L'application s'ouvrira automatiquement dans votre navigateur (http://localhost:8501).

## 📖 Mode d'emploi

### Étape 1 : Upload des fichiers
1. Téléchargez votre **fichier source** (la base à enrichir)
2. Téléchargez votre **fichier d'enrichissement** (les données supplémentaires)

### Étape 2 : Définir les clés de fusion
- Sélectionnez les colonnes du fichier source qui formeront la clé
- Sélectionnez les colonnes correspondantes du fichier d'enrichissement
- **Important** : Les deux doivent avoir le même nombre de colonnes

Exemple :
- Source : `[Nom, Prénom]` 
- Enrichissement : `[Nom, Prénom]`

### Étape 3 : Choisir les colonnes à importer
Sélectionnez les colonnes du fichier d'enrichissement que vous souhaitez ajouter à votre source.

### Étape 4 : Nommer le fichier de sortie
Modifiez le nom du fichier résultat si souhaité.

### Étape 5 : Lancer la fusion
Cliquez sur **"🚀 Lancer la fusion"** et téléchargez votre fichier résultat.

## 🔧 Caractéristiques techniques

- **Framework** : Streamlit (interface web Python)
- **Traitement données** : Pandas
- **Format entrée** : Excel (.xlsx)
- **Format sortie** : Excel (.xlsx)
- **Type de fusion** : LEFT JOIN sur clé composée
- **Normalisation** : Minuscules, suppression espaces et retours à la ligne

## 📦 Dépendances

```
streamlit>=1.28.0
pandas>=2.0.0
openpyxl>=3.10.0
```

Voir `requirements.txt` pour plus de détails.

## 🛠️ Déploiement sur Streamlit Cloud

1. **Pushez sur GitHub**
   ```bash
   git push origin main
   ```

2. **Allez sur** https://share.streamlit.io/

3. **Connectez votre dépôt**
   - GitHub repo : `votre-username/excel-fusion-tool`
   - Branch : `main`
   - Main file path : `app.py`

4. **Déployez** - L'application sera en ligne en quelques secondes !

## 💡 Conseils d'utilisation

- **Formats de données** : Assurez-vous que vos clés de fusion sont cohérentes (ex: les noms dans les deux fichiers doivent être identiques ou convertibles)
- **Fichiers volumineux** : L'outil fonctionne mieux avec des fichiers < 50 MB
- **Doublons** : Les doublons dans le fichier d'enrichissement sont supprimés (seule la première occurrence est gardée)

## 🐛 Troubleshooting

**Problème** : "Veuillez sélectionner le même nombre de colonnes"  
**Solution** : Vérifiez que vous avez sélectionné exactement le même nombre de colonnes des deux côtés.

**Problème** : Certaines lignes ne sont pas enrichies  
**Solution** : Les clés de fusion doivent correspondre exactement. Vérifiez l'orthographe et les espaces.

**Problème** : Erreur lors de la lecture du fichier  
**Solution** : Assurez-vous que vos fichiers sont au format .xlsx (pas .xls ou .csv)

## 📄 Exemple d'utilisation

**Fichier source (base.xlsx)**
| Nom | Prénom | Âge |
|-----|--------|-----|
| Dupont | Jean | 35 |
| Martin | Sophie | 28 |

**Fichier enrichissement (enrich.xlsx)**
| Nom | Prénom | Département | Salaire |
|-----|--------|-------------|---------|
| Dupont | Jean | Ventes | 45000 |
| Martin | Sophie | IT | 55000 |

**Résultat (base_enrichi.xlsx)**
| Nom | Prénom | Âge | Département | Salaire |
|-----|--------|-----|-------------|---------|
| Dupont | Jean | 35 | Ventes | 45000 |
| Martin | Sophie | 28 | IT | 55000 |

## 📧 Support

Pour toute question ou bug, veuillez ouvrir une issue sur GitHub.

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier LICENSE pour plus de détails.

---

**Développé avec ❤️ en utilisant Streamlit**
