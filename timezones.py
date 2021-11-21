from datetime import datetime
import pytz

CHILE_TIMEZONE = pytz.timezone('America/Santiago')
santiago_date = datetime.now(CHILE_TIMEZONE)

print(santiago_date.strftime('%d/%m/%Y - %H:%M'))