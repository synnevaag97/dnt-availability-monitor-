
# 🏕️ DNT Bed Checker

**Automatisert overvåkning av sengeplasser på DNT-hytter**

Dette prosjektet sjekker tilgjengelighet for sengeplasser på en spesifikk DNT-hytte (f.eks. Katnosdammen) ved hjelp av DNTs offentlige API. Når det er nok ledige plasser, sendes det automatisk en e-postvarsling til en forhåndsdefinert mottaker.

## 🚀 Funksjoner
- Henter data fra DNTs booking-API
- Sjekker om antall ledige sengeplasser overstiger et minimumskrav
- Sender e-postvarsel ved tilgjengelighet
- Kjører kontinuerlig med intervallbasert sjekk (default: hvert 5. minutt)

## 🔧 Teknologi
- Python 3
- `requests` for API-kall
- `smtplib` for e-post
- `email.mime` for e-postformatering

## 📦 Bruksområder
- Automatisk varsling for populære hytter
- Personlig assistent for booking
- Kan utvides til flere hytter eller datoer

## ⚙️ Konfigurasjon
Du kan enkelt endre:
- Hytte-ID (`CABIN_ID`)
- Datoer (`FROM_DATE`, `TO_DATE`)
- Antall ønskede sengeplasser (`REQUIRED_BEDS`)
- E-postinnstillinger (`EMAIL_USER`, `EMAIL_PASSWORD`, `TO_EMAIL`)

## 📄 Bruk
```bash
python main.py
