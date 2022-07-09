from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, ConversationHandler, CallbackQueryHandler, CommandHandler, MessageHandler, filters
import requests
import os
from dotenv import load_dotenv
import json
load_dotenv()
from googlemaps import Client as GoogleMaps

BOT_TOKEN= os.getenv('BOT_TOKEN')
# GOOGLEMAP=os.getenv('API_KEY')

#update object contain all users name
async def hello(options,context):
    await options.message.reply_text(f'Hello {options.effective_user.first_name}! \n\n/start : Select an option');

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
    await options.message.reply_text(f'Hello {options.effective_user.first_name}! What Would You Like To Do Today? :)', reply_markup=reply_markup)
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
            ]
        ]
        print('Hi')
        reply_markup=InlineKeyboardMarkup(keyboard)
        # await options.message.reply_text("What is favourite food", reply_markup=reply_markup)
        await options.callback_query.message.edit_text("Which Region Do You Live In?", reply_markup=reply_markup)
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
            ]
        ]
        reply_markup=InlineKeyboardMarkup(keyboard)
        # await options.message.reply_text("What is favourite food", reply_markup=reply_markup)
        await options.callback_query.message.edit_text("Select The Type of Recyclables.", reply_markup=reply_markup)
    return recycle_vid

async def recycle_vid(options,context):
    query=options.callback_query
    print(query)
    await query.answer()

    userinput2=query.data

    reply_markup2 = "https://www.youtube.com/watch?v=YJJbipvCHSA"
    
    if (userinput2=='plastic'):
        print('Hi')
        # await options.callback_query.message.edit_text("Youtube=>\https://www.youtube.com/watch?v=YJJbipvCHSA")
        await options.callback_query.message.edit_text("Select The Type of Recyclables.", reply_markup=reply_markup2)


# async def recycle_vid(options:Update, context:CallbackContext):
#     await options.message.reply_text("Youtube=>\https://www.youtube.com/watch?v=YJJbipvCHSA")

bot=ApplicationBuilder().token(BOT_TOKEN).build()
# bot.add_handler(CommandHandler("hello", hello))
bot.add_handler(CommandHandler("start", choice))
bot.add_handler(CallbackQueryHandler(getname))
bot.add_handler(CallbackQueryHandler(recycle_vid))
bot.run_polling()
