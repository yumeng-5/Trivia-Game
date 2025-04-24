import requests

parameters = {
    'amount': 10,
    'type': 'boolean',
}
quiz = requests.get(url="https://opentdb.com/api.php", params=parameters)
quiz.raise_for_status()

question_data = quiz.json()['results']

