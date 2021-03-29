'''
first we make big lists of dicts according to stock symbol
then we find average of each
compare each to find highest and lowest
when its highest find date
when lowest find date
finally compare all three max/min dicts
get high/low of all price and the date
write to console and text file(append) all these data points
'''


import csv


stocks = []
aapl_stocks = []
ibm_stocks = []
msft_stocks = []
unknown_stocks = []

#opens the csv file
with open('stocks_data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    
    #sort the csv file into 4 lists of dicts according to the stock
    for row in csv_reader:
        if row['Symbol'] == "AAPL":
            aapl_stocks.append({
                'Symbol': row['Symbol'],
                'Date': row['Date'],
                'Price': row['Adj Close']
            })

        elif row['Symbol'] == "IBM":
            ibm_stocks.append({
                'Symbol': row['Symbol'],
                'Date': row['Date'],
                'Price': row['Adj Close']
            })

        elif row['Symbol'] == "MSFT":
            msft_stocks.append({
                'Symbol': row['Symbol'],
                'Date': row['Date'],
                'Price': row['Adj Close']
            })

        else:
            unknown_stocks.append({
                'Symbol': row['Symbol'],
                'Date': row['Date'],
                'Price': row['Adj Close']
            })

#finds the high by iterating through dict and comparing each value
#also creates a count of how many of each script
aapl_stock_high = 0
aapl_stock_total = 0
aapl_stock_total_count = 0
aapl_stock_low = 1000
for dic in aapl_stocks:
    if float(dic['Price']) > aapl_stock_high:
        aapl_stock_high = float(dic['Price'])
        aapl_stock_total += float(dic['Price'])
        aapl_stock_total += 1
        aapl_stock_high_dict = dic

    else:
        if float(dic['Price']) < aapl_stock_low:
            aapl_stock_low = float(dic['Price'])
            aapl_stock_total += float(dic['Price'])
            aapl_stock_total_count += 1
            aapl_stock_low_dict = dic
            
        else:
            aapl_stock_total += float(dic['Price'])
            aapl_stock_total_count += 1

aapl_stock_average = aapl_stock_total / aapl_stock_total_count
aapl_stock_high_date = aapl_stock_high_dict["Date"]
aapl_stock_low_date = aapl_stock_low_dict["Date"]

#repeats for ibm
ibm_stock_high = 0
ibm_stock_total = 0
ibm_stock_total_count = 0
ibm_stock_low = 1000
for dic in ibm_stocks:
    if float(dic['Price']) > ibm_stock_high:
        ibm_stock_high = float(dic['Price'])
        ibm_stock_total += float(dic['Price'])
        ibm_stock_total += 1
        ibm_stock_high_dict = dic

    else:
        if float(dic['Price']) < ibm_stock_low:
            ibm_stock_low = float(dic['Price'])
            ibm_stock_total += float(dic['Price'])
            ibm_stock_total_count += 1
            ibm_stock_low_dict = dic
            
        else:
            ibm_stock_total += float(dic['Price'])
            ibm_stock_total_count += 1

ibm_stock_average = ibm_stock_total / ibm_stock_total_count
ibm_stock_high_date = ibm_stock_high_dict["Date"]
ibm_stock_low_date = ibm_stock_low_dict["Date"]

#repeats for msft
msft_stock_high = 0
msft_stock_total = 0
msft_stock_total_count = 0
msft_stock_low = 1000
for dic in msft_stocks:
    if float(dic['Price']) > msft_stock_high:
        msft_stock_high = float(dic['Price'])
        msft_stock_total += float(dic['Price'])
        msft_stock_total += 1
        msft_stock_high_dict = dic

    else:
        if float(dic['Price']) < msft_stock_low:
            msft_stock_low = float(dic['Price'])
            msft_stock_total += float(dic['Price'])
            msft_stock_total_count += 1
            msft_stock_low_dict = dic
            
        else:
            msft_stock_total += float(dic['Price'])
            msft_stock_total_count += 1

msft_stock_average = msft_stock_total / msft_stock_total_count
msft_stock_high_date = msft_stock_high_dict["Date"]
msft_stock_low_date = msft_stock_low_dict["Date"]

all_stock_high_list = (aapl_stock_high_dict, ibm_stock_high_dict, msft_stock_high_dict)
highest = 0
for dic in all_stock_high_list:
    if float(dic["Price"]) > highest:
        highest = dic
    else:
        pass
    
all_stock_low_list = (aapl_stock_low, ibm_stock_low, msft_stock_low)
lowest = 1000
for dic in all_stock_low_list:
    if float(dic["Price"]) < lowest:
        lowest = dic
    else:
        pass

all_stock_max = (max(
    float(aapl_stock_high_dict['Price']), 
    float(ibm_stock_high_dict['Price']), 
    float(msft_stock_high_dict['Price'])
))

all_stock_low = (min(
    float(aapl_stock_low_dict['Price']), 
    float(ibm_stock_low_dict['Price']), 
    float(msft_stock_low_dict['Price'])
))

print(lowest)
print(f"\nAAPL \n----")
print(f"Max: {aapl_stock_high} on {aapl_stock_high_date}.")
print(f"Min: {aapl_stock_low} on {aapl_stock_low_date}.")
print(f"Average: {aapl_stock_average}.")

print(f"\nIBM \n----")
print(f"Max: {ibm_stock_high} on {ibm_stock_high_date}.")
print(f"Min: {ibm_stock_low} on {ibm_stock_low_date}.")
print(f"Average: {ibm_stock_average}.")

print(f"\nMSFT \n----")
print(f"Max: {msft_stock_high} on {msft_stock_high_date}.")
print(f"Min: {msft_stock_low} on {msft_stock_low_date}.")
print(f"Average: {msft_stock_average}.")

print(f"\nHighest: ")
print(f"Lowest: ")

with open("stock_summary.txt", "a") as txt_file:
    print(f"\nAAPL \n----", file=txt_file)
    print(f"Max: {aapl_stock_high} on {aapl_stock_high_date}.", file=txt_file)
    print(f"Min: {aapl_stock_low} on {aapl_stock_low_date}.", file=txt_file)
    print(f"Average: {aapl_stock_average}.", file=txt_file)

    print(f"\nIBM \n----", file=txt_file)
    print(f"Max: {ibm_stock_high} on {ibm_stock_high_date}.", file=txt_file)
    print(f"Min: {ibm_stock_low} on {ibm_stock_low_date}.", file=txt_file)
    print(f"Average: {ibm_stock_average}.", file=txt_file)

    print(f"\nMSFT \n----", file=txt_file)
    print(f"Max: {msft_stock_high} on {msft_stock_high_date}.", file=txt_file)
    print(f"Min: {msft_stock_low} on {msft_stock_low_date}.", file=txt_file)
    print(f"Average: {msft_stock_average}.", file=txt_file)

    print(f"\nHighest: ", file=txt_file)
    print(f"Lowest: ", file=txt_file)

