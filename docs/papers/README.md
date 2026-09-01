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

## Revision From NZA v5

The v5 paper represented every value as `(local_label, infinity_universe)` and
defined the total as infinity. That construction preserved the intuition but
made conservation true by definition. It also mixed integer labels, floating
point implementation, division by zero, physical analogies, and ethical claims.

This suite changes the formal core as follows:

| v5 formulation | Proposed revision |
|---|---|
| Every value carries a constant infinity component | A state contains explicit local accounts and a declared boundary |
| `total()` always returns infinity | The total is calculated from the current state |
| Local subtraction implies relocation | A transfer names source, destination, quantity, and provenance |
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
