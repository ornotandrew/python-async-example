# Python Async Example

## Setup

### Client

Make sure your python is `>= 3.8.3`.

```shell
pip install -r requirements.txt
```

### Server

```shell
cd server
npm install
```

## Usage

First, start up the server.

```shell
cd server
npm start
```

Then, test out the two methods for running async code.

```shell
time python thread_pool.py
time python async.py
```
