#import OS
import os

# import csv to read/work with data file
import csv

#Variables used 
total_profit = 0
total_months = 0
total_change = 0
avg_change = 0
prior_pl = 0
min_change = 0
max_change = 0
min_index = 0
max_index = 0
min_date = 0
max_date = 0
avg_num = 0

mon_date = []
profit_loss_change = []

    

# data path
bdgt_path = os.path.join(".", "Resources", "budget_data.csv")
#setup
with open(bdgt_path) as bdgt_file:
    bdgt_reader = csv.reader(bdgt_file, delimiter = ',')

    #Read the header row
    bdgt_header = next(bdgt_reader)

    #Read each row of data after the header
    for row in bdgt_reader:
       
        total_months += 1
        total_profit += int(row[1])
        mon_date.append(row[0])

        if prior_pl != 0:   
            total_change = int(row[1]) - prior_pl
        
       
        profit_loss_change.append(total_change)
        prior_pl = int(row[1])

    min_change = min(profit_loss_change)
    min_index = profit_loss_change.index(min(profit_loss_change))
    max_change = max(profit_loss_change)
    max_index = profit_loss_change.index(max(profit_loss_change))
    min_date = mon_date[min_index]
    max_date = mon_date[max_index]

    avg_mon = total_months - 1
    
    avg_change = round(sum(profit_loss_change) / avg_mon)

    financial_analysis = (
        f"\Financial Analysis\n"
        f"-----------------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_profit}\n"
        f"Average Change: ${avg_change}\n"
        f"Greatest Increase in Profits: {max_date} (${max_change}\n"
        f"Greatest Decrease in Profits: {min_date} (${min_change})\n")

    print(financial_analysis, end="")

    report = open("fin_analysis.txt", 'w')
    print(financial_analysis, file=report)
    report.close
    
     
          
    
    
    
    

