from telethon import TelegramClient, events
from telethon.tl.types import MessageMediaPhoto, MessageMediaDocument

api_id = 21235409
api_hash = 'e20d5d2975a85d484d7fb030e6cbf437'

SOURCE_CHAT = -1002759525337
TARGET_CHAT = -1002724331058

client = TelegramClient('forward_bot_session', api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def forward(event):
    msg = event.message

    # টেক্সট মেসেজ হলে
    if msg.text:
        await client.send_message(TARGET_CHAT, msg.text)
    
    # ছবি/ডকুমেন্ট হলে
    elif msg.media:
        await client.send_file(TARGET_CHAT, msg.media, caption=msg.text or "")
    
    # অন্য যেকোনো মেসেজ হলে (অডিও, ভিডিও, স্টিকার ইত্যাদি)
    else:
        await client.send_message(TARGET_CHAT, "Unsupported message type")

    print(f"Copied message id {msg.id} without forward header")

async def main():
    await client.start()
    print("User Bot চলছে...")
    await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
