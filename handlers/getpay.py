from telethon import events
from main import bot

@bot.on(events.NewMessage(pattern=r"^\.getpay$", outgoing=True))
async def getpay(event):
    PREMIUM_EMOJI_1 = "<emoji id=5347619282938478291>"  # Ganti dengan ID pertama
    PREMIUM_EMOJI_2 = "<emoji id=8473629183746251928>"  # Ganti dengan ID kedua
    PREMIUM_EMOJI_3 = "<emoji id=9283746572918374652>"  # Ganti dengan ID ketiga

    message = (
        f"{PREMIUM_EMOJI_1} **Pembayaran dapat dilakukan melalui:**\n\n"
        f"{PREMIUM_EMOJI_2} **Metode Pembayaran:**\n"
        "1. Bank Transfer (BCA, Mandiri, dll.)\n"
        "2. E-Wallet (GoPay, OVO, Dana, dll.)\n"
        "3. Pulsa (Telkomsel, XL, dll.)\n\n"
        f"{PREMIUM_EMOJI_3} **Silakan hubungi admin untuk info lebih lanjut.**"
    )
    
    await event.reply(message, parse_mode="html")
    