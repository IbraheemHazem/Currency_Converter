# import requests

# def get_currency_input(prompt):
#     return input(prompt).strip()

# def get_valid_amount():
#     while True:
#         try:
#             amount = float(input("Enter the amount of money you want to convert: "))
#             if amount > 0:
#                 return amount
#             else:
#                 print("The amount must be greater than 0")
#         except ValueError:
#             print("The amount must be a numeric value")

# def convert_currency(init_currency, target_currency, amount):
#     url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"
    
#     payload = {}
#     headers = {
#         "apikey": "DO0QWzMiEQ3r5OcHKd5TyiwmSFBtuRTN"
#     }

#     response = requests.get(url, headers=headers, data=payload)

#     if response.status_code != 200:
#         print("Sorry, there is a problem. Please try again.")
#         quit()

#     return response.text

# def main():
#     init_currency = get_currency_input("Enter your initial currency: ")
#     target_currency = get_currency_input("Enter your target currency: ")
#     amount = get_valid_amount()

#     result = convert_currency(init_currency, target_currency, amount)
#     print(result)

# if __name__ == "__main__":
#     main()











# import requests

# def get_currency_input(prompt):
#     return input(prompt).strip()

# def get_valid_amount():
#     while True:
#         try:
#             amount = float(input("Enter the amount of money you want to convert: "))
#             if amount > 0:
#                 return amount
#             else:
#                 print("The amount must be greater than 0")
#         except ValueError:
#             print("The amount must be a numeric value")

# def convert_currency(init_currency, target_currency, amount):
#     url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"
    
#     payload = {}
#     headers = {
#         "apikey": "DO0QWzMiEQ3r5OcHKd5TyiwmSFBtuRTN"
#     }

#     response = requests.get(url, headers=headers, data=payload)

#     if response.status_code != 200:
#         print("Sorry, there is a problem. Please try again.")
#         return None

#     return response.text

# def main():
#     while True:
#         init_currency = get_currency_input("Enter your initial currency: ")
#         target_currency = get_currency_input("Enter your target currency: ")
#         amount = get_valid_amount()

#         result = convert_currency(init_currency, target_currency, amount)
#         if result:
#             print(result)

#         restart = input("Do you want to convert another currency? (yes/no): ").lower()
#         if restart != 'yes':
#             print("Exiting the currency converter. Goodbye!")
#             break

# if __name__ == "__main__":
#     main()
















# from flask import Flask, request, jsonify
# import requests

# app = Flask(__name__)

# FIXER_API_KEY = "DO0QWzMiEQ3r5OcHKd5TyiwmSFBtuRTN"

# def convert_currency(init_currency, target_currency, amount):
#     url = (f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}")
    
#     params = {
#         "base": init_currency,
#         "symbols": target_currency
#     }

#     response = requests.get(url, params=params)

#     if response.status_code != 200:
#         return None

#     data = response.json()
#     rate = data["rates"].get(target_currency)

#     if rate is None:
#         return None

#     converted_amount = amount * rate
#     return converted_amount

# @app.route('/convert', methods=['POST'])
# def handle_conversion():
#     data = request.get_json()

#     init_currency = data.get('init_currency')
#     target_currency = data.get('target_currency')
#     amount = data.get('amount')

#     if not init_currency or not target_currency or not amount:
#         return jsonify({"error": "Invalid input"}), 400

#     converted_amount = convert_currency(init_currency, target_currency, amount)

#     if converted_amount is None:
#         return jsonify({"error": "Conversion failed"}), 500

#     result = {
#         "init_currency": init_currency,
#         "target_currency": target_currency,
#         "amount": amount,
#         "converted_amount": converted_amount
#     }

#     return jsonify(result)

# if __name__ == "__main__":
#     app.run(debug=True)
