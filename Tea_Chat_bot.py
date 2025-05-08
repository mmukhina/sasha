import telebot
from telebot import types

#bot = telebot.TeleBot(token="8057253291:AAGJ6XypfwO4-WrY897HO7E9BlnDaDp6E6g")

test_points = {}

r_file = 'rating.txt'
rating_user1 = {}

import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

from flask import Flask, request

server = Flask(__name__)

@server.route('/' + os.environ.get('BOT_TOKEN'), methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://your-render-app-name.onrender.com/' + os.environ.get('BOT_TOKEN'))
    return "Webhook set!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


def load_rating():
    with open(r_file, 'r', encoding='utf-8') as f:
        for line in f:
            user_id, tea_type, rating = line.strip().split(':')
            rating_user1.setdefault(int(user_id), {})[tea_type] = int(rating)

@bot.message_handler(commands=['afterword'])
def start(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    bot.send_message(chat_id, """🌿 *Послесловие* 🌿

Не надо воспринимать предложенный чай, как поное лечение
Это лишь совет, что можно заварить, чтобы стало лучше

_Для консультации лучше обратиться к врачу_
""", parse_mode="Markdown")

@bot.message_handler(commands=['help'])
def start(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    bot.send_message(chat_id, """🆘 *Ты призвал помощь* 🆘

Этот Великий бот имеет две главные функции:
⚡️ Предлагать чай по желаниям пользователя
⚡️ Расскрыть пользователю, какой он чай

Также эсть генияльная функция рейтинга чай, где ты можешь поставить оценку чаю и посмотреть его среднюю

Сперва наперво, чтобы начать напиши /start
""", parse_mode="Markdown")
                    
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    bot.send_sticker(chat_id, "CAACAgIAAxkBAAEO6M9oGiM9bGoj1XsxoDCVId_B2iwk9wACbV4AAlchOUtBSAABpOELi1M2BA")
    bot.send_message(chat_id, "🐉 *Великий чаевед приветствует тебя!* 🐉", parse_mode="Markdown")
    mode1(message)

def mode1(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    tea = types.InlineKeyboardButton(text="Выбор чая", callback_data="tea") 
    test = types.InlineKeyboardButton(text="Тест «Какой ты чай?»", callback_data="test") 
    keyboard.add(tea, test)
    bot.send_message(message.chat.id, """Что ты сегодня хочешь?""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["tea", "test"]) 
def callback_inline(call): 
    if call.message: 
        if call.data == "tea":
            tea(call.message)
            menu11(call.message)
        elif call.data == "test": 
            test(call.message)
            menu11(call.message)

def tea(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    medicine = types.InlineKeyboardButton(text="Лечение", callback_data="medicine") 
    lose_weight = types.InlineKeyboardButton(text="Похудение", callback_data="lose_weight")
    other = types.InlineKeyboardButton(text="Другое", callback_data="other") 
    keyboard.add(medicine, lose_weight, other) 
    bot.send_message(message.chat.id, "🍵 Для чего вы будете пить чай?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["medicine", "lose_weight", "other"]) 
def callback_inline(call): 
    if call.message: 
        if call.data == "medicine":
            medicine(call.message)
        elif call.data == "lose_weight": 
            lose_weight(call.message)
        elif call.data == "other": 
            other(call.message)

def medicine(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    vitamins = types.InlineKeyboardButton(text="Авитаминоз", callback_data="vitamins")
    cold = types.InlineKeyboardButton(text="Простуда", callback_data="cold")
    headache = types.InlineKeyboardButton(text="Головная боль", callback_data="headache")
    sleep = types.InlineKeyboardButton(text="Проблема со сном", callback_data="sleep")
    fatigue = types.InlineKeyboardButton(text="Усталость", callback_data="fatigue")
    keyboard.add(vitamins, cold, headache, sleep, fatigue)
    
    bot.send_message(message.chat.id, "🌡 Что болит?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["vitamins", "cold", "headache", "sleep", "fatigue"]) 
def callback_inline1(call): 
    if call.message: 
        if call.data == "vitamins":
            vitamins(call.message)
            
        elif call.data == "cold": 
            cold(call.message)
            
        elif call.data == "headache": 
            headache(call.message)
            
        elif call.data == "sleep": 
            sleep(call.message)
            
        elif call.data == "fatigue": 
            fatigue(call.message)

def vitamins(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    kid = types.InlineKeyboardButton(text="Ребенок", callback_data="kid")
    adult = types.InlineKeyboardButton(text="Взрослый", callback_data="adult")
    keyboard.add(kid, adult)
    
    bot.send_message(message.chat.id, "🤨 Кто ты?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["kid", "adult"]) 
def callback_inline2(call):
    chat_id = call.message.chat.id
    if call.message: 
        if call.data == "kid":
            photo_path = "Tea_kid.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Детский чай «Витаминный»* 🍵
Помогает обогатить организм витаминами, полезными ферментами и  микроэлементами

*Cостав:*
- Цветки аптечной ромашки
- Трава душицы  обыкновенной
- Плоды шиповника майского
- Трава тимьяна ползучего (чабреца)
- Трава  мяты перечной
""", parse_mode="Markdown")

            ask_for_rating(call.message, "kid")

        elif call.data == "adult": 
            adult(call.message)

def adult(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    energy = types.InlineKeyboardButton(text="Дефицит энергии", callback_data="energy")
    low_vitality = types.InlineKeyboardButton(text="Простуда", callback_data="low_vitality")
    immunity = types.InlineKeyboardButton(text="Имунодифецит", callback_data="immunity")
    keyboard.add(energy, low_vitality, immunity)
    
    bot.send_message(message.chat.id, """📋 Какие из следующих симптомов ты наблюдаешь?""", reply_markup=keyboard, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data in ["energy", "low_vitality", "immunity"]) 
def callback_inline3(call):
    chat_id = call.message.chat.id
    if call.message: 
        if call.data == "energy":
            photo_path = "Tea_adult_grass.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Травяной чай «Витаминный»* 🍵
Чай обладает тонизирующим действием, восполняет дефицит  энергии, повышает выносливость, придаёт бодрость

*Состав:*
- Облепиха
- Душица
- Плоды шиповника
- Листья брусники,  малины, рябины           
""", parse_mode="Markdown")
            ask_for_rating(call.message, "energy")
            
        elif call.data == "low_vitality":
            photo_path = "Tea_adult_Altai.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Фиточай «Алтай» №15 «Витаминка»* 🍵
Рекомендуется для поддержки иммунитета и повышения жизненного тонуса. Применяется как общеукрепляющее средство в период простуд и  авитаминозов

*Состав:*
- Цветки ромашки
- Листья смородины
- Плоды  рябины красной
- Листья крапивы
""", parse_mode="Markdown")
            ask_for_rating(call.message, "low_vitality")
            
        elif call.data == "immunity":
            photo_path = "Tea_adult_gift.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Подарочный чай «Витаминный»* 🍵
Чай помогает поддерживать иммунитет и укреплять  организм

*Состав:*
- Листья ежевики, мяты, лимонника, календулы
- Кожура апельсина
- Брусника
- Клубника
- Облепиха
""", parse_mode="Markdown")

        ask_for_rating(call.message, "immunity")

def cold(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    stress = types.InlineKeyboardButton(text="Воспаления", callback_data="stress")
    
    fever = types.InlineKeyboardButton(text="Жар", callback_data="fever")
    
    cold1 = types.InlineKeyboardButton(text="Простуда", callback_data="cold1")
    
    diarrhea = types.InlineKeyboardButton(text="Диспепсия", callback_data="diarrhea")
    
    fatigue1 = types.InlineKeyboardButton(text="Усталость", callback_data="fatigue1")
    keyboard.add(stress, fever, cold1, diarrhea, fatigue1)
    
    bot.send_message(message.chat.id, """📋 Какие из следующих симптомов ты наблюдаешь?""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["stress", "fever", "cold1", "diarrhea", "fatigue1"]) 
def callback_inline4(call):
    chat_id = call.message.chat.id
    if call.message: 
        if call.data == "stress":
            photo_path = "Tea_honey.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Чай с мёдом и лимоном* 🍵
Лучше готовить некрепким, можно использовать как чёрный, так и зелёный чай
В напиток  добавляют 1 чайную ложку мёда и 1–2 дольки лимона. Чтобы сохранить полезные  свойства мёда и лимона, их не кладут в горячий напиток

*Состав:*
- Чай черный/зеленный
- Мед пчелинный
- Лимон
""", parse_mode="Markdown")
            ask_for_rating(call.message, "stress")
            
        elif call.data == "fever":
            photo_path = "Tea_raspberry.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Чай с малиной и липовым цветом* 🍵
Такой чай обладает липово-малиновым ароматом и считается мочегонным средством

*Состав:*
- Липовый цвет
- Ягоды малины
- Черный чай
- Лимон
- Сахар(по вкусу)
""", parse_mode="Markdown")
            ask_for_rating(call.message, "immunity")
            
        elif call.data == "cold1":
            photo_path = "Tea_ginger.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Имбирный чай* 🍵
Имбирный чай может быть полезен для организма, так как имбирь содержит витамины, минералы и эфирные масла

*Состав:*
- Лимон
- Имбирь
- Мед
- Гвоздика
""", parse_mode="Markdown")
            ask_for_rating(call.message, "cold1")
            
        elif call.data == "diarrhea":
            photo_path = "Tea_chamomile.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Ромашковый чай* 🍵
Популярный травяной напиток, известный своими успокаивающими и оздоровительными свойствами

*Состав:*
- Ромашковый чай
- Мед(про вкусу)
""", parse_mode="Markdown")
            ask_for_rating(call.message, "diarrhea")
            
        elif call.data == "fatigue1":
            photo_path = "Tea_currant.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Чай с листьями чёрной смородины* 🍵
Такой чай укрепляет защитные силы организма в период  простуды, улучшает процессы кроветворения, нормализует обмен веществ, укрепляет  стенки сосудов

*Состав:*
- Листья чёрной смородины
- Листья вишни
- Смородина чёрная
- Мёд (по вкусу)
""", parse_mode="Markdown")
            ask_for_rating(call.message, "fatigue1")
            
def headache(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    grasstea = types.InlineKeyboardButton(text="Травяной настой", callback_data="grasstea")
    greentea = types.InlineKeyboardButton(text="Зеленый чай", callback_data="greentea")
    fitotea = types.InlineKeyboardButton(text="Фито чай", callback_data="fitotea")
    keyboard.add(grasstea, greentea, fitotea)
    
    bot.send_message(message.chat.id, """🍂 Какой сорт чая ты предпочитаешь пить?""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["grasstea", "greentea", "fitotea"]) 
