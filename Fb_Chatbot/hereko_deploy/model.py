from flask import Flask,request
from pymessenger.bot import Bot

app = Flask("hello")

VERIFY_TOKEN = "1234567890"
ACCESS_TOKEN = "EAAoY5bXvl7IBAHG0gzPBlHAw5PIfdZC5ZBuP6Eyz3blBD1ZC0FiV560H2Mn8erU2ArNxlvQQCXHkpFXvZCm5aYZCVvvwZBWe9sZBGRpz1mcMkZCHzQg0ivh6EM4agzkYqDHQZBR4YbPUbjw15ZA2GolE26t0evruPca4MsoyqRREuujKT4PdEl6Yqq"

pybot = Bot(ACCESS_TOKEN)


@app.route("/check/", methods=["GET"])
def sayhi():
    return "working"


@app.route("/callback/", methods=["GET"])
def get_callback():
    if VERIFY_TOKEN == request.args.get("hub.verify_token"):
        return request.args.get("hub.challenge")
    else:
        return "not-working"


@app.route("/callback/", methods=["POST"])
def post_callback():
    output = request.get_json()

    for entry in output.get("entry"):
        if "messaging" in entry:
            for messaging in entry.get("messaging"):
                sender = messaging.get("sender").get("id")
                recipient = messaging.get("recipient").get("id")

                text = "You sent an attachment"

                if "text" in messaging.get("message"):
                    text = messaging.get("message").get("text")
                print(sender, recipient, text)

                pybot.send_text_message(sender, text)

    return "done"
app.run()