import json
import urllib
import datetime


def main():
    """ Set destination
    """
    flyFrom = 'PRG'  # Prague
    flyTo = 'TPS'  # Palermo

    dateFrom = '30/06/2017'
    dateTo = '30/04/2018'

    days = [7, 10, 14, 16, 18]

    """ Core
    """
    url_list = URL_builder(flyFrom, flyTo, dateFrom, dateTo, days)
    data_table = URL_loader(url_list)


    """ Creating .csv file
    """
    fn = []
    fn.append(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S_')) # Date prefix for filename
    fn.append(flyFrom + "-" + flyTo) # File locations
    fn.append(".csv")
    fn = ''.join(fn)

    file = open(fn, "w")
    for element in data_table:
        file.write(str(element.get('price')) + ", ")
        file.write(str(element.get('range')) + ", ")
        file.write(element.get('dateFrom') + ", ")
        file.write(element.get('dateTo') + ", ")
        file.write(element.get('url') + ", ")
        file.write("\n")
    file.close()



""" Creates the URL for request
"""
def URL_builder(airportDeparture, airportArrival, dateFrom, dateTo, period):

    dateStart = datetime.datetime.strptime(dateFrom, "%d/%m/%Y")
    dateEnd = datetime.datetime.strptime(dateTo, "%d/%m/%Y")


    # TODO Catch exception?
    # TODO This can be check sooner
    if dateStart < dateEnd:
        URL_list = []
        for currentDayRange in period:
            tempDateStart = dateStart

            #If current loop date for certain day range is less or equel to End date
            while tempDateStart <= dateEnd:

                # tempDateEnd = tempDateStart + current_period
                tempDateEnd = tempDateStart + datetime.timedelta(days=currentDayRange)

                tDS = str(tempDateStart.strftime("%d/%m/%Y"))
                tDE = str(tempDateEnd.strftime("%d/%m/%Y"))

                l = []
                l.append("https://api.skypicker.com/flights?")
                l.append("flyFrom=")
                l.append(airportDeparture)
                l.append("&")
                l.append("to=")
                l.append(airportArrival)
                l.append("&")
                l.append("dateFrom=")
                l.append(tDS)
                l.append("&")
                l.append("dateTo=")
                l.append(tDS)
                l.append("&")
                l.append("returnFrom=")
                l.append(tDE)
                l.append("&")
                l.append("returnTo=")
                l.append(tDE)
                l.append("&")
                l.append("limit=1")
                l.append("&")
                l.append("partner=picky")
                s = ''.join(l)

                record = {
                    "dateFrom": tDS,
                    "dateTo": tDE,
                    "url": s,
                    "range": currentDayRange
                     }

                URL_list.append(record)
                #print(record)

                # tempDateStart = +1 day
                tempDateStart = tempDateStart + datetime.timedelta(days=1)

        return URL_list
    else:
        print("INCORRECT DATES")



""" Simple function for retrieving JSON object of requested URL
    :param URL: 
    :return JSON object:
"""
def return_url_json(URL):
    try:
        return json.loads(urllib.urlopen(URL).read())
    except:
        print('Exception occurred while handling URL request:')
        print('-' *100)
        raise



""" Loads list of URLs and loop over it. Request data from URL and process retrieved data. Requiered information are 
    padded to new list. Function return new list with all requested information.
    :param url_list: 
    :return new_url_list: 
"""
def URL_loader(url_list):

    new_url_list = []
    # TODO This 2 following rows needs to be shorten - find one line solution
    for url_row in url_list:
         #print("DateFrom: {} , DateTo: {}, URL: {}".format(url_row["dateFrom"],url_row["dateTo"],url_row["url"]))
         request_data = return_url_json(url_row["url"])
         #print(request_data)

         if int(request_data['_results']) != 0:
             price = request_data['data'][0]['price']
             print("DateFrom: {}, DateTo: {}, Price: {}, Range: {}".format(url_row["dateFrom"], url_row["dateTo"], price, url_row["range"]))

             record = {
                 "dateFrom": url_row["dateFrom"],
                 "dateTo": url_row["dateTo"],
                 "url": url_row["url"],
                 "price": price,
                 "range": url_row["range"]
             }

             new_url_list.append(record)

    print(new_url_list)
    return new_url_list

main()