def callback_inline5(call):
    chat_id = call.message.chat.id
    if call.message: 
        if call.data == "grasstea":
            photo_path = "Tea_chamomile.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Ромашковый чай* 🍵
Популярный травяной напиток, известный своими успокаивающими и оздоровительными свойствами

*Состав:*
- Ромашковый чай
- Мед(про вкусу)
""", parse_mode="Markdown")
            ask_for_rating(call.message, "grasstea")
            
        elif call.data == "greentea":
            photo_path = "Tea_green.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Зелёный чай с лимоном* 🍵
Полезный напиток, который содержит антиоксиданты, эфирные масла и витамин Р. Он оказывает мочегонный эффект, понижает уровень сахара в крови и притупляет чувство голода

*Состав:*
- Зеленый чай
- Лимон
- Мед (по вкусу)
""", parse_mode="Markdown")
            ask_for_rating(call.message, "greentea")
            
        elif call.data == "fitotea":
            photo_path = "Tea_fito.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Сила российских трав №7* 🍵
Фиточай, который рекомендован при головной боли любого характера

*Состав:*
- Зверобой
- Кипрей
- Мята перечная
- Боярышник
- Пустырник
- Валериана
""", parse_mode="Markdown")
            ask_for_rating(call.message, "fitotea")

def sleep(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    stress1 = types.InlineKeyboardButton(text="Стресс", callback_data="stress1")
    
    anxiety = types.InlineKeyboardButton(text="Тревожность", callback_data="anxiety")
    
    badsleep = types.InlineKeyboardButton(text="Бодроствование", callback_data="badsleep")
    
    insomnia = types.InlineKeyboardButton(text="Бессонница", callback_data="insomnia")
    
    nervous = types.InlineKeyboardButton(text="Нервозность", callback_data="nervous")
    keyboard.add(stress1, anxiety, badsleep, insomnia, nervous)
    
    bot.send_message(message.chat.id, """📋 Какие из следующих симптомов ты наблюдаешь?""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["stress1", "anxiety", "badsleep", "insomnia", "nervous"]) 
