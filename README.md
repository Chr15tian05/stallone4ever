# stallone4ever

# **Telegram Bot per vincere lo stallone**

## **Descrizione**
Questo script Python permette di inviare automaticamente messaggi a un gruppo o canale Telegram a una determinata ora ogni giorno. È utile per fare il cancro ma da non sfruttare per spam anche perchè venite bannati.

## **Autore**
**christacce**

## **Versione**
1.0

---

## **Prerequisiti**

- **Python 3.x** (preferibilmente la versione 3.9.6)
- **Telethon**: una libreria Python per interagire con l'API di Telegram.
- **Schedule**: una libreria Python per pianificare l'esecuzione di funzioni a orari prestabiliti.

---

## **Passaggi per configurare il bot**

### **1. Creare un'app Telegram**

1. Vai su [my.telegram.org](https://my.telegram.org).
2. Clicca su **API development tools** e accedi con il tuo numero di telefono.
3. Una volta effettuato l'accesso, vedrai la sezione **Create a new application**.
4. **Compila il modulo** con il nome della tua app e altri dettagli. Ecco un esempio:
   - **App title**: TelegramBot
   - **Short name**: TGBot
   - **URL**: Puoi lasciare vuoto.
   - **Platform**: Desktop (la piattaforma da cui si usa lo script).
5. Dopo aver creato l'app, otterrai due valori importanti: **API ID** e **API Hash**. Salvali, poiché ne avrai bisogno per configurare lo script e **NON CONDIVIDERLI CON NESSUNO PER QUALSIASI MOTIVO**.

### **2. Prepara l'ambiente Python**

1. Assicurati di avere Python 3.9 o superiore installato nel tuo sistema. Puoi scaricarlo da [python.org](https://www.python.org/).

### **3. Configura lo script**

1. **Scarica lo script** e aprilo in un editor di testo.
2. **Inserisci le tue credenziali**:
   - Trova il file `bot.py`.
   - Sostituisci i seguenti valori con quelli ottenuti dalla creazione dell'app Telegram:
     ```python
     api_id = "INSERIRE IL TUO API_ID"  # Sostituisci con il tuo API ID
     api_hash = "INSERIRE IL TUO API_HASH"  # Sostituisci con il tuo API Hash
     chat_id = INSERIRE IL TUO CHAT_ID  # Sostituisci con l'ID del tuo gruppo/canale o tra virgolette "" con l'id del contatto.
     ```

3. Salva lo script con il nome che preferisci, per esempio `stallone.py`.

### **4. Esegui lo script**

1. Apri il terminale (su Windows o Mac).
2. Naviga nella directory dove hai salvato il file `stallone.py`.
3. Esegui lo script utilizzando un **compilatore** oppure se si ha Python installato:
   ```bash
   python3 bot.py
   ```

4. **Autenticazione**:
   - Quando esegui lo script per la prima volta, il bot ti chiederà di autenticarti su Telegram.
   - Inserisci il numero di telefono associato al tuo account Telegram.
   - Riceverai un codice di verifica via SMS, che dovrai inserire nel terminale per completare l'autenticazione.

5. **Il bot è pronto per inviare messaggi**. A questo punto, il bot invierà automaticamente un messaggio al gruppo o canale Telegram con l'ID che hai configurato, all'orario specificato (in questo caso, alle 01:29:00 ogni giorno).

---

## **Struttura del Codice**

- **TelegramClient**: Crea e gestisce la connessione con l'API di Telegram.
- **Asyncio**: Utilizzato per gestire l'esecuzione asincrona dei compiti.
- **Schedule**: Gestisce la pianificazione dell'invio dei messaggi a un orario specifico.
- **Send_message()**: Funzione che invia un messaggio al gruppo o canale.
- **Job()**: Funzione che pianifica l'invio del messaggio.
- **Scheduler()**: Funzione che esegue il ciclo continuo di pianificazione dei compiti.

---

## **Modifica Orario di Invio**

Puoi cambiare l'orario di invio del messaggio modificando la seguente riga di codice nel file:
```python
schedule.every().day.at("00:00:00").do(job)  # Sostituisci con l'orario desiderato
```

Assicurati che l'orario sia nel formato `HH:MM:SS` e che il formato di 24 ore sia rispettato.

---

## **Problemi comuni**

- **Autenticazione fallita**: Se non riesci a completare l'autenticazione, assicurati di aver inserito correttamente il numero di telefono e il codice di verifica.
- **ID chat non trovato**: Se il bot non riesce a trovare l'ID della chat, verifica che il gruppo o canale sia visibile per il bot e che tu abbia l'autorizzazione per inviare messaggi.
  
