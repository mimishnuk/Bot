from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from decouple import config

TOKEN = config("TOKEN")


bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['mem'])
async def mem_1(message: types.Message):
    photo = open("media/5.jpeg", 'rb')
    await bot.send_photo(message.from_user.id, photo=photo)



@dp.message_handler(commands=['start', 'help'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f"Охаёёё {message.from_user.first_name}")


@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data='button_call_1')
    markup.add(button_call_1)

    question = "Сколько полос на флаге США?"
    answers = [
        "56",
        '21',
        '13',
        '11',
        '9',
    ]

    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="иди учиться",
        open_period=10,
        reply_markup=markup
    )


@dp.callback_query_handler(text="button_call_1")
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("NEXT", callback_data='button_call_2')
    markup.add(button_call_2)

    question = "Какой национальный цветок Японии?"

    answers = [
        "Лотос",
        "Сакура",
        "Айгуль",
        "Гирень",
        "Гипсофилы",
        "Кактус",
    ]

    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Забей в гугле",
        open_period=10,
        reply_markup=markup
    )



@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)
    if message.text.isnumeric():
        await bot.send_message(message.from_user.id, int(message.text) ** 2)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
