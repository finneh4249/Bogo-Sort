# Bogo-Sort

## Requirements

- [Python 3.8+](https://www.python.org/downloads/)
- [PIP](https://pypi.org/project/pip/)
- [pyfiglet](https://pypi.org/project/pyfiglet/)
- [colorama](https://pypi.org/project/colorama/)

## Install

### Windows

Run `./bogo.bat` to start the program

### Linux & MacOS

Run `./bogo.sh` to start the program

## Usage

### Windows

- `./bogo.bat -h` or `./bogo.bat --help` for help
- `./bogo.bat <n>` where `n` is the number of elements in the randomly generated list

### Linux & MacOS

- `./bogo.sh -h` or `./bogo.sh --help` for help
- `./bogo.sh <n>` where `n` is the number of elements in the randomly generated list

## How Bogosort Works

Bogosort repeatedly shuffles the list until it happens to be sorted. Its expected
runtime grows factorially with the number of elements, so larger inputs can be
very slow.

### Example (Windows)

```
./bogo.bat 3
```

This sorts a randomly generated list of 3 elements.

### Example (Linux & MacOS)

```
./bogo.sh 3
```

This sorts a randomly generated list of 3 elements.

> **Warning:** No, that's not a typo. Bogosort's expected runtime grows
> factorially (roughly `n!`), which means even modestly larger inputs can take
> an extremely long time. Stick to small values of `n`.
