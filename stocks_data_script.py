'''
this is so bad :(
this doesnt find the date for when the high happens 
doesn't write to a text file either
'''

import csv

#opens the csv file
with open('stocks_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 1
    stocks = {'Symbol': [], 'Date': [], 'Price': []}
    aapl_stocks = {'Symbol': [], 'Date': [], 'Price': []}
    ibm_stocks = {'Symbol': [], 'Date': [], 'Price': []}
    msft_stocks = {'Symbol': [], 'Date': [], 'Price': []}

    #next skips the headers of the csv, that is why line count starts at 1
    next(csv_reader)

    #sort the csv file into 3 dicts according to the stock
    for row in csv_reader:
        if row[0] == "AAPL":
            aapl_stocks['Date'].append(row[1])
            aapl_stocks['Price'].append(float(row[2]))
            line_count += 1

        elif row[0] == "IBM":
            ibm_stocks['Date'].append(row[1])
            ibm_stocks['Price'].append(float(row[2]))
            line_count += 1

        elif row[0] == "MSFT":
            msft_stocks['Date'].append(row[1])
            msft_stocks['Price'].append(float(row[2]))
            line_count += 1
    
    print(f'Processed {line_count} lines.')

#finds the high by iterating through dict and comparing each value
#also creates a count of how many of each script
aapl_stock_high = 0
aapl_stock_total = 0
aapl_stock_total_count = 0
aapl_stock_low = 1000
for value in aapl_stocks["Price"]:
    if value > aapl_stock_high:
        aapl_stock_high = value
        aapl_stock_total += value
        aapl_stock_total_count += 1
    else:
        if value < aapl_stock_low:
            aapl_stock_low = value
            aapl_stock_total += value
            aapl_stock_total_count += 1
        else:
            aapl_stock_total += value
            aapl_stock_total_count += 1

#prints stock high, computes stock average and prints\
print(f"\nAAPL \n---")
print(f"Max: {aapl_stock_high}.")
print(f"Min: {aapl_stock_low}.")
aapl_stock_average = aapl_stock_total / aapl_stock_total_count
print(f"Average: {aapl_stock_average}.")

#repeats for ibm
ibm_stock_high = 0
ibm_stock_total = 0
ibm_stock_total_count = 0
ibm_stock_low = 1000
for value in ibm_stocks["Price"]:
    if value > ibm_stock_high:
        ibm_stock_high = value
        ibm_stock_total += value
        ibm_stock_total_count += 1
    else:
        if value < ibm_stock_low:
            ibm_stock_low = value
            ibm_stock_total += value
            ibm_stock_total_count += 1
        else:
            ibm_stock_total += value
            ibm_stock_total_count += 1
print(f"\nIBM \n---")
print(f"Max: {ibm_stock_high}.")
print(f"Min: {ibm_stock_low}.")
ibm_stock_average = ibm_stock_total / ibm_stock_total_count
print(f"Average: {ibm_stock_average}.")

#repeats for msft
msft_stock_high = 0
msft_stock_total = 0
msft_stock_total_count = 0
msft_stock_low = 1000
for value in msft_stocks["Price"]:
    if value > msft_stock_high:
        msft_stock_high = value
        msft_stock_total += value
        msft_stock_total_count += 1
    else:
        if value < msft_stock_low:
            msft_stock_low = value
            msft_stock_total += value
            msft_stock_total_count += 1
        else:
            msft_stock_total += value
            msft_stock_total_count += 1
print(f"\nMSFT \n---")
print(f"Max: {msft_stock_high}.")#place date here
print(f"Min: {msft_stock_low}.")#place date here
msft_stock_average = msft_stock_total / msft_stock_total_count
print(f"Average: {msft_stock_average}.")#place date here



#redundant print of total price

#ignore this something we might need if we have to fundamentally change the whole script
'''
        stocks['symbol'].append(row[0])
        stocks['date'].append(row[1])
        stocks['price'].append(float(row[2]))
'''
