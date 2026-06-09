# TypingDemo

Simula la digitazione in tempo reale durante le demo — scrivi un trigger breve e il testo appare carattere per carattere, come se lo stessi digitando tu.

Funziona in qualsiasi app: Slack, browser, Teams, PowerPoint, ecc.

---

## ⬇️ Download

**[Scarica l'ultima versione (ZIP)](https://github.com/bojanfaz-code/TypingDemo/archive/refs/heads/main.zip)**

oppure clona il repository:
```bash
git clone https://github.com/bojanfaz-code/TypingDemo.git
```

---

## Requisiti

- macOS (10.15 Catalina o successivo)
- Python 3 (già incluso su macOS, oppure da [python.org](https://www.python.org/downloads/))
- Google Chrome (per l'interfaccia di gestione snippet)

---

## Installazione rapida

1. Scarica e decomprimi lo ZIP (link sopra)
2. Doppio click su **`INSTALLA.command`**
3. Segui le istruzioni a schermo per il permesso Accessibilità
4. Apri **`GUIDA.html`** con Chrome per la guida completa

> ⚠️ Il permesso Accessibilità è obbligatorio. Senza di esso lo script non può simulare la tastiera.

---

## Utilizzo

**Prima della demo:** doppio click su `avvia.command` e minimizza la finestra.

**Durante la demo:** digita il trigger (es. `/1`) in qualsiasi campo testo — lo script lo sostituisce con il testo completo, carattere per carattere.

---

## Gestione snippet

Apri `gestisci_snippet.html` con Chrome per aggiungere, modificare o eliminare snippet tramite interfaccia grafica. Salva con ⌘S.

Il file `snippets.json` contiene la configurazione (snippet + impostazioni velocità).

---

## Struttura file

| File | Descrizione |
|------|-------------|
| `INSTALLA.command` | Installer automatico — eseguire una sola volta |
| `avvia.command` | Avvia lo script — eseguire prima di ogni demo |
| `gestisci_snippet.html` | Interfaccia grafica per gestire gli snippet |
| `GUIDA.html` | Guida visiva step-by-step |
| `typing_demo.py` | Script principale (non modificare) |
| `snippets.json` | Configurazione snippet e impostazioni |
