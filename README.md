# N-Zero Research Program

[![Tests](https://github.com/super-morphist-sukezo/nza-arithmetic/actions/workflows/tests.yml/badge.svg)](https://github.com/super-morphist-sukezo/nza-arithmetic/actions)

N-Zero explores a boundary-aware distinction between **local zero** and claims
of **global disappearance**.

Its foundational motivation is epistemic:

> The world currently visible to us is all the evidence we presently have, but
> our present view is not evidence that we have seen all that exists.

N-Zero therefore keeps two commitments together: expand the horizon of possible
resources and relations, while treating currently reachable resources as finite.

The project began as N-Zero Arithmetic, representing values as local labels with
an invariant universe component. Review of that formulation found a valuable
conceptual question but also showed that algebra, physical interpretation, and
ethical claims needed separate standards of evidence.

## Current Status

This repository is experimental.

- The Python package is a historical prototype of the v5 formulation.
- The prototype is not evidence for a physical conservation law.
- The current CI is not yet a release gate for a stable package.
- The revised N-Zero Conservation Model is specified but not yet implemented.

## Revised Paper Suite

The proposed Revision is split into three papers:

1. [N-Zero Conservation Model](docs/papers/01-n-zero-conservation-model.md)
   defines explicit boundaries, balances, transfers, discrepancies, and
   provenance.
2. [No-Zero Universe Interpretation](docs/papers/02-no-zero-universe-interpretation.md)
   treats the universe claim as a speculative interpretation requiring
   domain-specific predictions and tests.
3. [N-Zero Ethics and Governance](docs/papers/03-n-zero-ethics-and-governance.md)
   develops non-erasure and residual-aware governance without deriving ethics
   from arithmetic.

See the [paper suite overview](docs/papers/README.md) for evidence boundaries and
the revision map from v5. A Japanese editorial proposal is available in
[`REVISION_PROPOSAL.ja.md`](docs/papers/REVISION_PROPOSAL.ja.md).

## Historical Prototype

```python
from nza import NZA

a = NZA(5)
b = NZA(3)

print(a - b)             # 2.0_local + infinity_universe
print(NZA(5) - NZA(5))  # 0.0_local + infinity_universe
```

This API demonstrates the earlier local-label representation. Because its
`total()` method returns infinity by definition, it does not independently test
or prove conservation. It should not yet be treated as an implementation of the
revised NZCM specification.

## Development

```bash
git clone https://github.com/super-morphist-sukezo/nza-arithmetic
cd nza-arithmetic
python -m pip install -e '.[dev]'
pytest
```

## Review Principles

- Keep mathematical, physical, and normative claims in separate evidence planes.
- Treat failed tests and competing interpretations as Revision input.
- Do not equate a local measurement of zero with universal nonexistence.
- Keep an **Abundance Horizon** without closing the unknown as empty.
- Keep **Scarcity Discipline** for resources that are currently reachable.
- Do not let a single launch, transport, energy, or communication gateway turn
  possible abundance into a new monopoly.
- Preserve the original v5 paper as lineage rather than rewriting its claims.

## License

MIT
