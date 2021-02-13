# PE

My solutions for Project Euler.

## Set up

Python
```
python3 -m venv venv
. venv/bin/activate
# `python -V` => Python 3.8.5
pip install -r requirements.txt
```

TypeScript
```
# `nvm version` => v15.8.0
npm install
```

## Run code

- `python3 001.py`
- `npx ts-node 002.ts`

## Run tests

- `pytest`
- `npm test`

## Development

Local github workflow testing:

Install [act], and run

```
act -P ubuntu-latest=catthehacker/ubuntu:act-latest
```

[act]: https://github.com/nektos/act
