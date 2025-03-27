import telebot 
TOKEN = ' Token from BotFather'
from copy import deepcopy


bot = telebot.TeleBot(TOKEN)




locations = {
    '1':{
        'text':'Ты просыпаешься в темном и запущенном бункере, не помня, как сюда попал. Свет от мерцающей лампы лишь слабо освещает металлические стены, а воздух пахнет старостью и затхлостью. Твои руки нащупывают пыльные поверхности, а шаги раздаются гулко в этой забытой глубине.',
        'items': [],
        'next_move': {'К приключениям': '2'},
        'exchange': {}
        },
    '2':{
        'text':'Ты начинаешь свое путешествие по бункеру, осматривая каждый уголок и исследуя каждую дверь. Перед тобой возникают загадочные механизмы, старые компьютеры и запертые помещения. В поисках ключа к выходу ты сталкиваешься с загадками, которые предстоит разгадать, и препятствиями, которые нужно преодолеть.',
        'items': [],
        'next_move': {'Пойти вперед': '3',
                      'Пойти направо': '4',
                      'Пойти налево': '5'},
        'exchange': {}
        },
    '3':{
        'text': 'Ты понимаешь, что не сможешь найти выход из этого бункера. Тайны и опасности оказались слишком сильными, и ты застрял в этом забытом мире под землей. Твое путешествие заканчивается здесь, и бункер становится твоей темной тюрьмой, лишенной надежды на свободу.',
        'items': [],
        'next_move': {},
        'exchange': {}
        },
    '4':{
        'text': 'Ты продолжаешь свое путешествие по бункеру, и внезапно перед тобой появляется укромное помещение, освещенное мерцающим светом свечей. Ты видишь старинный стол, уставленный различными предметами, и мужчину с длинной бородой, одетого в потрепанный кожаный плащ, который приветствует тебя с улыбкой.',
        'items': [],
        'next_move': {'Выйти обратно': '6'},
        'exchange': {'Сундук': 'Монеты: 3'
}
    },
    '5':{
        'text':'Как только ты подходишь к подземелью, ты ощущаешь холодный ветер, исходящий из его темных глубин. Вокруг царит мрачная тишина, прерываемая лишь слабым шорохом и непонятными звуками. Подземелье манит тебя своей тайной и опасностью, приглашая на встречу с неизведанным. Ты чувствуешь, что внутри скрываются тайны и сокровища, но также и опасности, готовые испытать твою отвагу.',
        'items': [],
        'next_move': {'Осмотреться рядом': '6',
            'Войти в подземелье': '7',
            'Вернуться на развилку': '2'},
        'exchange': {}
    },
    '6':{
        'text':'Путешественник, когда ты осматриваешь местность вокруг подземелья, ты замечаешь, что окружающая местность выглядит угрожающе. Склонившись над входом в подземелье, ты видишь старые каменные ступени, покрытые лишайником, уводящие во тьму. Вдалеке слышится жуткий свист ветра, который словно проникает сквозь трещины в стенах подземелья. Взглянув на окружающую местность, ты замечаешь, что ветви деревьев склонены к земле, словно они уклоняются от чего-то зловещего. Подземелье, кажется, выбрало для себя это место, чтобы скрыть свои тайны от любопытных глаз.',
        'items': ['Сундук'],
        'next_move': {'Вернуться к подземелью': '5'},
        'exchange': {}
    },
    '7':{
        'text':'Когда ты входишь в подземелье, ты ощущаешь, как холодный воздух обволакивает тебя, словно приветствуя тебя в своих объятиях. Темнота становится гуще, лишь слабые лучи света пробиваются сквозь тесные проходы, бросая таинственные тени на стены. Ты слышишь приглушенные звуки из глубины подземелья, словно его собственное сердце бьется в такт с твоими шагами. Где-то вдали виднеется туннель.',
        'items': ['Монеты: 2'],
        'next_move': {'Войти в туннель': '8',
                      'Вернуться на улицу': '5'},
        'exchange': {}
    },
    '8':{
        'text':'Когда ты входишь в туннель и видишь свет в конце, ты ощущаешь, как твои шаги звучат громче в пустоте. Свет в конце туннеля кажется тебе приглашением к новым открытиям и приключениям.',
        'items': [],
        'next_move': {'Пойти на свет': '9',
            'Вернуться назад': '7'},
        'exchange': {}
    },
    '9':{
        'text':'Наконец-то, вы близки к тому, чтобы покинуть этот мрачный бункер. Но подождите, что это? Единственный выход перекрыт тяжёлой металлической дверью, и чтобы её открыть, вам нужно заплатить охраннику. Обернувшись, вы замечаете, как он внимательно наблюдает за вами, ожидая вашего решения.',
        'items': [],
        'next_move': {'Вернуться в туннель': '8'},
        'exchange': {
            'Монеты: 5': 'выход'
}
    },

}
users_info = {}


