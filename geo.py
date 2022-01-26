def geocoding(adresses):
    coord = []
    from geopy.geocoders import Nominatim



    #making an instance of Nominatim class
    geolocator = Nominatim(user_agent="my_request")
    for i in adresses:

    #applying geocode method to get the location
        location = geolocator.geocode(i)
        #coord.append(location)

    #printing address and coordinates
       # print(location.address)
       # print((location.latitude, location.longitude))
        coord.append([location.latitude, location.longitude])

    #print(coord)
    return coord



def get_adres():
    import sqlite3
    adresses=[]
    with sqlite3.connect('db/events.db') as db:
     cursor = db.cursor()
    cursor.execute("SELECT location FROM events")
    title = cursor.fetchall()
    for i in title:
        temp = (i[0])
        temp=str(temp)
        adresses.append(temp)
    #print(adresses)
    return adresses
def get_time():
    import sqlite3
    times=[]
    with sqlite3.connect('db/events.db') as db:
     cursor = db.cursor()
    cursor.execute("SELECT time FROM events")
    title = cursor.fetchall()
    for i in title:
        temp = (i[0])
        temp=str(temp)
        times.append(temp)
    print(times)
    return times


def get_date():
    import sqlite3
    dates=[]
    with sqlite3.connect('db/events.db') as db:
     cursor = db.cursor()
    cursor.execute("SELECT date FROM events")
    title = cursor.fetchall()
    for i in title:
        temp = (i[0])
        temp=str(temp)
        dates.append(temp)
    print(dates)
    return dates

def get_description():
    import sqlite3
    descs=[]
    with sqlite3.connect('db/events.db') as db:
     cursor = db.cursor()
    cursor.execute("SELECT description FROM events")
    title = cursor.fetchall()
    for i in title:
        temp = (i[0])
        temp=str(temp)
        descs.append(temp)
    print(descs)
    return descs

def get_name_event():
    import sqlite3
    names=[]
    with sqlite3.connect('db/events.db') as db:
     cursor = db.cursor()
    cursor.execute("SELECT name FROM events")
    title = cursor.fetchall()
    for i in title:
        temp = (i[0])
        temp=str(temp)
        names.append(temp)
    print(names)
    return names
def get_limitation():
    import sqlite3
    limitss=[]
    with sqlite3.connect('db/events.db') as db:
     cursor = db.cursor()
    cursor.execute("SELECT limitation FROM events")
    title = cursor.fetchall()
    for i in title:
        temp = (i[0])
        temp=str(temp)
        limitss.append(temp)
    print(limitss)
    return limitss

def get_maker():
    import sqlite3
    makers=[]
    with sqlite3.connect('db/events.db') as db:
     cursor = db.cursor()
    cursor.execute("SELECT maker FROM events")
    title = cursor.fetchall()
    for i in title:
        temp = (i[0])
        temp=str(temp)
        makers.append(temp)
    print(makers)
    return makers
def get_participants():
    import sqlite3
    participants = []
    with sqlite3.connect('db/events.db') as db:
     cursor = db.cursor()
    cursor.execute("SELECT participants FROM events")
    title = cursor.fetchall()
    for i in title:
        temp = (i[0])
        temp =str(temp)
        participants.append(temp)

    return participants
