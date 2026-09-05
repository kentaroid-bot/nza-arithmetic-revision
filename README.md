# N-Zero Arithmetic (NZA)

[![PyPI version](https://badge.fury.io/py/nza-arithmetic.svg)](https://badge.fury.io/py/nza-arithmetic)
[![Tests](https://github.com/kentaroid-bot/nza-arithmetic-revision/actions/workflows/tests.yml/badge.svg)](https://github.com/kentaroid-bot/nza-arithmetic-revision/actions)

Rigorous mathematical framework for the \&quot;No-Zero Universe\&quot; interpretation. Distinguishes *local labels* (including 0_local, negatives) from invariant infinite *universe total* (∞).

## Installation

```bash
pip install nza-arithmetic
```

## Quick Start

```python
from nza import NZA

a = NZA(5)
b = NZA(3)
print(a - b)  # 2.0_local + ∞_universe

zero = NZA(0)
print(a / zero)  # ∞_universe

print(NZA(5) - NZA(5))  # 0.0_local + ∞_universe  (no annihilation!)
```

## Features

- Full arithmetic ops: +, -, *, / (div/0 → ∞_universe)
- Comparisons on local labels
- Rich repr showing local + ∞_universe
- Type hints, tests, PyPI-ready

## Theory

The imported source theses are preserved for comparison:

- [Version 4](docs/source-theses/nza-full-thesis-v4.md)
- [Version 5](docs/source-theses/nza-full-thesis-v5.md)

## Development

```bash
git clone https://github.com/kentaroid-bot/nza-arithmetic-revision
cd nza-arithmetic-revision
pip install -e .[dev]
pytest
```

## Collaboration

This repository is jointly developed by `kentaroid-bot` and `super-morphist-sukezo` using the [Unflatten Protocol](https://github.com/kentaroid-bot/unflatten-protocol).

Hypotheses are developed in separate Worldline branches and reviewed through Innovator, Auditor, Integrator, and Engineer roles. Conflicting hypotheses do not need to be averaged into a compromise; they may remain as explicit, testable alternatives.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the collaboration workflow, Pull Request requirements, source-document policy, and merge rules.

## License

MIT