def generate_story(user_id):
    # берем локацию, в которой находится игрок
    current_location = users_info[user_id]['cur_pos']
    # получаем текстовое представление локации
    text = locations[current_location]['text']
    keyboard = telebot.types.InlineKeyboardMarkup()
    # перебираем направления из словаря следующих ходов
    for i in locations[current_location]['next_move']:
        # добавляем кнопку с текстом направления и callback_data - название локации
        keyboard.add(telebot.types.InlineKeyboardButton(i, callback_data=locations[current_location]['next_move'][i]))
    for i in users_info[user_id]['loc'][current_location]['items']:
        keyboard.add(telebot.types.InlineKeyboardButton(f'Взять предмет - {i}', callback_data=f'items {i}'))
    # перебираем предметы доступные для обменя в этой локации
    for i in users_info[user_id]['loc'][current_location]['exchange']:
        # проверям что предмет для обмена есть у нас, либо если нужны монеты для обмена, то у нас их достаточно
        if i in users_info[user_id]['items'] or i.startswith('Монеты: ') and int(i.replace('Монеты: ', '')) <= users_info[user_id]['coins']:
            # генерируем текст для кнопки
            text_key = f"Обменять предмет {i} на {users_info[user_id]['loc'][current_location]['exchange'][i]}"
            # генерируем строку для callback_data
            data_key = f'exchange {i}'
            keyboard.add(telebot.types.InlineKeyboardButton(text_key, callback_data=data_key))

    
    
    keyboard.add(
        telebot.types.InlineKeyboardButton('Рюкзак', callback_data='backpack'),
        telebot.types.InlineKeyboardButton('Баланс', callback_data='balance')
    )
    return text, keyboard


@bot.message_handler(commands=['game'])
def start_game(msg):
    # добавляем пользователя в словарь пользователей с начальнами значениями
    # cur_pos - текущая позиция игрока
    # items - предметы в *рюкзаке* у игрока
    # coins - баланс монет
    # loc - глубокая копия словаря локаций
    # message_id - id сообщения бота
    users_info[msg.from_user.id] = {'cur_pos': '1', 'items': [], 'coins': 0, 'loc': deepcopy(locations), 'message_id': None}
    text, keyboard = generate_story(msg.from_user.id)
    msg_bot = bot.send_message(msg.chat.id, text, reply_markup=keyboard)
    # запоминаем id сообщения бота
    users_info[msg.from_user.id]['message_id'] = msg_bot.message_id


@bot.callback_query_handler(func=lambda call: call.data in locations)
def next_move(call):
    # меняем текущую позицию игрока
    users_info[call.from_user.id]['cur_pos'] = call.data
    text, keyboard = generate_story(call.from_user.id)
    # редактируем сообщение бота
    bot.edit_message_text(text, call.message.chat.id, users_info[call.from_user.id]['message_id'], reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call: call.data.startswith('items '))
def get_item(call):
    item = call.data.replace('items ', '')
    if item.startswith('Монеты: '):
        users_info[call.from_user.id]['coins'] += int(item.replace('Монеты: ', ''))
    else:
        users_info[call.from_user.id]['items'].append(item)
    current_position = users_info[call.from_user.id]['cur_pos']
    users_info[call.from_user.id]['loc'][current_position]['items'].remove(item)
    text, keyboard = generate_story(call.from_user.id)
    bot.edit_message_text(text, call.message.chat.id, users_info[call.from_user.id]['message_id'], reply_markup=keyboard)
    bot.answer_callback_query(call.id, f'Вы взяли предмет {item}')
@bot.callback_query_handler(func=lambda call: call.data == 'backpack')
def backpack(call):
    if users_info[call.from_user.id]['items']:
        # выводим список предметов пользователя в уведомлении
        bot.answer_callback_query(call.id, f"Ваши предметы:\n {', '.join(users_info[call.from_user.id]['items'])}", show_alert=True)
    else:
        bot.answer_callback_query(call.id, 'У вас нет предметов')
@bot.callback_query_handler(func=lambda call: call.data == 'balance')
def balance(call):
    bot.answer_callback_query(call.id, f'Ваш баланс: {users_info[call.from_user.id]["coins"]}')
@bot.callback_query_handler(func=lambda call: call.data.startswith('exchange '))
def change_items(call):
    # берем текущую позицию игрока
    current_position = users_info[call.from_user.id]['cur_pos']
    # берем название предмета (который отдаем)
    item_1 = call.data.replace('exchange ', '')
    # берем название предмета (который получаем)
    item_2 = users_info[call.from_user.id]['loc'][current_position]['exchange'][item_1]
    if item_1.startswith('Монеты: '):
        users_info[call.from_user.id]['coins'] -= int(item_1.replace('Монеты: ', ''))
    else:
        users_info[call.from_user.id]['items'].remove(item_1)
   
    if item_2.startswith('Монеты: '):
        users_info[call.from_user.id]['coins'] += int(item_2.replace('Монеты: ', ''))
    else:
        users_info[call.from_user.id]['items'].append(item_2)
   
    users_info[call.from_user.id]['loc'][current_position]['exchange'].pop(item_1)


    if item_2 == 'выход':
        bot.edit_message_text('Ура! Ты выбрался!!!', call.message.chat.id, users_info[call.from_user.id]['message_id'])
    else:
        text, keyboard = generate_story(call.from_user.id)
        # редактируем сообщение бота
        bot.edit_message_text(text, call.message.chat.id, users_info[call.from_user.id]['message_id'], reply_markup=keyboard)
        # показываем, что взяли в уведомлении
        bot.answer_callback_query(call.id, f'Вы обменяли предмет {item_1} на {item_2}')
 
if __name__ == '__main__':
    bot.infinity_polling()
