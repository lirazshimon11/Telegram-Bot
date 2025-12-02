import os
import time
import threading
from dotenv import load_dotenv
import httpx
from http.server import BaseHTTPRequestHandler, HTTPServer

# טוען משתני סביבה מקובץ .env (לשימוש מקומי). ברנדר תקבל את ה-TOKEN מה-Environment.
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise RuntimeError("TELEGRAM_TOKEN is not set")

API_URL = f"https://api.telegram.org/bot{TOKEN}"

SEPARATOR_TEXT = "אאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאאא"   # החוצץ שאתה רוצה שיופיע
TRIGGER = "."              # מה שאתה שולח כדי ליצור חוצץ

# ---------- חלק 1: בוט טלגרם באמצעות HTTP רגיל ----------

def run_bot():
    print("Bot long-polling loop started")
    offset = None

    with httpx.Client(timeout=60) as client:
        while True:
            try:
                params = {"timeout": 50}
                if offset is not None:
                    params["offset"] = offset

                # מבקש עדכונים מטלגרם
                resp = client.get(f"{API_URL}/getUpdates", params=params)
                data = resp.json()

                if not data.get("ok"):
                    print("Telegram API error:", data)
                    time.sleep(3)
                    continue

                for update in data.get("result", []):
                    offset = update["update_id"] + 1

                    message = update.get("message") or update.get("edited_message")
                    if not message:
                        continue

                    text = (message.get("text") or "").strip()
                    chat_id = message["chat"]["id"]
                    message_id = message["message_id"]

                    # אם המשתמש כתב את הטריגר (למשל ".")
                    if text == TRIGGER:
                        # שולח את החוצץ
                        client.post(
                            f"{API_URL}/sendMessage",
                            json={"chat_id": chat_id, "text": SEPARATOR_TEXT},
                        )

                        # מנסה למחוק את הודעת הטריגר
                        try:
                            client.post(
                                f"{API_URL}/deleteMessage",
                                json={"chat_id": chat_id, "message_id": message_id},
                            )
                        except Exception as e:
                            print("Failed to delete message:", e)

                # קצת מנוחה בין סיבובים
                # (יש timeout ל-getUpdates, אז זה פחות קריטי)
            except Exception as e:
                print("Error in polling loop:", e)
                time.sleep(5)


# ---------- חלק 2: שרת HTTP קטן בשביל Render ----------

class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # תשובה פשוטה כדי ש-Render יהיה מרוצה שיש "שרת"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        # לא להדפיס לוגים מיותרים
        return


def run_http_server():
    port = int(os.environ.get("PORT", "8000"))
    server_address = ("", port)
    httpd = HTTPServer(server_address, DummyHandler)
    print(f"HTTP server running on port {port} (for Render health checks)")
    httpd.serve_forever()


# ---------- main ----------

def main():
    # מפעיל את השרת HTTP בת׳רד נפרד (כדי ש-Render יראה פורט פתוח)
    http_thread = threading.Thread(target=run_http_server, daemon=True)
    http_thread.start()

    # מפעיל את לולאת הבוט (polling)
    run_bot()


if __name__ == "__main__":
    print("Starting bot + HTTP server...")
    main()