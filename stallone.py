# Autore: christacce
# Creazione: 2025-03-15
# Versione: 1.0
# Lingua: Python
# Piattaforma: Python 3.9.6
# Dipendenze: telethon, schedule
# Descrizione: Script per inviare messaggi a gruppi Telegram tramite bot.

import asyncio
import schedule
from datetime import datetime
from telethon import TelegramClient

# --- INSERISCI QUI LE TUE CREDENZIALI ---
api_id = "INSERIRE IL TUO API_ID"  # Sostituisci con il tuo API ID
api_hash = "INSERIRE IL TUO API_HASH"  # Sostituisci con il tuo API Hash
chat_id = 1001520340812  # ID del gruppo, canale o tra virgolette "" per i contatti. Già inserito il gruppo degli Stalloni

# Crea il client
client = TelegramClient("stallone", api_id, api_hash) # Nome del file di sessione

# Funzione per inviare il messaggio
async def send_message():
    await client.send_message(chat_id, "stallone")
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Messaggio inviato!")

# Pianifica l'invio a mezzanotte e 32 secondi
def job():
    # Quando scatta il programma, chiama la funzione asincrona
    asyncio.create_task(send_message())

# Funzione che esegue il loop di schedule
async def scheduler():
    # Usa asyncio per il loop, in modo che possiate gestire `schedule` e `asyncio` insieme
    while True:
        schedule.run_pending()  # Esegui i job pianificati
        await asyncio.sleep(1)  # Fai dormire il ciclo per un po'

# Avvia il bot
async def main():
    try:
        print("Benvenuto nel bot Stallone creato da Christacce.\n\nInizio connessione al client...")
        async with client:
            # Verifica se il client è già autorizzato
            if not await client.is_user_authorized():
                print("Autenticazione necessaria...")
                await client.start()  # Avvia l'autenticazione
                print("Autenticato con successo!")
            
            print("Bot avviato e in attesa...")
            # Pianifica l'invio del messaggio. Ogni 5 secondi da mezzanotte.
            schedule.every().day.at("00:00:00").do(job)
            schedule.every().day.at("00:00:05").do(job)
            schedule.every().day.at("00:00:10").do(job)
            schedule.every().day.at("00:00:15").do(job)
            
            await scheduler()  # Inizia il ciclo di pianificazione
    except Exception as e:
        print(f"Errore di connessione: {e}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
