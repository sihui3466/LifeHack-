from multiprocessing import context
import types
from telegram import Bot, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, Update
import telegram
from telegram.ext import ApplicationBuilder, CallbackQueryHandler, CommandHandler,MessageHandler
from telegram.ext import filters
import telebot
import requests
import os
from dotenv import load_dotenv
import json
load_dotenv()
from googlemaps import Client as GoogleMaps

BOT_TOKEN= os.getenv('BOT_TOKEN')
tb = telebot.TeleBot(BOT_TOKEN)
# GOOGLEMAP=os.getenv('API_KEY')
PORT=int(os.environ.get('PORT',13978))
#update object contain all users name
async def help(options,context):
    await options.message.reply_text('Need help navigating around the chatbot? You may used the following to navigate around\nCommands:\n/start:Starts the bot\n/help: Get list of commands');

async def choice(options,context):
    keyboard=[ #4 dimensional array 4 rows
            [ 
                InlineKeyboardButton("Do you need help in preparing the recyclables?",callback_data="prepare") #callback data means data that is saved and passed back to us when users choose an option
            ],
            [ 
                InlineKeyboardButton("Find your nearest recycling point.",callback_data="point") #callback data means data that is saved and passed back to us when users choose an option
            ]
    ]
    reply_markup=InlineKeyboardMarkup(keyboard)
    await options.message.reply_text(f'Hello {options.effective_user.first_name}! What Would You Like To Do Today? :) \nHit /help for more information', reply_markup=reply_markup)
    return getname

async def getname(options,context):
    query=options.callback_query
    print(query)
    await query.answer()

    userinput =query.data

    # await query.edit_message_text(text=f"{options.effective_user.first_name} is in {location}")

    if (userinput=='point'):
        keyboard=[ #4 dimensional array 4 rows
            [ 
                InlineKeyboardButton("North",callback_data="north") #callback data means data that is saved and passed back to us when users choose an option
            ],
            [ 
                InlineKeyboardButton("Central",callback_data="central") #callback data means data that is saved and passed back to us when users choose an option
            ],
            [ 
                InlineKeyboardButton("West",callback_data="west") #callback data means data that is saved and passed back to us when users choose an option
            ],
            [ 
                InlineKeyboardButton("East",callback_data="east") #callback data means data that is saved and passed back to us when users choose an option
            ],
            

        ]
        # keyboard=ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        # button_geo = KeyboardButton(text="hello", request_location=True)
        # keyboard.add(button_geo)
        # await options.callback_query.message.edit_text(options.chat.id, 'ddksdks',reply_markup=keyboard)
  
        reply_markup=InlineKeyboardMarkup(keyboard)
        await options.callback_query.message.edit_text("Which Region Do You Live In?", reply_markup=reply_markup)
        
    if (userinput=='north'):
        await options.callback_query.message.edit_text(f"Locations in {userinput}!\nhttps://www.nea.gov.sg/our-services/waste-management/3r-programmes-and-resources/e-waste-management/where-to-recycle-e-waste")
    if (userinput=='central'):
        await options.callback_query.message.edit_text(f"Locations in {userinput}!\nhttps://www.nea.gov.sg/our-services/waste-management/3r-programmes-and-resources/e-waste-management/where-to-recycle-e-waste")
    if (userinput=='east'):
        await options.callback_query.message.edit_text(f"Locations in {userinput}!\nhttps://www.nea.gov.sg/our-services/waste-management/3r-programmes-and-resources/e-waste-management/where-to-recycle-e-waste")
    if (userinput=='west'):
        await options.callback_query.message.edit_text(f"Locations in {userinput}!\nhttps://www.nea.gov.sg/our-services/waste-management/3r-programmes-and-resources/e-waste-management/where-to-recycle-e-waste")
        
    if (userinput=='prepare'):
        keyboard=[ #4 dimensional array 4 rows
            [ 
                InlineKeyboardButton("Plastic",callback_data="plastic") #callback data means data that is saved and passed back to us when users choose an option
            ],
            [ 
                InlineKeyboardButton("Aluminium",callback_data="aluminium") #callback data means data that is saved and passed back to us when users choose an option
            ],
            [ 
                InlineKeyboardButton("Paper",callback_data="paper") #callback data means data that is saved and passed back to us when users choose an option
            ],
            [ 
                InlineKeyboardButton("Electronics",callback_data="ewaste") #callback data means data that is saved and passed back to us when users choose an option
            ],
            [ 
                InlineKeyboardButton("Others",callback_data="others") #callback data means data that is saved and passed back to us when users choose an option
            ],
            
            
        ]
        reply_markup=InlineKeyboardMarkup(keyboard)
        # await options.message.reply_text("What is favourite food", reply_markup=reply_markup)
        await options.callback_query.message.reply_text("Select The Type of Recyclables.", reply_markup=reply_markup)
    
    if userinput=='plastic':
        await options.callback_query.message.edit_text("https://www.youtube.com/watch?v=6rdBRKe5lMM")
    elif userinput=='aluminium':
        await options.callback_query.message.edit_text("https://www.youtube.com/watch?v=XF6OV0brUC0")
    elif userinput=='paper':
        await options.callback_query.message.edit_text("https://www.youtube.com/watch?v=YJJbipvCHSA")
    elif userinput=='ewaste':
        await options.callback_query.message.edit_text("https://www.youtube.com/watch?v=fyuxWDkLdcI ")
    elif userinput=='others':
        await options.callback_query.message.edit_text("https://www.youtube.com/watch?v=eDOAKQFSLgA")
        
# async def location(options,userinput):
    
#     print(userinput+'he')
#     if (userinput=='north'):
#         markup = types.ReplyKeyboardMarkup(row_width=2)
#         button1=KeyboardButton(text="send_location",request_location=True)
#         button2=KeyboardButton(text="send_location",request_location=True)
#         keyboard1=markup.add(button1, button2)
#         await options.callback_query.message.edit_text("Location", reply_markup=keyboard1)
#         print('hh')
    


bot=ApplicationBuilder().token(BOT_TOKEN).build()
db = telegram.Bot(BOT_TOKEN)

# connecting to the bot

# bot.add_handler(CommandHandler("hello", hello))
bot.add_handler(CommandHandler("start", choice))
bot.add_handler(CommandHandler("help", help))
# async def location(options,context):
#     if db.get_updates():
#         location_keyboard = telegram.KeyboardButton(text="send_location", request_location=True)
#         contact_keyboard = telegram.KeyboardButton(text="send_contact", request_contact=True)
#         custom_keyboard = [[location_keyboard, contact_keyboard]]
#         reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)

#         await options.callback_query.message.edit_text(text="Would you mind sharing your contact and location with me?", reply_markup=reply_markup)
        
#     else:
#         print("Empty list. Please, chat with the bot")
bot.add_handler(CallbackQueryHandler(getname))
# bot.add_handler(CallbackQueryHandler(location))
bot.run_polling()