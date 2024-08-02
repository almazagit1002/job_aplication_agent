# Job Aplication Agent

## Prerequisites
* Python 3.7+
* MongoDB instance (local or cloud-based)

## Instalation
1. Clone the repository:
```
git clone https://github.com/almazagit1002/job_aplication_agent.git
```

2. Create a virtual environment:
```
python -m venv venv
```

3. Activate virtual environment:
* On macOS and Linux:
```
source venv/bin/activate  
```
* On Windows:
 ```
venv\Scripts\activate
```

4. Install `pip` (if not already installed)
 * Check if pip is installed:
  ```
  pip --version
  ```
If `pip` is not installed, follow these steps to install it:
* Using `curl`:
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
* Using `wget`:
```
wget https://bootstrap.pypa.io/get-pip.py
```

Install:
```
python get-pip.py
```

5. Install Project Dependencies:
```
pip install -r requirements.txt

```

6. Running the `user_api`

```
cd user_api
```

* Option 1:
    ```
    uvicorn main:app --reload --host localhost --port 8000
    ```
* Option 2 (Docker Image):

    ```
    docker build -t user_api .  
    ```

    ```
    docker run -p 8000:8000 user_api  
    ```

* Access the interactive API documentation:
Open your browser and go to
```
 http://localhost:8000/api/v1/users/docs 
```
or
```
http://localhost:8000/api/v1/users/redoc
```

* Local Test
    * Use `...\job_aplication_agent\user_api\research\01_db_interaction.ipynb` count, delete or print documents

    * Use `...\job_aplication_agent\user_api\research\02_test_api.ipynb` to see insert user data




## Project Structure

```
user_api/
├── main.py
├──db
|  ├── models/
│       ├── base.py
│       ├── user.py
│       ├── contact_info.py
│       ├── education.py
│       ├── experience.py
│       ├── skills.py
│       └── projects.py
|  ├── db_set_up.py
|
├── api/
│   ├── utils
│       └── users.py
│   └── users.py

```


## Ignore this 

install miktex https://miktex.org/
install pearl https://strawberryperl.com/