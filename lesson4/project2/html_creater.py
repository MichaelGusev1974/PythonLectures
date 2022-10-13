from user_interface import temperature_view
from user_interface import preassure_view
from user_interface import wind_speed_view

def create(divice = 1):
    style = 'style="font-size:20px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '       <p {}>Temperature: {} c</p> \n'\
        .format(style, temperature_view(divice))
    html += '       <p {}>wind_speed: {} m/s</p> \n' \
        .format(style, wind_speed_view(divice))
    html += '       <p {}>preassure: {} mmHg</p> \n' \
        .format(style, preassure_view(divice))
    html += '</body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html

def new_create(data, divice = 1):
    t, p, w = data
    style = 'style="font-size:22px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '       <p {}>Temperature: {} c</p> \n'\
        .format(style, t)
    html += '       <p {}>wind_speed: {} m/s</p> \n' \
        .format(style, w)
    html += '       <p {}>preassure: {} mmHg</p> \n' \
        .format(style, p)
    html += '</body>\n</html>'

    with open('new_index.html', 'w') as page:
        page.write(html)

    return data