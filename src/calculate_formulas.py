def get_const(product):
    if product == 'Lb': return 0.24
    if product == 'H - 60': return 0.845
    if product == 'H-114 (600)': return 0.6
    if product == 'КД': return 0.226
    if product == 'WS': return 0.33
    if product in ['С - 44', 'С - 21', 'HC -35']: return 1
    if product in ['С - 8', 'С - 10']: return 1.15
    if product in ['МП - 18', 'МП - 20', 'МЧ']: return 1.1
    if product in ['H - 75', 'H-114 (750)']: return 0.75


def calculate(product, const, height, width):
    if product in ['Lb', 'КД', 'WS']:
        if width < 0.5:
            width = 0.5
        if width > 6:
            alert = ' Внимание! Возможная длинна 0.5 - 6м.'
        else:
            alert = ''

        product_count = round(height / const, 2)
        additional1 = round(width / 3, 2)
        additional2 = round(height / 3 * width / 6, 2)
        return f'{product}, Кол-во листов: {product_count}, Длина листа: {width}, Начальная планка: {additional1}, Планка ' \
               f'стыковочная: {additional2};{alert}\n'

    else:
        if height > 12:
            alert = ' Внимание! Возможная длина 0.5 - 12м.'
        else:
            alert = ""

        product_count = round(width / const, 2)
        additional1 = width / 2
        additional2 = width
        additional3 = height * 4 / 2
    return f'{product}, Кол-во листов: {product_count}, Длина листа: {height}, Конёк: {additional1}, Карнизная ' \
           f': {additional2}, Торцевая: {additional3}; {alert}\n'

