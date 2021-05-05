import csv

def writeCSV():
    with open('puma_price.csv', mode='w') as puma_price:
        employee_writer = csv.writer(puma_price, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)


if __name__ == '__main__':
    writeCSV()
