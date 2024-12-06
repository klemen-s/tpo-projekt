
## Run Locally

#### Prerequsities
* Poetry package manager
* Docker
* VS Code
* Python ^3.12

Clone the project

```bash
  git clone https://github.com/klemen-s/tpo-projekt.git
```
### Database
#### The database must be running before the backend
In the root directory of the project run the command:
```bash
  docker compose -f ok.yml up
```

### Backend
Go to the project directory

```bash
  cd backend
```

```bash
  poetry install
  poetry shell
```

  When "poetry shell" command has ran, it will print out a venv path (.../bin/activate), copy that.
  In VS Code enter CTRL + P and type in:
    "Select Interpreter" and choose  "Enter interpreter path..."
  Paste in the path you copied.
  
  For the new interpreter to replace the old one, you need to reselect the new Python interpreter called "3.12 (backend-...)", at the bottom right of VS Code (see "razvojni kanal" in Discord for the picture) .


Start the server

```bash
  fastapi dev main.py
```

Start developing...

