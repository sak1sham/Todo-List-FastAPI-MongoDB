# To Do List API

This is a Python API for creating the personal To Do List.

## Installation

Either download and decompress the zip file, or use git to clone the repository.

```bash
git clone https://github.com/sak1sham/Todo-List-FastAPI-MongoDB.git
```

## Usage
Once you are inside the root folder,
```bash
pip install -r requirements.txt
```
This will install all require python wrappers for the repository. If need be, you can install more wrappers.

Now, create a ```.env``` file inside the ```config``` folder to store the password for MongoDB. Your ```.env``` file shall look like
```python
MONGOPWD=<password>
```
MongoDB Cloud: Create a ```todos_app``` collection inside the database ```todo_app```

For running the API (```main.py```), 

```bash
uvicorn main:app --reload
```

For testing purposes (```test_main.py```),
```bash
pytest
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)