
import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

wikipedia.set_lang("uz")
API_TOKEN = '5887330674:AAGptIDeQcUSaRQStwhTh1S5_4HPMeFifiw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'boshlash'])
async def send_welcome(message: types.Message):
    await message.reply("Salom!\nWikipedia botga xush kelibiz!")


@dp.message_handler(commands=['help', 'yordam'])
async def send_welcome(message: types.Message):
    await message.reply("Wikipedia bot!\nKerakli ma'umotlarni qulay topib beradi!")


@dp.message_handler()

async def echo(message: types.Message):
	kirish_matn = message.text
	try:
		javob_matn = wikipedia.summary(kirish_matn)
		await message.reply(javob_matn)
	except:
		await message.reply("Bu mavzuga oid maqola topilmadi :(\nMatnni to'g'ri yozganingizni tekshiring!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)