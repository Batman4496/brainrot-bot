# Brainrot Bot

I L rizz party rizz just biggest bird pibby glitch rizz king rizzard of oz dj khaled whopper whopper whopper biggest bird zoomer omega male

[Watch a demo](https://youtube.com/shorts/-82lzUF4_3k?feature=share)
---

## Features
- Categorize memes into videos, pictures, and songs.
- Store your collection in a structured directory.
- Simple configuration for seamless operation.
- ChatGPT'd the shit out of this README

---

## Setup

### Prerequisites
- Python 3.7+
- `pip` (Python package manager)

### Steps
1. **Clone the repository**:
2. **Create a virtual environment**: `python -m venv venv`
3. Copy `.example.env` to `.env` and update the `TOKEN`
3. **Activate the virtual environment**:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source venv/bin/activate
  ```

4. **Install dependencies**: `pip install -r requirements.txt`

---

## Directory Setup

1. **Organize your memes**:
  Store your memes inside the `storage/`. 
2. **Creating directory**: Create `temp` directory inside `storage/`
3. **Update configuration**:
Modify the path in `constants.py` to point to your `storage/` directory. Example:
```python
TEMP_PATH = "./storage/temp"
MEME_FOLDER = "./storage/memes"
```
NOTE: Do not put tailing slash. 
- `./storage/memes/` ❌ 
- `./storage/memes` ✔️ 

## Usage

`python main.py`

Thanks.