def callback_inline6(call):
    chat_id = call.message.chat.id
    if call.message: 
        if call.data == "stress1":
            photo_path = "Tea_chamomile.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Ромашковый чай* 🍵
Популярный травяной напиток, известный своими успокаивающими и оздоровительными свойствами

*Состав:*
- Ромашковый чай
- Мед(про вкусу)
""", parse_mode="Markdown")
            ask_for_rating(call.message, "stress1")
            
        elif call.data == "anxiety":
            photo_path = "Tea_mint.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Чай с мятой* 🍵
Действие чая с мятой зависит от концентрации травы. В небольшом количестве мята оказывает успокаивающее действие, а концентрированный настой приобретает бодрящий эффект

*Состав:*
- Листья мяты
- Вода
- Лимон (по желанию)
- Сахар/мед (по желанию)
""", parse_mode="Markdown")
            ask_for_rating(call.message, "anxiety")
            
        elif call.data == "badsleep":
            photo_path = "Tea_lavanda.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Чай из цветов лаванды* 🍵
Улучшает сон, укрепляет иммунитет

*Состав:*
- Засшенные цветы лаванды
- Свежая мята
- Мед (по вкусу)
""", parse_mode="Markdown")
            ask_for_rating(call.message, "badsleep")

        elif call.data == "insomnia":
            photo_path = "Tea_valerian.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Чай на основе корня валерианы* 🍵
Чай способствует снижению возбудимости центральной нервной системы, улучшению сна и настроения

*Состав:*
- Корень валерьяны
- Мед
- Лимонный сок
""", parse_mode="Markdown")
            ask_for_rating(call.message, "insomnia")
            
        elif call.data == "nervous":
            photo_path = "Tea_rosehip.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Чай с шиповником* 🍵
Биологически активные вещества в составе шиповника увеличивают сопротивляемость организма инфекциям, принимают участие в углеводном и минеральном обмене.

*Состав:*
- Шиповник сушенный
- Мед
- Корень имбиря
- Лимон
""", parse_mode="Markdown")
            ask_for_rating(call.message, "nervous")

def fatigue(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    vigor = types.InlineKeyboardButton(text="Бодрость", callback_data="vigor")
    fresh = types.InlineKeyboardButton(text="Свежесть", callback_data="fresh")
    tonization = types.InlineKeyboardButton(text="Тонизация", callback_data="tonization")
    productivity = types.InlineKeyboardButton(text="Продуктивность", callback_data="productivity")
    vitamins2 = types.InlineKeyboardButton(text="Прилив витаминов", callback_data="vitamins2")
    keyboard.add(vigor, fresh, tonization, productivity, vitamins2)
    
    bot.send_message(message.chat.id, """🏮 Для чего ты будешь пить чай?""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["vigor", "fresh", "tonization", "productivity", "vitamins2"]) 
def callback_inline7(call):
    chat_id = call.message.chat.id
    if call.message: 
        if call.data == "vigor":
            photo_path = "Tea_puer.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Пуэр* 🍵
Чайный лист пуэра богат кофеином
Есть две разновидности пуэра: шу пуэр («чёрный»,  произведённый по ускоренной технологии) и шэн пуэр («зелёный», произведённый по  естественной, длительной технологии)

*Состав:*
- Пуэр чай
""", parse_mode="Markdown")
            ask_for_rating(call.message, "vigor")
            
        elif call.data == "fresh":
            photo_path = "Tea_green1.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Зелёный чай* 🍵
Утренний зелёный чай помогает не только взбодриться, но и улучшить обмен веществ, способствует сжиганию калорий и содержит антиоксиданты, которые защищают клетки от повреждений

*Состав:*
- Зелёный чай
""", parse_mode="Markdown")
            ask_for_rating(call.message, "fresh")
            
        elif call.data == "tonization":
            photo_path = "Tea_oolong.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Улун* 🍵
Полуферментированный чай, который занимает промежуточное положение между зелёными и красными чаями. В Китае улун часто называют «Цин Ча»

*Состав:*
- Улун
""", parse_mode="Markdown")
            ask_for_rating(call.message, "tonization")

        elif call.data == "productivity":
            photo_path = "Tea_grass1.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Травяной чай* 🍵
Травы содержат много витаминов и полезных веществ, за счёт чего способны зарядить организм продуктивной энергией

*Состав:*
- Травы (в зависимости от вида чая)
""", parse_mode="Markdown")
            ask_for_rating(call.message, "productivity")
            
        elif call.data == "vitamins2":
            photo_path = "Tea_white.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Белый чай* 🍵
Подвергается минимальной обработке — по сути, это просто высушенные  молодые листочки и почки. В них по максимуму, как и в зелёном чае, сохраняются все  полезные вещества и витамины

*Состав:*
- Белый чай
""", parse_mode="Markdown")
            ask_for_rating(call.message, "vitamins2")

def lose_weight(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    metabolism = types.InlineKeyboardButton(text="1", callback_data="metabolism")
    nofat = types.InlineKeyboardButton(text="2", callback_data="nofat")
    appetite = types.InlineKeyboardButton(text="3", callback_data="appetite")
    sugar = types.InlineKeyboardButton(text="4", callback_data="sugar")
    bioactive = types.InlineKeyboardButton(text="5", callback_data="bioactive")
    keyboard.add(metabolism, nofat, appetite, sugar, bioactive)
    
    bot.send_message(message.chat.id, """🧘‍♀ Каким методом ты хочешь похудеть?

