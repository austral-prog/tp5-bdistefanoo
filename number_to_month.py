# Replace the "ANSWER HERE" for your answer
def number_to_month(month):
    meses = [
        "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"
    ]
    if 1 <= month <= 12:
        return meses[month -1]
    else:
        return "error"
print(number_to_month(1))
