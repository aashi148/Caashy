import requests

def get_inflation(country="India"):
    headers = {'X-Api-Key': 'YOUR_API_KEY'}  # Replace with your API key
    url = f'https://api.api-ninjas.com/v1/inflation?country={country}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print(f"\n📈 Inflation Rate in {country}: {data[0]['inflation_rate']}%")
    else:
        print("Failed to fetch inflation data.")

def get_spending_tip():
    print("\n💡 Tip: Review subscriptions monthly to avoid unused charges.")
