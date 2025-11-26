# 📦 Guide de Déploiement Vercel

## Méthode 1 : Via GitHub (RECOMMANDÉ) ⭐

### Étape 1 : Créer un repo GitHub

1. Va sur https://github.com/new
2. Nom du repo : `polymarket-finder`
3. Public ou Private (ton choix)
4. Crée le repo

### Étape 2 : Push le code

```bash
cd polymarket-vercel-final

git init
git add .
git commit -m "Initial commit - Polymarket Finder"
git branch -M main
git remote add origin https://github.com/TON_USERNAME/polymarket-finder.git
git push -u origin main
```

### Étape 3 : Déployer sur Vercel

1. Va sur https://vercel.com
2. Connecte-toi avec GitHub
3. Clique "Add New..." → "Project"
4. Sélectionne ton repo `polymarket-finder`
5. Vercel détecte automatiquement la config
6. Clique "Deploy" 🚀
7. Attends 1-2 minutes

✅ **C'est en ligne !** Ton URL : `https://polymarket-finder.vercel.app`

---

## Méthode 2 : Via Vercel CLI

### Installation

```bash
npm install -g vercel
```

### Déploiement

```bash
cd polymarket-vercel-final
vercel login
vercel
```

Réponds aux questions :
- Set up and develop? **Y**
- Which scope? (choisis ton compte)
- Link to existing project? **N**
- What's your project's name? `polymarket-finder`
- In which directory? `./` (appuie sur Enter)

Vercel va déployer et te donner l'URL !

---

## Test Local Avant Déploiement

```bash
vercel dev
```

Ouvre http://localhost:3000

---

## Mettre à Jour le Site

### Si déployé via GitHub :

```bash
git add .
git commit -m "Update: description du changement"
git push
```

Vercel redéploie automatiquement ! ✨

### Si déployé via CLI :

```bash
vercel --prod
```

---

## Custom Domain (Optionnel)

1. Va dans ton projet sur vercel.com
2. Settings → Domains
3. Ajoute ton domaine custom
4. Configure les DNS selon les instructions

---

## Vérifier que ça Marche

Ton site devrait :
- ✅ Charger les marchés Polymarket
- ✅ Afficher les filtres
- ✅ Permettre de cliquer sur les marchés
- ✅ Être responsive sur mobile

---

## Dépannage

### "No markets found"
- Vérifie que l'API `/api/markets` retourne des données
- Va sur `https://ton-site.vercel.app/api/markets`
- Tu devrais voir du JSON

### Erreur de build
- Vérifie que tous les fichiers sont présents :
  - index.html
  - api/markets.py
  - vercel.json
  - requirements.txt

### L'API ne marche pas
- Les logs sont dans : Vercel Dashboard → ton projet → Logs
- Vérifie les erreurs Python

---

## 🎉 Fini !

Une fois déployé, partage ton lien :
`https://polymarket-finder.vercel.app`

Ton site est maintenant live et accessible mondialement ! 🌍
