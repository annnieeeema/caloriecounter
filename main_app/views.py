from django.shortcuts import render

# apiKey - xURY1NGNvFUgDmNVX1no+w==uRCSd79qlz5t4Kxs
# Create your views here.
def home(request):
    import requests

    query = 'apple'
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'xURY1NGNvFUgDmNVX1no+w==uRCSd79qlz5t4Kxs'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)

    return render(request, 'home.html')