import requests

init_currency = input("Enter your initial currency: ")
target_currency = input("Enter your target currency: ")

while True:
    try:
        amount = float(input("Enter the amount of money you want to convert: "))
    except ValueError:
        print("The amount must be a numeric value")
        continue

    if amount <= 0:
        print("The amount must be greater than 0")
        continue
    else:
        break

url = (f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}")

payload = {}
headers= {
    "apikey": "DO0QWzMiEQ3r5OcHKd5TyiwmSFBtuRTN"
    } 

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.json()
if response.status_code != 200:
    print("Sorry there is a problem, try again.")
    quit()
result = response.text
print(result)