*1)* Ускорение метаболизма
*2)* Окисление жиров
*3)* Понижение аппетита
*4)* Понижение сахара в крови
*5)* Биодобавка
""", reply_markup=keyboard, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data in ["metabolism", "nofat", "appetite", "sugar", "bioactive"]) 
def callback_inline8(call):
    chat_id = call.message.chat.id
    if call.message: 
        if call.data == "metabolism":
            photo_path = "Tea_green1.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Зелёный чай* 🍵
Обладает мягким мочегонным эффектом и содержит катехины, которые ускоряют  обмен веществ

*Состав:*
- Зелёный чай
""", parse_mode="Markdown")
            ask_for_rating(call.message, "metabolism")
            
        elif call.data == "nofat":
            photo_path = "Tea_mate.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Чай мате* 🍵
Изготавливается из листьев Парагвайского падуба, содержит витамины,  антиоксиданты и аминокислоты
Мате запускает процесс окисления жиров в  организме и препятствует отложению новых жировых клеток

*Состав:*
- Сушёные листья парагвайского падуба 
""", parse_mode="Markdown")
            ask_for_rating(call.message, "nofat")
            
        elif call.data == "appetite":
            photo_path = "Tea_puer.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Пуэр* 🍵
Понижает аппетит и приводит в норму работу ЖКТ. Содержит большое количество  важных для организма микроэлементов

*Состав:*
- Пуэр чай
""", parse_mode="Markdown")
            ask_for_rating(call.message, "appetite")

        elif call.data == "sugar":
            photo_path = "Tea_roibush.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Ройбуш* 🍵
Понижает уровень сахара в крови, обладает мочегонным свойством

*Состав:*
- Измельчённые листья кустарника Аспалатус линейный
- Мед/сахар (по вкусу)
- Молоко (по вкусу)
""", parse_mode="Markdown")
            ask_for_rating(call.message, "sugar")
            
        elif call.data == "bioactive":
            photo_path = "Tea_Altai.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Фито чай снижение веса алтайский травник* 🍵
Биологически активная добавка к пище, которая нормализует жировой обмен,  уменьшает всасывание жиров и помогает организму выводить скопления шлаков и  токсинов

*Состав:*
- Столбики с рыльцами кукурузы
- Трава горца птичьего (спорыша)
- Корневища имбиря
- Зелёный чай
- Мята перечная
""", parse_mode="Markdown")
            ask_for_rating(call.message, "bioactive")

def other(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    milk = types.InlineKeyboardButton(text="С молоком", callback_data="milk")
    nomilk = types.InlineKeyboardButton(text="Без молока", callback_data="nomilk")
    keyboard.add(milk, nomilk)
    
    bot.send_message(message.chat.id, """🥛 Чай с молоком или без?""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["milk", "nomilk"]) 
def callback_inline9(call):
    chat_id = call.message.chat.id
    if call.message: 
        if call.data == "milk":
            milktea(call.message)
            
        elif call.data == "nomilk":
            no_milktea(call.message)

def milktea(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    india = types.InlineKeyboardButton(text="Индия", callback_data="india")
    taiwan = types.InlineKeyboardButton(text="Тайвань", callback_data="taiwan")
    asia = types.InlineKeyboardButton(text="Южная Азия", callback_data="asia")
    hongkong = types.InlineKeyboardButton(text="Гонг-Конг", callback_data="hongkong")
    keyboard.add(india, taiwan, asia, hongkong)
    
    bot.send_message(message.chat.id, """📍 Место происхождения""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["india", "taiwan", "asia", "hongkong"]) 
def callback_inline10(call):
    chat_id = call.message.chat.id
    if call.message: 
        if call.data == "india":
            photo_path = "Tea_masala.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Масала* 🍵
Традиционный индийский напиток. В Индии для приготовления напитка используют красный гранулированный чай с  маркировкой CTC.

*Состав:*
- Чай
- Пряности
- Молоко
- Подсластитель  
""", parse_mode="Markdown")
            ask_for_rating(call.message, "india")
            
        elif call.data == "taiwan":
            photo_path = "Tea_bubble.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Бабл-ти (чай с шариками)* 🍵
В основе бабл-ти могут быть разные виды чая, включая чёрный, зелёный, улун и с  жасмином

*Состав:*
- Чай
- Молоко
- Шарики из тапиоки
- Кусочки желе
- Вкусовые добавки
""", parse_mode="Markdown")
            ask_for_rating(call.message, "taiwan")
            
        elif call.data == "asia":
            photo_path = "Tea_doodh.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Doodh pati chai* 🍵
Чайный напиток, употребляемый в Индии, Пакистане, Бангладеш, Афганистане и  Непале, в котором молоко вместе с сахаром заваривают с чаем.
Дуд пати отличается от  саада чая тем, что в нем используются только молоко и чай.

*Состав:*
- Чай
- Молоко
- Сахар
- Специи
""", parse_mode="Markdown")
            ask_for_rating(call.message, "asia")

        elif call.data == "hongkong":
            photo_path = "Tea_HongKong.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Hong Kong–style milk tea* 🍵
Напиток появился в середине 20 века, во времена британского правления в Гонконге, и  был вдохновлен британским послеобеденным чаепитием

*Состав:*
- Черный чай (Цейлон)
- Сгущенное молоко
""", parse_mode="Markdown")
            ask_for_rating(call.message, "hongkong")

