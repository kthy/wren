# World of Warships Renamer

Does what it says on the tin. (Or will some day, at least.)
A utility that can rename ships in the [World of Warships] game by [Wargaming.net]. Hence, **W**orld of Warships **Ren**amer &rarr; **wren**.

## ⚠️ WIP

This is a work in progress. By one person. In his spare time. **Caveat emptor!**

### Code

[![Requirements Status][requirements-badge-img]][requirements-badge-href]
[![Updates][pyup-badge-img]][pyup-badge-href]
[![Conventional commits][conventional-commits-badge-img]][conventional-commits-badge-href]
[![Code style: black][black-badge-img]][black-badge-href]

### CI

![Build status][github-actions-badge-img]
[![Code coverage][codecov-badge-img]][codecov-badge-href]
[![Technical debt][sonarcloud-badge-img]][sonarcloud-badge-href]

## Usage

```
$ wren --help
Usage: wren [OPTIONS] [CHANGESETS]...

  wren = Warships RENamer. A utility that can rename ships in the World of
  Warships game by Wargaming.net.

  Applies all changes found in the list of CHANGESETS, as defined in the
  provided config file.

  Example:

      $ wren radar cyrillic

Options:
  -c, --config PATH  Path to config file.  [default: ./wren.cfg]
  -u, --undo         If provided, the original names will be reinstated.
  --help             Show this message and exit.```
```

## Development environment setup

* Assumes you have `pipenv` installed and in your path.
* Assumes Windows 10.

```bash
pipenv install --dev
```

[black-badge-href]: https://github.com/psf/black
[black-badge-img]: https://img.shields.io/badge/code%20style-black-000000.svg
[codecov-badge-href]: https://codecov.io/gh/kthy/wren
[codecov-badge-img]: https://codecov.io/gh/kthy/wren/branch/main/graph/badge.svg
[conventional-commits-badge-href]: https://www.conventionalcommits.org/en/v1.0.0/
[conventional-commits-badge-img]: https://img.shields.io/badge/conventional%20commits-1.0.0-blue.svg
[github-actions-badge-img]: https://github.com/kthy/wren/workflows/build/badge.svg
[pyup-badge-href]: https://pyup.io/repos/github/kthy/wren/
[pyup-badge-img]: https://pyup.io/repos/github/kthy/wren/shield.svg
[requirements-badge-href]: https://requires.io/github/kthy/wren/requirements/?branch=main
[requirements-badge-img]: https://requires.io/github/kthy/wren/requirements.svg?branch=main
[sonarcloud-badge-href]: https://sonarcloud.io/dashboard?id=kthy_wren
[sonarcloud-badge-img]: https://sonarcloud.io/api/project_badges/measure?project=kthy_wren&metric=sqale_index
[Wargaming.net]: https://wargaming.com/
[World of Warships]: https://worldofwarships.eu/
