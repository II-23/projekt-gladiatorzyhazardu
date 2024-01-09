# Gladiatorzy Hazardu
Witamy na repozytorium naszego projektu z PWI

## Uruchamianie serwera

1. Zainstaluj wymagane pakiety
   ```bash
   sudo apt install python3
   pip install -r requirements.txt
   ``` 

2. Zmień domyślne ustawienia serwera

    W pliku config.py zmień host na IP serwera i port na dowolny wybrany.

2. Uruchom serwer
   ```bash
   python3 server.py
   ```

## Uruchamianie clienta

Na ten moment nie ma dokładnego połączenia pomiędzy GUI oraz 
kodem logiki, wiec narazie aby uruchomić client po prostu:

```bash
python3 client.py
```