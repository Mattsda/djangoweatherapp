from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']

		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=50&API_KEY=635C8574-084A-49A2-942E-CF3972AB6D8E")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0 to 50) Air Quality is Satisfactory"
			category_color = "good"	

		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51 - 100) Air quality is acceptable"
			category_color = "moderate"	

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101 - 150) Although general public is not likely to be affected, people with lung problems should stay away"
			category_color = "usg"

		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151 - 200) Everyone may begin to experience health effects"
			category_color = "unhealthy"

		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201 - 300) Health alert: everyone may experience serious health effects"
			category_color = "veryunhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(301 - 500) Health warnings of emergency conditions. Entire population is likely to be affected"
			category_color = "hazardous"

		return render(request, 'home.html', {
			'api': api, 
			'category_description': category_description,
			'category_color': category_color
			})


	else:

		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=32960&distance=50&API_KEY=635C8574-084A-49A2-942E-CF3972AB6D8E")

		try:
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		if api[0]['Category']['Name'] == "Good":
			category_description = "(0 to 50) Air Quality is Satisfactory"
			category_color = "good"	

		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "(51 - 100) Air quality is acceptable"
			category_color = "moderate"	

		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
			category_description = "(101 - 150) Although general public is not likely to be affected, people with lung problems should stay away"
			category_color = "usg"

		elif api[0]['Category']['Name'] == "Unhealthy":
			category_description = "(151 - 200) Everyone may begin to experience health effects"
			category_color = "unhealthy"

		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "(201 - 300) Health alert: everyone may experience serious health effects"
			category_color = "veryunhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "(301 - 500) Health warnings of emergency conditions. Entire population is likely to be affected"
			category_color = "hazardous"

		return render(request, 'home.html', {
			'api': api, 
			'category_description': category_description,
			'category_color': category_color
			})


def about(request):
	return render(request, 'about.html', {})
