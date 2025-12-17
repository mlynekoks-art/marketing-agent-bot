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

# Marketing prompts
MARKETING_PROMPTS = {
    'post': """Jesteś ekspertem od marketingu w social media. Stwórz angażujący post na podstawie podanego tematu.
    
Post powinien:
- Być krótki i chwytliwy (max 280 znaków dla Twitter, max 2200 dla innych platform)
- Zawierać emocjonalny hook
- Mieć jasne CTA (call to action)
- Używać odpowiednich emoji
- Być zoptymalizowany pod engagement

Temat: {topic}
Platforma: {platform}
Ton: {tone}""",

    'caption': """Stwórz idealny opis do zdjęcia/filmu na Instagram/TikTok.

Opis powinien:
- Być kreatywny i przyciągający uwagę
- Zawierać 5-10 relevantnych hashtagów
- Mieć storytelling element
- Zachęcać do interakcji
- Pasować do contentu wizualnego

Temat/Opis contentu: {topic}
Platforma: {platform}""",

    'thread': """Stwórz angażujący thread na Twitter/X (seria połączonych postów).

Thread powinien:
- Składać się z 5-8 tweetów
- Każdy tweet max 280 znaków
- Pierwszy tweet = hook (przyciąga uwagę)
- Środkowe tweety = wartość/edukacja
- Ostatni tweet = CTA + zachęta do RT
- Numeracja: 1/8, 2/8, etc.

Temat: {topic}""",

    'ad': """Stwórz przekonującą reklamę/ad copy.

Reklama powinna:
- Mieć silny headline (nagłówek)
- Pokazywać korzyści (nie tylko features)
- Adresować pain points
- Mieć jasne CTA
- Być zgodna z AIDA (Attention, Interest, Desire, Action)

Produkt/Usługa: {topic}
Target audience: {audience}
Platforma: {platform}""",

    'email': """Napisz profesjonalny email marketingowy.

Email powinien:
- Mieć chwytliwy subject line
- Personalizowany greeting
- Jasną wartość dla odbiorcy
- Storytelling lub case study
- Silne CTA
- PS z dodatkową zachętą

Temat/Oferta: {topic}
Cel: {goal}""",

    'script': """Napisz skrypt do krótkiego filmu marketingowego (15-60 sekund).

Skrypt powinien zawierać:
- Hook (pierwsze 3 sekundy)
- Problem/Pain point
- Rozwiązanie (produkt/usługa)
- Korzyści
- CTA
- Wskazówki wizualne

Temat: {topic}
Długość: {duration} sekund
Platforma: {platform}"""
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /start is issued."""
    welcome_message = """
🤖 Witaj w Marketing Agent Bot!

Jestem AI-powered asystentem marketingowym napędzanym przez Gemini 3 Pro.

📝 Mogę pomóc Ci w:
✅ Tworzeniu treści marketingowych
✅ Generowaniu postów na social media
✅ Pisaniu opisów i captionów
✅ Tworzeniu threadów i reklam
✅ Pisaniu emaili marketingowych
✅ Tworzeniu skryptów do filmów

🎯 Dostępne komendy:
/post - Generuj post na social media
/caption - Stwórz opis do zdjęcia/filmu
/thread - Wygeneruj thread (seria postów)
/ad - Stwórz reklamę
/email - Napisz email marketingowy
/script - Stwórz skrypt do filmu
/help - Pokaż pomoc

💬 Możesz też po prostu napisać do mnie naturalnie, a ja zrozumiem Twoją intencję!

Gotowy do tworzenia? 🚀
"""
    await update.message.reply_text(welcome_message)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when the command /help is issued."""
    help_text = """
📚 Jak używać Marketing Agent Bot:

🎯 KOMENDY SPECJALISTYCZNE:

/post <temat> - Generuj post
Przykład: /post Nowy produkt eco-friendly

/caption <opis> - Opis do zdjęcia/filmu
Przykład: /caption Zachód słońca nad morzem

/thread <temat> - Thread (seria postów)
Przykład: /thread 10 tips na produktywność

/ad <produkt> - Reklama
Przykład: /ad Kurs online marketingu

/email <temat> - Email marketingowy
Przykład: /email Promocja Black Friday

/script <temat> - Skrypt do filmu
Przykład: /script Prezentacja nowego produktu

/image <opis> - Prompt do generowania obrazu AI
Przykład: /image Nowoczesne logo firmy tech

💬 NATURALNA KONWERSACJA:
Możesz też po prostu napisać:
- "Stwórz post o kawie"
- "Potrzebuję opisu do zdjęcia"
- "Napisz reklamę mojego produktu"

🎨 OPCJE DODATKOWE:
Możesz dodać szczegóły jak:
- Platforma (Instagram, Twitter, LinkedIn, TikTok)
- Ton (profesjonalny, casualowy, humorystyczny)
- Długość (krótki, średni, długi)
- Target audience (młodzież, profesjonaliści, etc.)

Przykład: /post Nowy produkt | Instagram | casualowy | młodzież

Gotowy? Zacznijmy! 🚀
"""
    await update.message.reply_text(help_text)

async def generate_post(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Generate social media post"""
    if not context.args:
        await update.message.reply_text("❌ Podaj temat posta!\nPrzykład: /post Nowy produkt eco-friendly")
        return
    
    topic = ' '.join(context.args)
    await update.message.reply_text("✍️ Tworzę post... Chwilę!")
    
    # Parse additional parameters
    parts = topic.split('|')
    main_topic = parts[0].strip()
    platform = parts[1].strip() if len(parts) > 1 else "Instagram"
    tone = parts[2].strip() if len(parts) > 2 else "profesjonalny"
    
    prompt = MARKETING_PROMPTS['post'].format(
        topic=main_topic,
        platform=platform,
        tone=tone
    )
    
    try:
        response = model.generate_content(prompt)
        await update.message.reply_text(f"📱 Post ({platform}):\n\n{response.text}")
    except Exception as e:
        logger.error(f"Error generating post: {e}")
        await update.message.reply_text("❌ Wystąpił błąd podczas generowania posta. Spróbuj ponownie!")

async def generate_caption(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Generate caption for image/video"""
    if not context.args:
        await update.message.reply_text("❌ Opisz content!\nPrzykład: /caption Zachód słońca nad morzem")
        return
    
    topic = ' '.join(context.args)
    await update.message.reply_text("✍️ Tworzę caption... Chwilę!")
    
    parts = topic.split('|')
    main_topic = parts[0].strip()
    platform = parts[1].strip() if len(parts) > 1 else "Instagram"
    
    prompt = MARKETING_PROMPTS['caption'].format(
        topic=main_topic,
        platform=platform
    )
    
    try:
        response = model.generate_content(prompt)
        await update.message.reply_text(f"📸 Caption ({platform}):\n\n{response.text}")
    except Exception as e:
        logger.error(f"Error generating caption: {e}")
        await update.message.reply_text("❌ Wystąpił błąd podczas generowania caption. Spróbuj ponownie!")

async def generate_thread(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Generate Twitter/X thread"""
    if not context.args:
        await update.message.reply_text("❌ Podaj temat threada!\nPrzykład: /thread 10 tips na produktywność")
        return
    
    topic = ' '.join(context.args)
    await update.message.reply_text("✍️ Tworzę thread... To może chwilę potrwać!")
    
    prompt = MARKETING_PROMPTS['thread'].format(topic=topic)
    
    try:
        response = model.generate_content(prompt)
        await update.message.reply_text(f"🧵 Thread:\n\n{response.text}")
    except Exception as e:
        logger.error(f"Error generating thread: {e}")
        await update.message.reply_text("❌ Wystąpił błąd podczas generowania threada. Spróbuj ponownie!")

async def generate_ad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Generate advertisement copy"""
    if not context.args:
        await update.message.reply_text("❌ Opisz produkt/usługę!\nPrzykład: /ad Kurs online marketingu")
        return
    
    topic = ' '.join(context.args)
    await update.message.reply_text("✍️ Tworzę reklamę... Chwilę!")
    
    parts = topic.split('|')
    main_topic = parts[0].strip()
    audience = parts[1].strip() if len(parts) > 1 else "ogólna"
    platform = parts[2].strip() if len(parts) > 2 else "Facebook"
    
    prompt = MARKETING_PROMPTS['ad'].format(
        topic=main_topic,
        audience=audience,
        platform=platform
    )
    
    try:
        response = model.generate_content(prompt)
        await update.message.reply_text(f"📢 Reklama ({platform}):\n\n{response.text}")
    except Exception as e:
        logger.error(f"Error generating ad: {e}")
        await update.message.reply_text("❌ Wystąpił błąd podczas generowania reklamy. Spróbuj ponownie!")

async def generate_email(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Generate marketing email"""
    if not context.args:
        await update.message.reply_text("❌ Podaj temat emaila!\nPrzykład: /email Promocja Black Friday")
        return
    
    topic = ' '.join(context.args)
    await update.message.reply_text("✍️ Piszę email... Chwilę!")
    
    parts = topic.split('|')
    main_topic = parts[0].strip()
    goal = parts[1].strip() if len(parts) > 1 else "sprzedaż"
    
    prompt = MARKETING_PROMPTS['email'].format(
        topic=main_topic,
        goal=goal
    )
    
    try:
        response = model.generate_content(prompt)
        await update.message.reply_text(f"📧 Email marketingowy:\n\n{response.text}")
    except Exception as e:
        logger.error(f"Error generating email: {e}")
        await update.message.reply_text("❌ Wystąpił błąd podczas generowania emaila. Spróbuj ponownie!")

async def generate_script(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Generate video script"""
    if not context.args:
        await update.message.reply_text("❌ Podaj temat filmu!\nPrzykład: /script Prezentacja nowego produktu")
        return
    
    topic = ' '.join(context.args)
    await update.message.reply_text("✍️ Tworzę skrypt... Chwilę!")
    
    parts = topic.split('|')
    main_topic = parts[0].strip()
    duration = parts[1].strip() if len(parts) > 1 else "30"
    platform = parts[2].strip() if len(parts) > 2 else "TikTok"
    
    prompt = MARKETING_PROMPTS['script'].format(
        topic=main_topic,
        duration=duration,
        platform=platform
    )
    
    try:
        response = model.generate_content(prompt)
        await update.message.reply_text(f"🎬 Skrypt ({duration}s, {platform}):\n\n{response.text}")
    except Exception as e:
        logger.error(f"Error generating script: {e}")
        await update.message.reply_text("❌ Wystąpił błąd podczas generowania skryptu. Spróbuj ponownie!")

async def generate_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Generate image using AI (placeholder for future integration)"""
    if not context.args:
        await update.message.reply_text("❌ Podaj opis obrazu!\nPrzykład: /image Nowoczesny design logo dla firmy tech")
        return
    
    description = ' '.join(context.args)
    await update.message.reply_text(f"🎨 Generuję obraz: {description}...")
    
    # Note: Gemini 3 Pro doesn't have built-in image generation
    # This would require integration with:
    # - Google Imagen 3 API
    # - DALL-E 3 API (OpenAI)
    # - Stable Diffusion API
    # - Midjourney API
    
    prompt = f"""Stwórz szczegółowy prompt do generowania obrazu AI dla: {description}

Uwzględnij:
- Styl wizualny i estetykę
- Kolory i nastrój
- Kompozycję i perspektywę
- Szczegóły techniczne (rozdzielczość, format)
- Słowa kluczowe dla AI image generator

Prompt powinien być w języku angielskim, szczegółowy i zoptymalizowany pod generatory obrazów AI."""

    try:
        response = model.generate_content(prompt)
        result = f"🎨 **Prompt do generowania obrazu:**\n\n{response.text}\n\n"
        result += "ℹ️ **Jak użyć:**\n"
        result += "1. Skopiuj powyższy prompt\n"
        result += "2. Wklej do generatora AI (DALL-E, Midjourney, Stable Diffusion)\n"
        result += "3. Dostosuj parametry według potrzeb\n\n"
        result += "💡 **Polecane narzędzia:**\n"
        result += "• DALL-E 3 (OpenAI)\n"
        result += "• Midjourney\n"
        result += "• Stable Diffusion\n"
        result += "• Google Imagen 3"
        
        await update.message.reply_text(result)
    except Exception as e:
        logger.error(f"Error generating image prompt: {e}")
        await update.message.reply_text("❌ Wystąpił błąd podczas generowania promptu. Spróbuj ponownie!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle natural language messages"""
    user_message = update.message.text
    logger.info(f"User message: {user_message}")
    
    # Analyze intent and generate response
    intent_prompt = f"""Jesteś asystentem marketingowym. Użytkownik napisał: "{user_message}"

Przeanalizuj intencję i odpowiedz pomocnie. Jeśli użytkownik chce:
- Stworzyć post/content  wygeneruj go
- Zadać pytanie o marketing  odpowiedz merytorycznie
- Poprosić o pomoc  zasugeruj odpowiednie komendy

Odpowiedz naturalnie i pomocnie po polsku."""
    
    try:
        response = model.generate_content(intent_prompt)
        await update.message.reply_text(response.text)
    except Exception as e:
        logger.error(f"Error handling message: {e}")
        await update.message.reply_text("❌ Przepraszam, wystąpił błąd. Spróbuj użyć konkretnej komendy jak /post lub /help")

def main():
    """Start the bot"""
    # Create application
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("post", generate_post))
    application.add_handler(CommandHandler("caption", generate_caption))
    application.add_handler(CommandHandler("thread", generate_thread))
    application.add_handler(CommandHandler("ad", generate_ad))
    application.add_handler(CommandHandler("email", generate_email))
    application.add_handler(CommandHandler("script", generate_script)
                               application.add_handler(CommandHandler("image", generate_image)))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start bot
    logger.info("🚀 Marketing Agent Bot started!")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
