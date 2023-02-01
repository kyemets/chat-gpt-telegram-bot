from revChatGPT.ChatGPT import Chatbot
from aiogram import Bot, Dispatcher, executor, types, executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import aiogram.utils.markdown as fmt
import asyncio
import os.path
import keyboard as kb


bot = Bot("5810386021:AAGZ9LXIRO-Cf36kTNT4Qjf0yzJwydLMeLk")
dp = Dispatcher(bot)


''' Command Start '''
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
  user_id = message.from_user.id
  await bot.send_sticker(user_id, sticker='CAACAgIAAxkBAAEEeItiWG7TWqCapeRnGLmb0JhzlfO6UwACAQEAAladvQoivp8OuMLmNCME')
  await message.answer(f"Hi, {message.from_user.first_name}")
  await message.answer("Available command: /chat  ")


""" chat """
@dp.message_handler(commands="chat")
async def cmd_start(message: types.Message):
  await message.answer("Input a text")

  @dp.message_handler()
  async def get_msg(message: types.Message):
    get_msg = message.text
            
    chatbot = Chatbot({
      "session_token": "<SESSION_TOKEN>"
    }, conversation_id=None, parent_id=None) # You can start a custom conversation

    response = chatbot.ask(get_msg, conversation_id=None, parent_id=None) # You can specify custom conversation and parent ids. Otherwise it uses the saved conversation (yes. conversations are automatically saved)
    await message.answer(response['message'])

  
if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)