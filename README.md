# Movie Recc

Movie Recc è un sistema di raccomandazione progettato per consigliare film sulla base del profilo di personalità dell’utente, determinato tramite il test **Big Five Personality Inventory (BFI)**.

Il sistema si basa sul concetto di similarità tra utenti e film, combinando due fattori principali:

1. **Profilo di personalità dell’utente** – derivato dalle risposte al quiz Big Five.
2. **Preferenze espresse durante la selezione dei film** – l’utente sceglie film che gli piacciono (Sì/No) e il sistema apprende dai feedback.

Il database utilizzato è il **MovieLens 20M Dataset**, disponibile su Kaggle: [MovieLens 20M Dataset](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset)

In particolare, i file usati sono: `movies.csv` e `ratings.csv`.

---

## Metodo di raccomandazione

1. L’utente compila il quiz Big Five, generando un **profilo psicologico**.
2. Il sistema calcola la **similarità di personalità** tra l’utente e tutti gli altri utenti presenti nel dataset.
3. Viene generata una lista iniziale di film da proporre all’utente per feedback (Sì/No).
4. Dopo la selezione di **5 film che piacciono all’utente**, il sistema crea una lista finale di **10 raccomandazioni** basata sia sulla personalità che sui generi dei film scelti.

---

* I dati dell’utente vengono salvati localmente nei file `output/profilo_utente.json`, `output/final_recommendations.csv` e `output/feedback.csv`.
* Non è richiesta alcuna registrazione o invio dati online.
