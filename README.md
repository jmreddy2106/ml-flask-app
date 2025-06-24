# Build, Test, and Secure a Machine Learning API with DevOps Tools

1. mkdir ml-flask-app

2. create empty dirs and files

		ml-flask-app/
		├── .github/
		│   └── workflows/
		│       └── ci.yml
		├── app.py
		├── model.py
		├── requirements.txt
		├── tests/
		│   └── test_app.py
		│   └── test_model.py
		├── README.md
		|-- .gitignore

## To Create model file or pickle file, run the below command form your project directory.
```
python -c "from ml_model import load_model; load_model()"
```

