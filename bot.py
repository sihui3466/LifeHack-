from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, ConversationHandler, CallbackQueryHandler, CommandHandler, MessageHandler, filters
import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

BOT_TOKEN= os.getenv('BOT_TOKEN')
# GOOGLEMAP=os.getenv('API_KEY')
# gmaps=GoogleMaps(GOOGLEMAP)

#update object contain all users name
async def hello(options,context):
    await options.message.reply_text(f'Hello {options.effective_user.first_name}! \n\nWelcome to SihuiTest_bot, What would you like to do? \n\nIf you have any queries, please contact us at @sihuiiii27\n\n/question : Select to start game');

async def choice(options,context):
    keyboard=[ #4 dimensional array 4 rows
            [ 
                InlineKeyboardButton("Lex",callback_data="lex") #callback data means data that is saved and passed back to us when users choose an option
            ],
            [ 
                InlineKeyboardButton("Damian",callback_data="damian") #callback data means data that is saved and passed back to us when users choose an option
            ],
            [ 
                InlineKeyboardButton("Kayla",callback_data="kayla") #callback data means data that is saved and passed back to us when users choose an option
            ]
    ]
    reply_markup=InlineKeyboardMarkup(keyboard)
    await options.message.reply_text("Who is the smartest?", reply_markup=reply_markup)
    return getname

async def getname(options,context):
    query=options.callback_query

    await query.answer()

    name=query.data

    await query.edit_message_text(text=f"{options.effective_user.first_name} selected option: {name} is the smartest")

    if name=='lex':
        keyboard2=[ 
            [ 
                InlineKeyboardButton("Pancake",callback_data="pancake"), #callback data means data that is saved and passed back to us when users choose an option
                InlineKeyboardButton("Cake",callback_data="cake"), #callback data means data that is saved and passed back to us when users choose an option
            ],
            [ 
                InlineKeyboardButton("Bread",callback_data="bread"), #callback data means data that is saved and passed back to us when users choose an option
                InlineKeyboardButton("Puff",callback_data="puff"), #callback data means data that is saved and passed back to us when users choose an option
            ]
        ]
    reply_markup2=InlineKeyboardMarkup(keyboard2)
    await options.message.reply_text("What is favourite food", reply_markup=reply_markup2)

# async def pointsys():
#     question_1 = '1) Who was the first American woman in space? '
#     correct_answer_1 = 'Sally Ride'
#     candidate_answer_1 = input(question_1)
    
#     question_2 = '2) True or false: 5 kilometer == 5000 meters? '
#     correct_answer_2 = 'true'
#     candidate_answer_2 = input(question_2)
    
#     question_3 = '3) (5 + 3)/2 * 10 = ? '
#     correct_answer_3 = '40'
#     candidate_answer_3 = input(question_3)
    
#     question_4 = "4) Given the list [8, 'Orbit', 'Trajectory', 45], what entry is at index 2? "
#     correct_answer_4 = 'Trajectory'
#     candidate_answer_4 = input(question_4)
    
#     question_5 = '5) What is the minimum crew size for the ISS? '
#     correct_answer_5 = '3'
#     candidate_answer_5 = input(question_5)
    
#     #lists that correlate to the variables assigned above
    
#     quiz_questions = [question_1, question_2, question_3, question_4, question_5]
#     correct_answers = [correct_answer_1, correct_answer_2, correct_answer_3, correct_answer_4, correct_answer_5]
#     candidate_answers = [candidate_answer_1, candidate_answer_2, candidate_answer_3, candidate_answer_4, candidate_answer_5]
    
#     points = 0
#     for correct, candidate in zip(correct_answers, candidate_answers):
#         if correct.lower() == candidate.lower():
#             points += 1
#             print(f'Your Answer: {candidate}\nCorrect Answer: {correct}') 
#         else:
#             print('Incorrect.\nThe correct answer is: ', correct)
#     print(points)
        

bot=ApplicationBuilder().token(BOT_TOKEN).build()
bot.add_handler(CommandHandler("start", hello))
bot.add_handler(CommandHandler("question", choice))
bot.add_handler(CallbackQueryHandler(getname))
bot.run_polling()