from telegram import Update
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext
import random
import datetime


def print_board(board):
    
    keyboard = [[], [], []]

    if board != None:  
        for i in range(0, 3):
            for j in range(0, 3):
                keyboard[i].append(InlineKeyboardButton(board[j + i * 3], callback_data = str(board[j + i * 3]) + board))

    return keyboard
        



def InputNumber(text):
    is_OK = False
    while not is_OK:
       
        try:
            number =int(input(f"Ваш ход, выберите свободную ячейку {text} от 1 до 9:"))
        except ValueError:
            print('Это не число!')
            continue
        if number >= 1 and number <= 9:
            if(str(board[number-1]) not in 'XO'):
                board[number-1] = text
                is_OK = True
            else:
                print('Занято')
        else:
            print('Это не число от 1 до 9!')

def victory_check(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            #print(board[i[0]])
            return board[i[0]]
    return False

def newGame(update: Update, context: CallbackContext):
    board = "123456789"
    update.message.reply_text('Ваш ход', reply_markup=InlineKeyboardMarkup(print_board(board)))
    

def countUndefinedCells(cellArray):
    counter = 0
    for i in cellArray:
        if i != 'X' and i != 'O':
            counter += 1
    return counter

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    callbackData = query.data 
    print(callbackData[0])
    message, callbackData, alert = game(callbackData) 
    query.answer()  
    query.edit_message_text(text=message, reply_markup=InlineKeyboardMarkup(print_board(callbackData)))
    
def game(callBackData):
    message = 'Ваш ход'
    alert = None

    buttonNumber = int(callBackData[0])  
    charList = list(callBackData)  
    print(charList)
    charList.pop(0)  
    if charList[buttonNumber-1] != 'X' and charList[buttonNumber-1] != 'O':  
            charList[buttonNumber-1] = 'X'  
            if victory_check(charList):  
                message = "Вы победили"
            else:  
                if countUndefinedCells(charList) != 0:  
                    
                    isCycleContinue = True
                    
                    while (isCycleContinue):
                        rand = random.randint(0, 8)  
                        if charList[rand-1]  != 'X' and charList[rand-1] != 'O':  
                            charList[rand-1] = 'O'
                            isCycleContinue = False  
                            if victory_check(charList):  
                                message = "Бот победил"

        
    else:
            alert = "Занято"

        
    if countUndefinedCells(charList) == 0 and message == "Ваш ход":
            message = 'Ничья'

        
    callBackData = ''
    for c in charList:
            callBackData += c

    if message == "Вы победили" or message == "Бот победил" or message == 'Ничья':
        message += '\n'
        for i in range(0, 3):
            message += '\n | '
            for j in range(0, 3):
                message += callBackData[j + i * 3] + ' | '
        callBackData = None 

    return message, callBackData, alert