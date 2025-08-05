from telethon import TelegramClient, events

api_id = 21235409
api_hash = 'e20d5d2975a85d484d7fb030e6cbf437'

SOURCE_CHAT = -1002825701159   # সোর্স গ্রুপ আইডি
TARGET_CHAT = -1002899324768       # টার্গেট গ্রুপ/চ্যানেল আইডি

client = TelegramClient('forward_bot_session', api_id, api_hash)

@client.on(events.NewMessage(chats=SOURCE_CHAT))
async def forward(event):
    await event.forward_to(TARGET_CHAT)
    print(f"Forwarded message id {event.message.id}")

async def main():
    print("NeW Bot STARTed😁😁✅...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())