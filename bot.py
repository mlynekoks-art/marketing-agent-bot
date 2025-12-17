#!/usr/bin/env python3
"""
Marketing Agent Bot - AI-powered marketing assistant
Powered by Gemini 3 Pro and Telegram
"""

import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import google.generativeai as genai

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Configuration
TELEGRAM_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Initialize Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-3-pro-preview')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    welcome_message = """
🤖 Witaj w Marketing Agent Bot!

Jestem AI-powered asystentem marketingowym napędzanym przez Gemini 3 Pro.

Mogę pomóc Ci w:
📝 Tworzeniu treści marketingowych
🎨 Generowaniu pomysłów na posty
📊 Analizie strategii marketingowej
🎬 Planowaniu kampanii

Wyślij mi wiadomość, a ja Ci pomogę!
    """
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    help_text = """
📚 Dostępne komendy:

/start - Rozpocznij rozmowę
/help - Pokaż tę pomoc
/generate - Generuj treść marketingową

Po prostu napisz do mnie, a ja odpowiem używając zaawansowanej AI!
    """
    await update.message.reply_text(help_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle user messages with Gemini AI."""
    user_message = update.message.text
    user_name = update.effective_user.first_name
    
    logger.info(f"Message from {user_name}: {user_message}")
    
    try:
        # Send typing action
        await update.message.chat.send_action("typing")
        
        # Generate response with Gemini
        prompt = f"""Jesteś profesjonalnym asystentem marketingowym. 
        Użytkownik {user_name} pisze: {user_message}
        
        Odpowiedz w sposób pomocny, kreatywny i profesjonalny."""
        
        response = model.generate_content(prompt)
        
        # Send response
        await update.message.reply_text(response.text)
        
    except Exception as e:
        logger.error(f"Error generating response: {e}")
        await update.message.reply_text(
            "Przepraszam, wystąpił błąd. Spróbuj ponownie później."
        )

def main():
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the Bot
    logger.info("Starting Marketing Agent Bot...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
