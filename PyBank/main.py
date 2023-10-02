import os
import csv

budget_csv = os.path.join("PyBank","Resources","budget_data.csv")

budget_data=[]

total_months = len(budget_data)
total_months=0
total_profit_loss=0

profit_loss_change=[]
net_change_list=[]
greatest_increase=["",0]
greatest_decrease=["",99999999999999999999]

with open(budget_csv, newline="") as csvfile:
      csvreader=csv.reader(csvfile)

      next(csvreader)
      first_row=next(csvreader)
      total_months+=1
      total_profit_loss+=int(first_row[1])
      prev_profit_loss=int(first_row[1])


      for row in csvreader:
        total_months +=1
        print(row)
        total_profit_loss+=int(row[1])
        profit_loss_change=int(row[1])-prev_profit_loss
        prev_profit_loss=int(row[1])
        net_change_list+=[profit_loss_change]

        if (profit_loss_change > greatest_increase[1]):
                greatest_increase[0]=row[0]
                greatest_increase[1]=profit_loss_change
                  
        if(profit_loss_change<greatest_decrease[1]):
                greatest_decrease[0]=row[0]
                greatest_decrease[1]=profit_loss_change

average_profit_loss_change=round(total_profit_loss/total_months,2)
print(net_change_list)
net_monthly_avg = round(sum(net_change_list) / len(net_change_list),2)

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit_loss}')
print(f'Average Change: ${net_monthly_avg :.2f}')
print(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
print(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')


budget_csv = os.path.join('PyBank', 'analysis','analysis_results')
with open(budget_csv, "w") as text_file:
        print('Financial Analysis', file=text_file)
        print('----------------------------', file=text_file)
        print(f'Total Months: {total_months}', file=text_file)
        print(f'Total: ${total_profit_loss}', file=text_file)
        print(f'Average Change: ${net_monthly_avg}', file=text_file)
        print(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[0]})', file=text_file)
        print(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[0]})', file=text_file)



