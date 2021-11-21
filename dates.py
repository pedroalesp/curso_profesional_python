from datetime import datetime, date

# # Hora y fecha justa del momento en que se ejecuta la línea de código
# actual_hour = datetime.now()
# print(actual_hour)

# # Fecha de hoy
# today = date.today()
# print(today)

# # Año, mes y día detallados
# year = today.year
# month = today.month
# day = today.day
# print('year:', year, 'month:', month, 'day:', day)

#-------------------------------------------------

todays_date = datetime.now()
print(todays_date)

#formatear a latam
formated_latam_date = todays_date.strftime('%d/%m/%Y')
print(formated_latam_date)

#formatear a USA
formated_usa_date = todays_date.strftime('%m/%d/%Y')
print(formated_usa_date)

#sacar el año, mes o día de la fecha
formated_random_year = todays_date.strftime('%Y')
formated_random_month = todays_date.strftime('%m')

print(f'Estamos en el mes {formated_random_month} del año {formated_random_year}')
