# World of Warships Ship Renamer

Does what it says on the tin. (Or will some day, at least.)
A utility that can rename ships in the [World of Warships] game by [Wargaming.net].

## ⚠️ WIP

This is a work in progress. By one person. In his spare time. **Caveat emptor!**

### Code

[![Requirements Status][requirements-badge-img]][requirements-badge-href]
[![Updates][pyup-badge-img]][pyup-badge-href]
[![Conventional commits][conventional-commits-badge-img]][conventional-commits-badge-href]
[![Code style: black][black-badge-img]][black-badge-href]

### CI

#### TODO: CI

![Build status][github-actions-badge-img]
[![Technical debt](https://sonarcloud.io/api/project_badges/measure?project=kthy_uml.cs&metric=sqale_index)](https://sonarcloud.io/dashboard?id=kthy_uml.cs)

## Usage

### TODO: Usage

```bash
$ python3 -m wren --help
Usage: wren [OPTIONS]

  Foo.

Options:
  --config FILE          Path to the configuration file.
  --help                 Show this message and exit.
```

## Development environment setup

### TODO: Terraform

Ubuntu on WSL:

```bash
$ sudo apt install graphviz
$ sudo apt install python3-pip
$ pip3 install --user pipenv
$ . .profile
$ pipenv --version
pipenv, version 2018.11.26
```

## Concept

1. Convert `${wowsPath}/res/texts/en/LC_MESSAGES/global.mo` to `temp/global.po`
   using `msgunfmt` from [PoEdit](https://github.com/vslavik/poedit).
2. Depending on input params, search and replace or prefix:
    * Prefix ship names with radar symbols and, optionally, range.
    * Convert names of Russian ships to cyrillic alphabet.
3. Convert the changed `temp/global.po` using `msgfmt` into `temp/global.mo`.
4. Rename the original `global.mo` to `global.mo.original`.
5. Copy the new `global.mo` to where the original was.

[black-badge-img]: https://img.shields.io/badge/code%20style-black-000000.svg
[black-badge-href]: https://github.com/psf/black
[conventional-commits-badge-img]: https://img.shields.io/badge/conventional%20commits-1.0.0-blue.svg
[conventional-commits-badge-href]: https://www.conventionalcommits.org/en/v1.0.0/
[github-actions-badge-img]: https://github.com/kthy/wows-ship-renamer/workflows/build/badge.svg
[pyup-badge-img]: https://pyup.io/repos/github/kthy/wows-ship-renamer/shield.svg
[pyup-badge-href]: https://pyup.io/repos/github/kthy/wows-ship-renamer/
[requirements-badge-img]: https://requires.io/github/kthy/wows-ship-renamer/requirements.svg?branch=main
[requirements-badge-href]: https://requires.io/github/kthy/wows-ship-renamer/requirements/?branch=main
[Wargaming.net]: https://wargaming.com/
[World of Warships]: https://worldofwarships.eu/
