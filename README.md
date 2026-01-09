# SB_GymTracker
Super Basic Gym Tracker

En enkel och lättanvänd webbapplikation för att hålla koll på dina träningspass.

## Funktioner

- ✅ Lägg till träningspass med övning, set, reps och vikt
- 📊 Visa träningshistorik sorterad efter datum
- 💾 Data sparas lokalt i webbläsaren (localStorage)
- 🗑️ Ta bort enskilda träningspass eller rensa alla
- 📱 Responsiv design som fungerar på mobil och desktop

## Hur man använder

1. Öppna `index.html` i din webbläsare
2. Fyll i formuläret med ditt träningspass:
   - Övning (t.ex. Bänkpress, Knäböj)
   - Antal set
   - Antal repetitioner
   - Vikt (valfritt - lämna tomt för kroppsviktsövningar)
   - Datum
3. Klicka på "Lägg till" för att spara träningspasset
4. Din träningshistorik visas nedanför formuläret

## Installation

Ingen installation krävs! Detta är en helt klientbaserad applikation.

1. Klona eller ladda ner detta repository
2. Öppna `index.html` i din webbläsare

Eller använd en enkel webbserver:
```bash
# Med Python 3
python -m http.server 8000

# Med Node.js (npx)
npx http-server
```

Öppna sedan http://localhost:8000 i din webbläsare.

## Filer

- `index.html` - Huvudsidan med HTML-struktur
- `style.css` - Styling och layout
- `app.js` - JavaScript-logik för data och interaktion

## Datalagring

All data sparas lokalt i din webbläsares localStorage. Ingen data skickas till någon server.

## Teknologi

- HTML5
- CSS3
- Vanilla JavaScript
- LocalStorage API
