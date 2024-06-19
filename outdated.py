months = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12"
}
date_input = input("Date: ").replace(" ", "/").replace(",", "")
date_input_separated = date_input.split("/")

##### get the final month value
if date_input_separated[0] in months:
    final_month_value = str(months[date_input_separated[0]])
elif int(date_input_separated[0]) < 10:
    final_month_value = str(f"0{date_input_separated[0]}")
else:
    final_month_value = date_input_separated[0]

##### get the final day value
if int(date_input_separated[1]) < 10:
    final_day_value = str(f"0{date_input_separated[1]}")
else:
    final_day_value = str(date_input_separated[1])
    
#### get the final year value
final_year_value = date_input_separated[2]

##output the final date format

print(final_year_value,final_month_value,final_day_value, sep="-")




