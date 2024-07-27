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
* # On Windows:
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

6. Running the Application
```
uvicorn main:app --reload


```

install miktex https://miktex.org/
install pearl https://strawberryperl.com/