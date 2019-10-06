# ifp-assessment-tester

Assuming you are on a Linux System, you probably have Python 3 installed (And PIP as well)

```
pip3 install -r requirements.txt
```

Setup settings.json

```
{
	"username": "jane",
	"password": "123456789",
	"server_url": "http://localhost:8000",
	"interval": 1
}


```
Above keys are required! Kindly point to your relavent server. Username/Password doesn't matter as long as they are valid ones. Required to obtain token.

```
python3 autopost.py
```
