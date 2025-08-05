from telethon import TelegramClient, events
import asyncio
import os

api_id = 21235409
api_hash = 'e20d5d2975a85d484d7fb030e6cbf437'

SOURCE_CHAT = -1002759525337
TARGET_CHAT = -1002890422217

SESSION_NAME = "forward_bot_session"  # সেশন ফাইল এখানে সেভ হবে (forward_bot_session.session)

client = TelegramClient(SESSION_NAME, api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def forward_handler(event):
    try:
        msg = event.message
        if msg.text:
            await client.send_message(TARGET_CHAT, msg.text)
            print(f"✅ Forwarded: {msg.text[:50]}")
        else:
            print("⏭ Skipped non-text message.")
    except Exception as e:
        print("❌ Forward failed:", e)

async def main():
    # প্রথমবার লগইন করতে হবে
    if not os.path.exists(f"{SESSION_NAME}.session"):
        phone = input("📱 Enter phone number (e.g. +8801xxxxxxxxx): ")
        await client.start(phone=phone)
        print("✅ Session saved. Next time no need to login!")
    else:
        await client.start()
        print("🔓 Logged in using saved session.")

    print("🚀 Bot running (text-only forward mode)...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())