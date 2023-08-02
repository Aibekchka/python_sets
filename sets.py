def print_valid_cities(barlyk_qalalar,atalgan_qalalar):
    oynda_atalmagan_qalalar = barlyk_qalalar.difference(atalgan_qalalar)
    for i in oynda_atalmagan_qalalar:
        print(i)
all_cities = {
    'Алматы',
    'Астана',
    'Шымкент',
    'Актобе',
    'Караганда',
    'Тараз',
    'Павлодар',
    'Семей'
}
used_cities = {'Алматы', 'Семей', 'Караганда'}


def add_cities(all_cities,new_cities):
    for city in new_cities:
        all_cities.add(city)
all_cities = {
    'Алматы',
    'Астана',
    'Шымкент',
    'Актобе',
    'Караганда',
    'Тараз',
    'Павлодар',
    'Семей'
}

new_cities = [
    'Атырау',
    'Кызылорда',
    'Костанай',
    'Актау',
    'Уральск',
    'Петропавловск',
    'Кокшетау'
]
add_cities(all_cities, new_cities)
print_valid_cities(all_cities, used_cities)


def get_together_games(playgame_1,playgame_2):
    return set(playgame_1).intersection(set(playgame_2))
tomiris_games = [
    'Online-chess',
    'Города',
    'Doom',
    'Крестики-нолики'
]
set(tomiris_games).intersection()
alexa_games = [
    'Doom',
    'Online-chess',
    'Города',
    'GTA',
    'World of tanks'
]
together_games = get_together_games(tomiris_games, alexa_games)
for i in together_games:
    print(i)


unique_cities = set(all_cities)
for i in unique_cities:
    print('У меня есть друг в городе',i)





