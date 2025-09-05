import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# --- KONSTANTER OG KONFIGURASJON ---
Katnosdammen_ID = 10778  # Katnosdammen
Lerbergsetra_ID = 101148967  # Lerbergsetra
CABIN_ID = Katnosdammen_ID
FROM_DATE = "2025-09-06"
TO_DATE = "2025-09-07"
REQUIRED_BEDS = 2
CHECK_INTERVAL_SECONDS = 300  # 5 minutter

URL = f"https://hyttebestilling.dnt.no/api/booking/available-price?cabinId={CABIN_ID}&fromDate={FROM_DATE}&toDate={TO_DATE}"
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0 Safari/537.36"
    )
}

# --- E-POSTINNSTILLINGER ---
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_USER = "trym.synnevag@gmail.com"
EMAIL_PASSWORD = "hqba gipt tjdm rwvn"  # App-passord for Gmail
TO_EMAIL = "trym.synnevag@gmail.com"


def send_email(subject: str, body: str) -> None:
    """
    Sender en e-post med gitt emne og innhold.
    """
    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = TO_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASSWORD)
            server.send_message(msg)
        print("📧 E-post sendt!")
    except Exception as e:
        print(f"Feil ved sending av e-post: {e}")


def fetch_available_beds() -> int:
    """
    Henter antall tilgjengelige sengeplasser fra DNT API.
    """
    try:
        response = requests.get(URL, headers=HEADERS)
        response.raise_for_status()
        data = response.json().get("data", {})

        products = data.get("productsAndPrices", [])
        total_available = sum(product.get("available", 0)
                              for product in products)

        print("🛏️ Totalt tilgjengelige senger:", total_available)
        return total_available
    except Exception as e:
        print(f"Feil ved henting av data: {e}")
        return 0


def main():
    """
    Hovedfunksjon som sjekker tilgjengelighet og sender e-post ved ledige plasser.
    """
    while True:
        available_beds = fetch_available_beds()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] Ledige plasser: {available_beds}")

        if available_beds >= REQUIRED_BEDS:
            booking_url = f"https://hyttebestilling.dnt.no/hytte/{CABIN_ID}"
            email_body = (
                f"🎉 Nå er det {available_beds} ledige plasser på Katnosdammen!\n"
                f"Bestill her: {booking_url}"
            )
            print(email_body)
            send_email("Ledige plasser på Katnosdammen", email_body)

        time.sleep(CHECK_INTERVAL_SECONDS)


if __name__ == "__main__":
    main()
