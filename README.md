# Signal
The current url is http://ec2-13-59-254-214.us-east-2.compute.amazonaws.com/. 

## Podcasts
`/podcasts/data`
Get with no query parameters to get a list of all podcast meta data
Get with an id to get a specific podcast
```
{
  _id: {
  $oid: "5cb1b13a5842d645cbf8515f"
  },
  description: "I want to be a billionaire",
  host: "Ariana Grande ",
  title: "7-rings"
}
```

Post with a title, host, and description. Returns a json `{"id": str(podcast.id)}`


`/podcasts/audio` 
Get with a mandatory id query parameter to recieve the podcast audio.

`/podcasts/suggest`
Get with a mandatory id query parameter to recieve suggestions for soundbites
```
[{'start_time': 13793, 
'end_time': 25000,
'transcript': "Why would you do this to me Miss Edision? Because I am the devil"}, 
{'start_time': 49000, 
'end_time': 77777,
'transcript': "Knowing what to read and what to listen to, what kind of questions to ask that’ll be engaging and that they’ll give good answers to. How to follow up on a ..."}
]}
```

## Setup App
1. `pip install pipenv`
2. In the main directory, `pipenv install`, this handles your virtual environment using the Pipfile much like npm
3. Follow the instructions in `example.env` to set your env variables/db

## Run App
1. `pipenv shell` enters the virtual environment
2. `flask run`, runs app.py with .env variables
- if you uncommented debug mode in the .env, flask run will enter debug mode and automatically reload on changes

*Can also not shell and prefix any command with `pipenv run` i.e `pipenv run flask run``*