def no_milktea(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    rice = types.InlineKeyboardButton(text="С рисом", callback_data="rice")
    ice = types.InlineKeyboardButton(text="Холодный чай", callback_data="ice")
    mushroom = types.InlineKeyboardButton(text="Гриб", callback_data="mushroom")
    other1 = types.InlineKeyboardButton(text="Другое", callback_data="other1")
    keyboard.add(rice, ice, mushroom, other1)
    
    bot.send_message(message.chat.id, """✨ Особенности чая""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["rice", "ice", "mushroom", "other1"]) 
def callback_inline11(call):
    chat_id = call.message.chat.id
    if call.message: 
        if call.data == "rice":
            photo_path = "Tea_rice.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Brown rice green tea* 🍵
Считается более полезным, чем обычный зелёный чай, так как коричневый рис  обладает высоким содержанием антиоксидантов.  
Можно пить как горячим, так и холодным, подходит для утреннего  завтрака или послеобеденного перерыва

*Состав:*
- Зелёный чай
- Коричневый рис
""", parse_mode="Markdown")
            ask_for_rating(call.message, "rice")
            
        elif call.data == "ice":
            icetea(call.message)
            
        elif call.data == "mushroom":
            photo_path = "Tea_mushroom.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Чайный гриб (комбуча)* 🍵
Ферментированный напиток, который получают из симбиоза дрожжей и полезных  бактерий
История напитка начинается более двух тысяч лет назад: впервые чайный гриб  упоминается в китайских летописях за 200 лет до нашей эры

*Состав:*
- Чайный гриб (комбуча)
""", parse_mode="Markdown")
            ask_for_rating(call.message, "mushroom")


        elif call.data == "other1":
            other2(call.message)


def icetea(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    lemon = types.InlineKeyboardButton(text="С лимоном", callback_data="lemon")
    strawberry = types.InlineKeyboardButton(text="С клубникой", callback_data="strawberry")
    raspberry = types.InlineKeyboardButton(text="С малиной", callback_data="raspberry")
    berry = types.InlineKeyboardButton(text="С ягодами", callback_data="berry")
    keyboard.add(lemon, strawberry, raspberry, berry)
    
    bot.send_message(message.chat.id, """🧊 Какой чай ты предпочитаешь пить?""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["lemon", "strawberry", "raspberry", "berry"]) 
def callback_inline12(call):
    chat_id = call.message.chat.id
    if call.message: 
        if call.data == "lemon":
            photo_path = "Tea_lemon.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Холодный зелёный чай с лимоном и мятой* 🍵

*Состав:*
- Зелёный чай
- Мята
- Лимон
- Сироп топинамбура
- Лед
""", parse_mode="Markdown")
            ask_for_rating(call.message, "lemon")
            
        elif call.data == "strawberry":
            photo_path = "Tea_strawberry.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Холодный чай с клубникой* 🍵

*Состав:*
- Клубника
- Чай зелёный с цветками жасмина
- Лимон
- Лед  
""", parse_mode="Markdown")
            ask_for_rating(call.message, "strawberry")
            
        elif call.data == "raspberry":
            photo_path = "Tea_raspberry1.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Холодный чай с персиками и малиной* 🍵

*Состав:*
- Травяной сбор
- Мята
- Персики
- Малина
- Лед 
""", parse_mode="Markdown")
            ask_for_rating(call.message, "raspberry")

        elif call.data == "berry":
            photo_path = "Tea_berry.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Холодный чай каркаде с ягодами* 🍵

*Состав:*
- Чай каркаде
- Листья смородины
- Ягоды (малина / ежевика / смородина / вишня)
""", parse_mode="Markdown")
            ask_for_rating(call.message, "berry")

