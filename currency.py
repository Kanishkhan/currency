import requests

def convert_currency(amount, from_currency, to_currency, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency.upper()}"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code != 200 or data['result'] != 'success':
        print("Error fetching exchange rates.")
        return None

    rate = data['conversion_rates'].get(to_currency.upper())
    if rate:
        converted_amount = amount * rate
        print(f"{amount} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}")
        return converted_amount
    else:
        print(f"Currency '{to_currency}' not found.")
        return None

# --- Example Usage ---
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Get a free API key from exchangerate-api.com
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Convert from (e.g., USD): ")
    to_currency = input("Convert to (e.g., INR): ")

    convert_currency(amount, from_currency, to_currency, api_key)
