import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = os.getenv("TOKEN")

def classify(text):
    text = text.lower()
    number = ""
    explanation = []

    if "تسويق" in text or "marketing" in text:
        number = "658"
        explanation.append("658 → إدارة")
        number += ".8"
        explanation.append("658.8 → تسويق")

    if "الكتروني" in text or "digital" in text:
        number += "72"
        explanation.append("658.872 → تسويق رقمي")

    if "مصر" in text or "egypt" in text:
        number += "962"
        explanation.append(".962 → مصر")

    return number, explanation


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    number, explanation = classify(text)

    if number == "":
        reply = "❌ مش لاقي تصنيف مناسب"
    else:
        reply = f"📚 رقم ديوي: {number}\n\n"
        reply += "📖 الشرح:\n"
        for line in explanation:
            reply += f"- {line}\n"

    await update.message.reply_text(reply)


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

app.run_polling()