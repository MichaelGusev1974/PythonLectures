from user_interface import temperature_view
from user_interface import preassure_view
from user_interface import wind_speed_view

def create(divice = 1):
    xml = '<xml>\n'
    xml += '      <temperature units = "c">{}</temperature>\n' \
        .format(temperature_view(divice))
    xml += '      <wind_speed units = "m/s">{}</wind_speed>\n' \
        .format(wind_speed_view(divice))
    xml += '      <preassure units = "mmHg">{}</preassure>\n' \
        .format(preassure_view(divice))
    xml += '</xml>'

    with open('data.xml', 'w') as page:
        page.write(xml)
        return xml

def new_create(data, divice = 1):
    t, p, w = data
    t = t * 1.8 + 32              # перевод из Цельсия в Фаренгейты
    xml = '<xml>\n'
    xml += '      <temperature units = "f">{}</temperature>\n' \
        .format(t)
    xml += '      <wind_speed units = "m/s">{}</wind_speed>\n' \
        .format(w)
    xml += '      <preassure units = "mmHg">{}</preassure>\n' \
        .format(p)
    xml += '</xml>'

    with open('new_data.xml', 'w') as page:
        page.write(xml)
        return data