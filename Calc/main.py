import telebot
from random import *
import logger as log
import json
from telebot import types
from model import calc
bot = telebot.TeleBot('5621219084:AAG_65PwtTTIlQ6L-XEOS6WDGs5iuy0jeyc')
value_a = 0
value_b = 0
operation = ""
result = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Введите первое число")
        bot.register_next_step_handler(message, get_value_a); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')

def get_value_a(message): #получаем фамилию
    global value_a
    value_a = float(message.text)
    bot.send_message(message.from_user.id, 'Введите второе число')
    bot.register_next_step_handler(message, get_value_b);

def get_value_b(message):
    global value_b
    value_b = float(message.text)
    bot.send_message(message.from_user.id, "Введите операцию(варианты:+,-,/,*,mod,pow,div): ")
    bot.register_next_step_handler(message, get_operation)

def get_operation(message):
    global operation
    operation = str(message.text) 
    result = calc(value_a, value_b, operation)
    log.calc_logger(f'{value_a} {operation} {value_b} = {result}')
    bot.send_message(message.from_user.id, f"Результат = {result}")

print('server start')
bot.polling()