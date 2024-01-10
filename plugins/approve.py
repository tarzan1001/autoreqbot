from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserIsBlocked, PeerIdInvalid


@Client.on_chat_join_request()
async def accept_request(client, r):

    rm = InlineKeyboardMarkup([[
        InlineKeyboardButton("🎭 𝘑𝘖𝘐𝘕 𝘍𝘖𝘙 𝘔𝘖𝘝𝘐𝘌𝘚 🎭", url=f"https://t.me/OTT_ARAKAL_THERAVAD_MOVIESS")
        InlineKeyboardButton("👥 𝗚𝗥𝗢𝗨𝗣 - 𝟭", url=f"https://t.me/ARAKAL_THERAVAD_MOVIES"),
        InlineKeyboardButton("👥 𝗚𝗥𝗢𝗨𝗣 - 𝟮", url=f"https://t.me/ARAKAL_THERAVAD_GROUP_02")
        ],[
        InlineKeyboardButton("👥 𝗚𝗥𝗢𝗨𝗣 - 𝟯", url=f"https://t.me/ARAKAL_THERAVAD_GROUP_03"),
        InlineKeyboardButton("👥 𝗚𝗥𝗢𝗨𝗣 - 𝟰", url=f"https://t.me/ARAKAL_THERAVAD_GROUP_04")
        ],[
        InlineKeyboardButton("🖥 𝗡𝗘𝗪 𝗢𝗧𝗧 𝗨𝗣𝗗𝗔𝗧𝗘𝗦 🖥", url="https://t.me/OTT_ARAKAL_THERAVAD_MOVIESS")
        ],[
        InlineKeyboardButton("⭕️ 𝗚𝗘𝗧 𝗢𝗨𝗥 𝗖𝗛𝗔𝗡𝗡𝗘𝗟 𝗟𝗜𝗡𝗞𝗦 ⭕️", url="https://t.me/ARAKAL_THERAVAD_GROUP_LINKS")
    ]])
    
    try:
        await client.send_photo(
            r.from_user.id,
            'https://telegra.ph/file/03a7b834ccabe5017f6b5.jpg https://telegra.ph/file/8b5f3c3bfa867b1c842ed.jpg',
            f"**𝖧𝖾𝗅𝗅𝗈 {r.from_user.mention} 👻, 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 {r.chat.title}\n𝖸𝗈𝗎𝗋 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖧𝖺𝗌 𝖡𝖾𝖾𝗇 𝖠𝗉𝗉𝗋𝗈𝗏𝖾𝖽...!!!**",
            reply_markup=rm)

    except UserIsBlocked:
        print("User blocked the bot")
    except PeerIdInvalid:
        print("Err")
    except Exception as e:
        print(f"#Error\n{str(e)}")

    await r.approve()
