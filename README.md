# Game project

Start the game following these instructions on your terminal:

```sh
cd game
python3 main.py
```

# App project

```sh
git clone
cd app
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
# For a world population pie chart use:
python3 graph_world_pop.py
# For a country population bar chart use:
python3 graph_population.py
```

# Web server project

```sh
git clone
cd web-server
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
uvicorn main:app --reload
```