def other2(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    black_berry = types.InlineKeyboardButton(text="Черный ягодный чай", callback_data="black_berry")
    fruit_berry = types.InlineKeyboardButton(text="Фруктово-ягодный чай", callback_data="fruit_berry")
    keyboard.add(black_berry, fruit_berry)
    
    bot.send_message(message.chat.id, """🫖 Какой чай ты предпочитаешь пить?""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["black_berry", "fruit_berry"]) 
def callback_inline13(call):
    chat_id = call.message.chat.id
    if call.message: 
        if call.data == "black_berry":
            photo_path = "Tea_black_berry.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Сила Сибири* 🍵

 *Состав:*
- Лапсанг сушонг
- Ягоды можевельнека
- Боярышник
- Сосновые почки
- Листья смородины
- Клюква
- Ароматические масла
""", parse_mode="Markdown")
            ask_for_rating(call.message, "black_berry")
            
        elif call.data == "fruit_berry":
            photo_path = "Tea_fruit_berry.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(call.message.chat.id, photo)
            bot.send_message(chat_id, """🍵 *Граф Орлов* 🍵
Напиток назван в честь российского графа Орлова, который предпочитал чёрный чай с  добавками

*Состав:*
- Листья чёрного индийского чая
- Лепестки василька
- Листья сафлоры
- Ягоды  красной смородины
- Малина 
""", parse_mode="Markdown")
            ask_for_rating(call.message, "fruit_berry")

def menu11(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu1 = types.KeyboardButton("""Главное меню""")
    other = types.KeyboardButton("""Другое - это что?""")
    keyboard.add(menu1, other)
    menu12(message)

def menu12(message):
    if(message.text == """📒 Главное меню"""):
        start(message)

    elif(message.text == """🔧 Другое - это что?"""):
        
        bot.send_message(message.chat.id, text="""*1. Для чего вы будете пить чай?*
Например, другое может быть:
•	Для бодрости 
•	Для сна
•	Для сосредоточения
•	Усталость (вялость)
•	…
•	И так далее


*2. Особенности чая*
Например, другое может быть:
•	Вкусный запас
•	На основе ягод
•	…
•	Нет особенностей

""", parse_mode="Markdown")
        return

def test(message):
    user_id = message.from_user.id
    
    keyboard = types.InlineKeyboardMarkup()
    yes_11 = types.InlineKeyboardButton(text="Да", callback_data="yes_11")
    
    no_11 = types.InlineKeyboardButton(text="Нет", callback_data="no_11")
    
    keyboard.add(yes_11, no_11)
    
    bot.send_message(message.chat.id, """🤔 Готов узнать какой ты чай?""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["yes_11", "no_11"]) 
def callback_inline14(call):
    chat_id = call.message.chat.id
    user_id = call.message.from_user.id
    
    if call.message: 
        if call.data == "yes_11":
            test11(call.message)
            
        elif call.data == "no_11":
            bot.send_message(chat_id, """Главное меню""")
            mode1(call.message)

def test11(message):
    user_id = message.from_user.id

    photo_path = "Tea_collage.jpg"
    with open(photo_path, "rb") as photo:
        bot.send_photo(message.chat.id, photo)

    
    keyboard = types.InlineKeyboardMarkup()
    forest = types.InlineKeyboardButton(text="1", callback_data="forest")
    
    chinese = types.InlineKeyboardButton(text="2", callback_data="chinese")
    
    indian = types.InlineKeyboardButton(text="3", callback_data="indian")
    
    savana = types.InlineKeyboardButton(text="4", callback_data="savana")
    
    city = types.InlineKeyboardButton(text="5", callback_data="city")
    
    spring = types.InlineKeyboardButton(text="6", callback_data="spring")
    
    winter = types.InlineKeyboardButton(text="7", callback_data="winter")
    
    undefined = types.InlineKeyboardButton(text="8", callback_data="undefined")
    keyboard.add(forest, chinese, indian, savana, city, spring, winter, undefined)
    
    bot.send_message(message.chat.id, """🌄 Какая картинка больше тебе откликается?""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["forest", "chinese", "indian", "savana", "city", "spring", "winter", "undefined"]) 
def callback_inline14(call):
    chat_id = call.message.chat.id
    user_id = call.message.from_user.id
    
    if call.message: 
        if call.data == "forest":
            test_points[user_id] = test_points.get(user_id, 0) + 8
            
        elif call.data == "chinese":
            test_points[user_id] = test_points.get(user_id, 0) + 7

        elif call.data == "indian":
            test_points[user_id] = test_points.get(user_id, 0) + 6
            
        elif call.data == "city":
            test_points[user_id] = test_points.get(user_id, 0) + 5

        elif call.data == "spring":
            test_points[user_id] = test_points.get(user_id, 0) + 4
            
        elif call.data == "winter":
            test_points[user_id] = test_points.get(user_id, 0) + 3

        elif call.data == "savana":
            test_points[user_id] = test_points.get(user_id, 0) + 2
            
        elif call.data == "undefined":
            test_points[user_id] = test_points.get(user_id, 0) + 1
            
    test2(call.message)

def test2(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    friendly = types.InlineKeyboardButton(text="Дружелюбный", callback_data="friendly")
    
    wisdom = types.InlineKeyboardButton(text="Мудрость", callback_data="wisdom")
    
    calm = types.InlineKeyboardButton(text="Спокойствие", callback_data="calm")
    
    relax = types.InlineKeyboardButton(text="Расслабленность", callback_data="relax")
    
    polite = types.InlineKeyboardButton(text="Вежливость", callback_data="polite")
    
    energy = types.InlineKeyboardButton(text="Энергичность", callback_data="energy")
    
    intelegence = types.InlineKeyboardButton(text="Высший разум", callback_data="intelegence")
    
    closure = types.InlineKeyboardButton(text="Замкнутость", callback_data="closure")
    keyboard.add(friendly, wisdom, calm, relax, polite, energy, intelegence, closure)
    
    bot.send_message(message.chat.id, """🔤 Каким словом ты себя охарактеризуешь?""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["friendly", "wisdom", "calm", "relax", "polite", "energy", "intelegence", "closure"]) 
def callback_inline15(call):
    chat_id = call.message.chat.id
    user_id = call.message.from_user.id
    
    if call.message: 
        if call.data == "friendly":
            test_points[user_id] = test_points.get(user_id, 0) + 8
            
        elif call.data == "wisdom":
             test_points[user_id] = test_points.get(user_id, 0) + 7

        elif call.data == "calm":
            test_points[user_id] = test_points.get(user_id, 0) + 6
            
        elif call.data == "relax":
           test_points[user_id] = test_points.get(user_id, 0) + 5

        elif call.data == "polite":
            test_points[user_id] = test_points.get(user_id, 0) + 4
            
        elif call.data == "energy":
            test_points[user_id] = test_points.get(user_id, 0) + 3

        elif call.data == "intelegence":
           test_points[user_id] = test_points.get(user_id, 0) + 2
            
        elif call.data == "closure":
           test_points[user_id] = test_points.get(user_id, 0) + 1
            
    test3(call.message)

def test3(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    laziness = types.InlineKeyboardButton(text="Флегматик", callback_data="laziness")
    
    joy = types.InlineKeyboardButton(text="Сангвиник", callback_data="joy")
    
    anger = types.InlineKeyboardButton(text="Холерик", callback_data="anger")
    
    sadness = types.InlineKeyboardButton(text="Меланхолик", callback_data="sadness")
    
    not_me = types.InlineKeyboardButton(text="Это не про меня", callback_data="not_me")
    keyboard.add(laziness, joy, anger, sadness, not_me)
    
    bot.send_message(message.chat.id, """🎚 Какой у тебя темперамент?""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["laziness", "joy", "anger", "sadness", "not_me"]) 
def callback_inline16(call):
    chat_id = call.message.chat.id
    user_id = call.message.from_user.id
    
    if call.message: 
        if call.data == "laziness":
            test_points[user_id] = test_points.get(user_id, 0) + 5
            
        elif call.data == "joy":
             test_points[user_id] = test_points.get(user_id, 0) + 4

        elif call.data == "anger":
            test_points[user_id] = test_points.get(user_id, 0) + 3
            
        elif call.data == "sadness":
           test_points[user_id] = test_points.get(user_id, 0) + 2

        elif call.data == "not_me":
            test_points[user_id] = test_points.get(user_id, 0) + 1
            
    test4(call.message)

def test4(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    bagel = types.InlineKeyboardButton(text="Сушки", callback_data="bagel")
    
    nothing = types.InlineKeyboardButton(text="Ничего", callback_data="nothing")
    
    honey = types.InlineKeyboardButton(text="Халва/мед", callback_data="honey")
    
    water = types.InlineKeyboardButton(text="Воду", callback_data="water")
    
    sandwitch = types.InlineKeyboardButton(text="Выпечка", callback_data="sandwitch")

    chocolate = types.InlineKeyboardButton(text="Шоколад", callback_data="chocolate")
    
    cookie = types.InlineKeyboardButton(text="Печенье", callback_data="cookie")
    
    anything = types.InlineKeyboardButton(text="Все", callback_data="anything")
    keyboard.add(bagel, nothing, honey, water, sandwitch, chocolate, cookie, anything)
    
    bot.send_message(message.chat.id, """🍪 Что ты обычно ешь с чаем?""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["bagel", "nothing", "honey", "water", "sandwitch", "chocolate", "cookie", "anything"]) 
def callback_inline17(call):
    chat_id = call.message.chat.id
    user_id = call.message.from_user.id
    
    if call.message: 
        if call.data == "bagel":
            test_points[user_id] = test_points.get(user_id, 0) + 8
            
        elif call.data == "nothing":
             test_points[user_id] = test_points.get(user_id, 0) + 7

        elif call.data == "honey":
            test_points[user_id] = test_points.get(user_id, 0) + 6
            
        elif call.data == "water":
           test_points[user_id] = test_points.get(user_id, 0) + 5

        elif call.data == "sandwitch":
            test_points[user_id] = test_points.get(user_id, 0) + 4

        elif call.data == "chocolate":
            test_points[user_id] = test_points.get(user_id, 0) + 3
            
        elif call.data == "cookie":
           test_points[user_id] = test_points.get(user_id, 0) + 2

        elif call.data == "anything":
            test_points[user_id] = test_points.get(user_id, 0) + 1
            
    test5(call.message)

def test5(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton(text="Да", callback_data="yes")
    no = types.InlineKeyboardButton(text="Нет", callback_data="no")
    keyboard.add(yes, no)
    
    bot.send_message(message.chat.id, """🧂 Пьешь чай с сахаром?""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["yes", "no"]) 
def callback_inline18(call):
    chat_id = call.message.chat.id
    user_id = call.message.from_user.id
    
    if call.message: 
        if call.data == "yes":
            test_points[user_id] = test_points.get(user_id, 0) + 1
            
        elif call.data == "no":
             test_points[user_id] = test_points.get(user_id, 0) + 5
            
    test6(call.message)

def test6(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    tea2 = types.InlineKeyboardButton(text="Чай", callback_data="tea2")
    
    water1 = types.InlineKeyboardButton(text="Вода", callback_data="water1")
    
    milk1 = types.InlineKeyboardButton(text="Молоко", callback_data="milk1")
    
    juice = types.InlineKeyboardButton(text="Сок", callback_data="juice")
    
    cocao = types.InlineKeyboardButton(text="Какао", callback_data="cocao")
    
    air = types.InlineKeyboardButton(text="Воздух", callback_data="air")
    
    coffee = types.InlineKeyboardButton(text="Кофе", callback_data="coffee")
    
    no_list = types.InlineKeyboardButton(text="Нет в списке", callback_data="no_list")
    keyboard.add(tea2, water1, milk1, juice, cocao, air, coffee, no_list)
    
    bot.send_message(message.chat.id, """🧋 Твой любимый напиток?""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["tea2", "water1", "milk1", "juice", "cocao", "air", "coffee", "no_list"]) 
def callback_inline19(call):
    chat_id = call.message.chat.id
    user_id = call.message.from_user.id
    
    if call.message: 
        if call.data == "tea2":
            test_points[user_id] = test_points.get(user_id, 0) + 8
            
        elif call.data == "water1":
             test_points[user_id] = test_points.get(user_id, 0) + 7

        elif call.data == "milk1":
             test_points[user_id] = test_points.get(user_id, 0) + 6

        elif call.data == "juice":
             test_points[user_id] = test_points.get(user_id, 0) + 3

        elif call.data == "cocao":
             test_points[user_id] = test_points.get(user_id, 0) + 4

        elif call.data == "air":
             test_points[user_id] = test_points.get(user_id, 0) + 5

        elif call.data == "coffee":
             test_points[user_id] = test_points.get(user_id, 0) + 1

        elif call.data == "no_list":
             test_points[user_id] = test_points.get(user_id, 0) + 2
            
    test7(call.message)

def test7(message):
    user_id = message.from_user.id

    keyboard = types.InlineKeyboardMarkup()
    tea3 = types.InlineKeyboardButton(text="Чай", callback_data="tea3")
    
    only_tea = types.InlineKeyboardButton(text="Однозначно чай", callback_data="only_tea")
    
    teeeaa = types.InlineKeyboardButton(text="Чаааааай", callback_data="teeeaa")
    
    no_matter = types.InlineKeyboardButton(text="Без разницы", callback_data="no_matter")
    
    coffee1 = types.InlineKeyboardButton(text="Кофе", callback_data="coffee1")
    
    nothing1 = types.InlineKeyboardButton(text="Ни то, ни другое", callback_data="nothing1")
    keyboard.add(tea3, only_tea, teeeaa, no_matter, coffee1, nothing1)
    
    bot.send_message(message.chat.id, """🫖 Кофе или чай?""", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ["tea3", "only_tea", "teeeaa", "no_matter", "coffee1", "nothing1"]) 
def callback_inline20(call):
    chat_id = call.message.chat.id
    user_id = call.message.from_user.id
    
    if call.message: 
        if call.data == "tea3":
            test_points[user_id] = test_points.get(user_id, 0) + 6
            
        elif call.data == "only_tea":
             test_points[user_id] = test_points.get(user_id, 0) + 5

        elif call.data == "teeeaa":
             test_points[user_id] = test_points.get(user_id, 0) + 4

        elif call.data == "no_matter":
             test_points[user_id] = test_points.get(user_id, 0) + 3

        elif call.data == "coffee1":
             test_points[user_id] = test_points.get(user_id, 0) + 1

        elif call.data == "nothing1":
             test_points[user_id] = test_points.get(user_id, 0) + 2
            
    test8(call.message)

def test8(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    
    if message: 
        if test_points[user_id] >= 46:
            photo_path = "Tea_test1.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(message.chat.id, photo)
            bot.send_message(chat_id, """🌲 *Сила Сибири (Русский чай)* 🌲
Ты обладаешь великой силой и физической и духовной. Ты вынослив и способен на многое. Только терпение и труд и ты догтигнешь статуса Всемогущего чая
""", parse_mode="Markdown")
              
        elif test_points[user_id] >= 40:
            photo_path = "Tea_test2.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(message.chat.id, photo)
            bot.send_message(chat_id, """🏮 *Пуэр (Китайский чай)* 🏮
Ты великий мудрец чая. Если ты предашься весь чаюведенью, то ты станешь Высшим разумом
""", parse_mode="Markdown")

        elif test_points[user_id] >= 34:
            photo_path = "tea_test3.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(message.chat.id, photo)
                bot.send_message(chat_id, """🪷 *Масала-чай (Индийский чай)* 🪷
У тебя энергичная, жизнрадостная личность. Ты скорее любишь лето, тепло, яркие цвета и танцы. Делай то, что душа просит и ты станешь самым чайным чаем из всех чаев
""", parse_mode="Markdown")

        elif test_points[user_id] >= 28:
            photo_path = "Tea_test4.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(message.chat.id, photo)
                bot.send_message(chat_id, """🧘‍♂ *Маринованный чай (Лахпет)* 🧘‍♂️
Ты максимально на кайфе все время. Ты не знаешь слова шок или удивление, но зато ты легко переносишь любую стрессовую ситуацию. Не будешь будешь - станешь таким же
""", parse_mode="Markdown")

        elif test_points[user_id] >= 22:
            photo_path = "Tea_test5.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(message.chat.id, photo)
                bot.send_message(chat_id, """🎩 *English breakfast tea (Английский чай)* 🎩
Ты достаточно строг и пунктуален, что только украшает твою личность. Ты перфекционист во всем. Остнешься таким же и любая наука тебе не проблема
""", parse_mode="Markdown")

        elif test_points[user_id] >= 18:
            photo_path = "Tea_test6.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(message.chat.id, photo)
                bot.send_message(chat_id, """🍃 *Сенча (Зеленый чай)* 🍃
Бодрость и энергичность - все про тебя. Многие даже считают тебя гиперактивным, ведь усталость не про тебя. Стань активированным чаем!
""", parse_mode="Markdown")

        elif test_points[user_id] >= 13:
            photo_path = "Tea_test7.png"
            with open(photo_path, "rb") as photo:
                bot.send_photo(message.chat.id, photo)
                bot.send_message(chat_id, """💧 *Вода* 💧
H2O — химическое вещество, представляющее собой бинарное неорганическое соединение, молекула которого состоит из двух атомов водорода и одного атома кислорода, соединённых между собой ковалентной связью
Ты не на чьей стороне, у тебя своя сторона

_между кофем и чаем_
""", parse_mode="Markdown")

        elif test_points[user_id] >= 8:
            photo_path = "Tea_test8.jpg"
            with open(photo_path, "rb") as photo:
                bot.send_photo(message.chat.id, photo)
                bot.send_message(chat_id, """☕️ *Кофе* ☕️
ААА Ты не чай! Ты нечто другое - ты Великое кофе
""", parse_mode="Markdown")



def ask_for_rating(message, tea_type=None):
    keyboard = types.InlineKeyboardMarkup()
    yes_btn = types.InlineKeyboardButton(text="Да", callback_data=f"rate_yes_{tea_type}")
    no_btn = types.InlineKeyboardButton(text="Нет", callback_data=f"rate_no_{tea_type}")
    rating_btn = types.InlineKeyboardButton(text="Рейтинг", callback_data=f"rate_show_{tea_type}")
    keyboard.add(yes_btn, no_btn, rating_btn)
    bot.send_message(message.chat.id, "⭐️ Хотите оценить этот чай?", reply_markup=keyboard)

def ask_for_rating1(message, tea_type=None):
    keyboard = types.InlineKeyboardMarkup()
    for i in range(1, 11):
        button = types.InlineKeyboardButton(text=str(i), callback_data=f"rating_{tea_type}_{i}")
        keyboard.add(button)
    bot.send_message(message.chat.id, "🌟 Поставьте чаю оценку от 1 до 10:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith(('rate_yes_', 'rate_no_', 'rate_show_', 'rating_')))
def handle_rating_callback(call):
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    data = call.data.split('_')
    
    if data[0] == 'rate':
        tea_type = data[2] if len(data) > 2 else None
        
        if data[1] == 'yes':
            ask_for_rating1(call.message, tea_type)
        elif data[1] == 'no':
            bot.send_message(chat_id, """🛰Напиши /start , чтобы выйти на главное меню""")
        elif data[1] == 'show':
            avg_rating = calculate_average_rating(tea_type)
            bot.send_message(chat_id, f"""📊 Средний рейтинг чая: {avg_rating:.1f}""")
    
    elif data[0] == 'rating':
        tea_type = data[1]
        rating = int(data[2])
        rating_user1.setdefault(user_id, {})[tea_type] = rating
        save_rating()
        bot.send_message(chat_id, f"""🏅 Вы поставили оценку: {rating}""")

        
def calculate_average_rating(tea_type):
    ratings = []
    for user_ratings in rating_user1.values():
        if tea_type in user_ratings:
            ratings.append(user_ratings[tea_type])
    return round(sum(ratings) / len(ratings), 1) if ratings else 0

def save_rating():
    with open(r_file, 'w', encoding='utf-8') as f:
        for user_id, ratings in rating_user1.items():
            for tea_type, rating in ratings.items():
                f.write(f"""{user_id}:{tea_type}:{rating}\n""")

@bot.message_handler(content_types=['text'])
def get_text(message):
    if(message.text == """📒 Главное меню"""):
        start(message)

    elif(message.text == """🔧 Другое - это что?"""):
        
        bot.send_message(message.chat.id, text="""*1. Для чего вы будете пить чай?*
Например, другое может быть:
•	Для бодрости 
•	Для сна
•	Для сосредоточения
•	Усталость (вялость)
•	…
•	И так далее


*2. Особенности чая*
Например, другое может быть:
•	Вкусный запас
•	На основе ягод
•	…
•	Нет особенностей

""", parse_mode="Markdown")

        
load_rating()

bot.polling(none_stop=True)
