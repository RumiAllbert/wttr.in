import csv

AIRPORTS_DAT_FILE = '/home/igor/wttrin-geo/share/airports.dat'

def load_aiports_index():
    file_ = open(AIRPORTS_DAT_FILE, "r")
    reader = csv.reader(file_)
    return {line[4]: line for line in reader}

AIRPORTS_INDEX = load_aiports_index()

def get_airport_gps_location(iata_code):
    if iata_code in AIRPORTS_INDEX:
        airport = AIRPORTS_INDEX[iata_code]
        return f'{airport[6]},{airport[7]} airport'
    return None

