matches = [
    {
        'home_team': 'Bolivia',
        'away_team': 'Uruguay',
        'home_team_score': 3,
        'away_team_score': 1,
        'home_team_result': 'Win'
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Mexico',
        'home_team_score': 1,
        'away_team_score': 1,
        'home_team_result': 'Draw'
    },
    {
        'home_team': 'Ecuador',
        'away_team': 'Venezuela',
        'home_team_score': 5,
        'away_team_score': 0,
        'home_team_result': 'Win'
    },
]

# Lista Original
print(matches)
print(len(matches))

# Filtra los equipos que han ganado
new_list = list(
    filter(lambda item: item['home_team_result'] == 'Win', matches))

# Lista Filtrada
print(new_list)
print(len(new_list))

# Si imprimimos la Lista Original después de esa modificación, NO DEBERÍA cambiar la Lista Original, solo la Nueva Lista
print(matches)
print(len(matches))
