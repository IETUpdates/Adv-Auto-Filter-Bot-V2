#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from bot import Translation, LOGGER # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        try:
            await update.reply_cached_media(
                file_id,
                quote=True,
                caption = f"@MM_MOVIESS {file_name}",
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🎖️ᴊᴏɪɴ ᴅɪꜱᴄᴜꜱꜱɪᴏɴ 🎖️', url="https://t.me/MM_MOVIESS"
                                )
                        ]
                    ]
                )
            )
        except Exception as e:
            await update.reply_text(f"<b>Error:</b>\n<code>{e}</code>", True, parse_mode="html")
            LOGGER(__name__).error(e)
        return

    buttons = [[
        InlineKeyboardButton('📽️Fᴏʀ ꜱᴇʀɪᴇꜱ', url='https://t.me/mm_seriess'),
        InlineKeyboardButton('🎥Fᴏʀ ᴍᴏᴠɪᴇꜱ', url ='https://t.me/mm_moviess')
    ],[
        InlineKeyboardButton('🏵️ SHERE & SUPPORT 🏵️', url='http://t.me/share/url?url=%2A%2AHai+Bro%20%E2%9D%A4%EF%B8%8F%2C%20%2A%2A%0A__Today%20I%20Just%20Found%20Out%20A%20Movie+Group%20Which%20Uploads__%20%2A%2ARequested+Movies%20In%20Second's%2A%2A%F0%9F%A5%B0.%0A%2A%2AJσιи+Nσω%20%20%3A%20%40MM_MOVIESS+👌%F0%9F%94%A5%2A%2A%0A%2A%2AJσιи+Nσω%20%20%3A%20%40MM_SERIESS+👌%F0%9F%94%A5%2A%2A.%0A%2A%2AJσιи+Nσω%20%20%3A%20%40MM_NewOTTUpdatesS+👌%F0%9F%94%A5%2A%2A')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('About 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('Home ⚡', callback_data='start'),
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
