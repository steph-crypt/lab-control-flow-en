total_sales = 0
max_sales = 0

# List representing sales data for seven days (in units)
sales_data = [200, 300, 400, 500, 600, 700, 800]

# Initialize total_sales to 0 before starting the loop
total_sales = 0

# Initialize max_sales before starting the loop
max_sales = 0

for day in sales_data:
    total_sales += day

print("Your total sales are:" + " " + str(total_sales))

if max(sales_data):
    max_sales = day
    index = sales_data.index(max_sales)
print("Your best sales were" + " " + str(max_sales) + " " + "on day" + " " + str(index + 1))

age_bob = 14
age_minimum = 25

if age_bob >= age_minimum:
    print("Bob is old enough to go to the club")
elif 21 < age_bob < age_minimum:
    print("Bob is not old enough to go to this club but he can go to another club called Disco Light")
else:
    print("Bob is not old enough to go to either club")


# Box S (small): weight less than 53 grams.
# Box M (medium) : weight greater than or equal to 53 grams and less than 63 grams.
# Box L (large): weight greater than or equal to 63 grams and less than 73 grams.
# XL box (super large): weight greater than or equal to 73 grams.

egg = 0
box_s = []
box_m = []
box_l = []
box_xl = []

if egg < 53:
    box_s.append(egg)
elif 53 <= egg < 63:
    box_m.append(egg)
elif 63 <= egg < 73:   
    box_l.append(egg)
elif egg >= 73:
    box_xl.append(egg)
print(egg)

