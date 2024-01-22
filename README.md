# Gladiatorzy Hazardu
Witamy na repozytorium naszego projektu z PWI

## Przed uruchamieniem

Zainstaluj wymagane pakiety

```bash
sudo apt install python3
pip install -r requirements.txt
```

## Uruchamianie serwera

1. Zmień domyślne ustawienia serwera

    W pliku config.py zmień host na IP serwera i port na dowolny wybrany.

2. Uruchom serwer
   
   ```bash
   python3 server.py
   ```
**Upewnij się, że jakiś serwer jest już postawiony, bo inaczej klient nie uruchomi się przez brak połączenia!**

## Uruchamianie gry
   
   ```bash
   python3 main.py
   ```