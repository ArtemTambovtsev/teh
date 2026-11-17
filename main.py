import telebot
from telebot import types

TOKEN = "8270149322:AAH4J9NyqbRfGy3oaNLZZlN0nS_ZWCt3hAE"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
  menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
  menu.add(types.KeyboardButton("Популярные вопросы"))
  menu.add(types.KeyboardButton("Задать вопрос специалисту"))

  bot.send_message(
      message.chat.id,
      'Привет! Интернет-магазин "Все на свете". Выбери, что нужно:',
      reply_markup=menu,
  )

@bot.message_handler(func=lambda message: True)
def handle_text(message):
  text = message.text

  
  if text == "Популярные вопросы":
    answers = (
        "<b>Популярные вопросы и ответы:</b>"
        "<b>1. Как оформить заказ?</b>"
        'Выбери товар, нажми "Добавить в корзину" и следуй подсказкам на сайте.'
        "<b>2. Как узнать статус заказа?</b>"
        'Зайди в свой аккаунт на сайте в раздел "Мои заказы".'
        "<b>3. Как отменить заказ?</b>"
        "Свяжись с поддержкой как можно быстрее до отправки заказа."
        "<b>4. Товар поврежден?</b>"
        "Сразу напиши в поддержку и отправь фото повреждений."
        "<b>5. Как узнать про доставку?</b>"
        "Все сроки и способы указаны при оформлении заказа на сайте."
    )
    bot.send_message(message.chat.id, answers, parse_mode="HTML")

  
  elif text == "Задать вопрос специалисту":
    bot.send_message(
        message.chat.id,
        "Напиши свой вопрос следующим сообщением, и он уйдет специалистам:",
    )
    
    bot.register_next_step_handler(message, save_question)

  else:
    bot.send_message(
        message.chat.id, "Пожалуйста, используй кнопки меню внизу экрана."
    )


def save_question(message):
  bot.send_message(
      message.chat.id,
      "Готово! Твой вопрос успешно отправлен специалистам магазина.",
  )


bot.infinity_polling()

