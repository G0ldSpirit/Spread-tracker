# 🔐 Guide de Configuration Sécurisée

## Étape 1 : Push le code sur GitHub

```bash
cd polymarket-spreads-secure

git init
git add .
git commit -m "Initial commit - Polymarket Real Spreads"
git branch -M main
git remote add origin https://github.com/TON_USERNAME/polymarket-spreads.git
git push -u origin main
```

⚠️ **Remplace `TON_USERNAME`** par ton vrai username GitHub !

---

## Étape 2 : Déployer sur Vercel

1. Va sur **https://vercel.com**
2. Clique **"Add New..."** → **"Project"**
3. Sélectionne ton repo **`polymarket-spreads`**
4. **AVANT de cliquer Deploy**, va dans **"Environment Variables"**

---

## Étape 3 : Ajouter les Variables d'Environnement 🔑

### Dans la section "Environment Variables" sur Vercel :

Ajoute ces 3 variables (une par une) :

#### Variable 1 :
- **Name:** `POLYMARKET_API_KEY`
- **Value:** Colle ton API Key (ex: `12345678-1234-5678-9abc-123456789012`)
- **Environment:** Production, Preview, Development (coche les 3)

#### Variable 2 :
- **Name:** `POLYMARKET_API_SECRET`
- **Value:** Colle ton Secret (ex: `Lxxxxxxxxxxx...`)
- **Environment:** Production, Preview, Development (coche les 3)

#### Variable 3 :
- **Name:** `POLYMARKET_API_PASSPHRASE`
- **Value:** Colle ton Passphrase (ex: `dxxxxxxxxxxx...`)
- **Environment:** Production, Preview, Development (coche les 3)

---

## Étape 4 : Déployer !

Une fois les 3 variables ajoutées :

1. Clique **"Deploy"** 🚀
2. Attends 2-3 minutes
3. Ton site sera en ligne avec les VRAIS spreads !

---

## 🎯 Résultat

Tu auras un site qui affiche :
- ✅ **Vrais spreads bid/ask** depuis les order books
- ✅ **Prix Bid et Ask** pour YES et NO
- ✅ **Top 30 marchés** par volume
- ✅ **Credentials 100% sécurisés** (pas dans le code)

---

## 🔄 Mettre à Jour

Pour mettre à jour ton site :

```bash
git add .
git commit -m "Update: description"
git push
```

Vercel redéploiera automatiquement !

---

## 🛡️ Sécurité

✅ Tes credentials ne sont **JAMAIS** dans le code GitHub  
✅ Seul Vercel a accès aux variables d'environnement  
✅ Personne ne peut voir tes API keys  

---

## ⚠️ Important

**NE PARTAGE JAMAIS** tes credentials :
- API Key
- Secret
- Passphrase

Si quelqu'un les obtient, il peut trader avec ton compte !

---

## 🎉 C'est Tout !

Une fois déployé, ton site affichera les vrais spreads Polymarket !
