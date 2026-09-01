# N-Zero Paper Suite

**Status:** `proposal`

**Version:** `0.1-draft`

**Last updated:** 2026-09-01

## Purpose

This paper suite revises the original N-Zero Arithmetic thesis without erasing
its central intuition:

> A value disappearing from a local observation does not by itself establish
> disappearance from the wider system.

The original thesis combined an algebra, a physical interpretation, and ethical
claims in one document. These drafts separate those layers so that each can be
reviewed using an appropriate standard of evidence.

The research motivation is not that unseen resources may be counted as if they
were already available. It is that the present observational boundary should not
be promoted into a final boundary of reality without evidence.

N-Zero adopts a strong interpretive starting point:

> `5 - 5 = 0_local + 5_universe` means zero in a selected local account while
> the same five remains at universe scope; it is not absolute nothingness.

The formal model does not claim that the arithmetic expression itself identifies
where the five went. Provenance requirements establish a specific transfer;
they do not authorize an inference from local zero to ontological annihilation.

```text
Abundance Horizon: do not declare the unknown empty or permanently closed.
Scarcity Discipline: allocate currently reachable resources as finite.
```

Multiplanetary expansion is one possible boundary-expansion strategy. It does
not produce decentralization unless access to transport, energy, communication,
and settlement can avoid capture by a small set of gateways.

## Documents

The editorial change is summarized in Japanese in
[`REVISION_PROPOSAL.ja.md`](REVISION_PROPOSAL.ja.md).

1. [N-Zero Conservation Model](01-n-zero-conservation-model.md)
   defines a finite, testable state-transition and provenance model.
2. [No-Zero Universe Interpretation](02-no-zero-universe-interpretation.md)
   presents the ontological and physical intuition as a speculative research
   interpretation with explicit falsifiability requirements.
3. [N-Zero Ethics and Governance](03-n-zero-ethics-and-governance.md)
   develops the ethical implications as design proposals rather than
   mathematical consequences.

## Positioning

`N-Zero` is the umbrella name for the research program. The three documents
make different kinds of claims:

| Layer | Name | Evidence expected | Current status |
|---|---|---|---|
| Formal | N-Zero Conservation Model (NZCM) | definitions, proofs, executable tests | draft specification |
| Interpretive | No-Zero Universe Interpretation (NZUI) | domain models, observations, predictions | speculative hypothesis |
| Normative | N-Zero Ethics and Governance (NZEG) | argument, case analysis, pilot evidence | design proposal |

Passing a test in one layer does not validate another layer. In particular:

- software tests do not establish a physical law;
- a conservation invariant does not prove that the universe is infinite;
- an ontological interpretation does not entail a political or ethical rule;
- an ethical preference does not prove a mathematical theorem.
- a possibly infinite universe does not make resources presently accessible to
  any node infinite.

## Revision From NZA v5

The N-Zero lineage contains two related formulations. Its motivating finite
notation, `5 - 5 = 0_local + 5_universe`, expressed the Local Zero Axiom while
retaining the conserved quantity. The v5 formalization then represented values
as `(local_label, infinity_universe)` and defined the total as infinity. That
generalization preserved the intuition but made conservation true by definition.
It also mixed integer labels, floating point implementation, division by zero,
physical analogies, and ethical claims.

This suite changes the formal core as follows:

| v5 formulation | Proposed revision |
|---|---|
| `0_local + 5_universe` preserves five across scopes | Keep this finite insight and express each scope as an explicit account |
| Every value carries a constant infinity component | A state contains explicit local accounts and a declared boundary |
| `total()` always returns infinity | The total is calculated from the current state |
| Local subtraction reaches absolute nothingness | The Local Zero Axiom treats zero as scoped, not ontological annihilation |
| A specific relocation is known without provenance | An accepted transfer names source, destination, quantity, and evidence |
| Division by zero returns infinity | Division by zero remains undefined unless a domain-specific extension is declared |
| Negative values do not exist | Negative coordinates are valid; obligations may instead be represented as directed edges |
| Tests validate conservation | Property tests attempt to falsify the invariant across transitions |
| Physics and ethics follow from the algebra | Physics and ethics are reviewed in separate evidence planes |

## Promotion Gate

Before any document is described as an adopted theory:

1. notation and domains must be internally consistent;
2. proofs must be independently reviewed;
3. the reference implementation and CI must pass;
4. physical claims must state a domain, observables, and discriminating tests;
5. ethical claims must address scarcity, power asymmetry, privacy, and exit;
6. competing interpretations and failed tests must remain visible.

The original v5 paper remains part of the lineage. These drafts are a Revision,
not a retroactive claim that the earlier document already contained this model.
