# Auditor Report: Universe Term Semantics

## 1. Audit Target & Locks

### Core hypothesis

NZA's falsifiable conservation content requires a tracked universe state rather
than a constant infinity component; v5 and the current implementation cannot
detect a conservation discrepancy because infinity absorbs every finite change.

### Preserved core premises

- `5 - 5 = 0_local + 5_universe` preserves a distinction between a local zero
  and disappearance from the declared wider scope.
- Conservation must be able to fail an observation or test.
- A universe term that records movement is not semantically equivalent to a
  constant ontological marker.
- A failed scalar formulation must not force the inquiry back to ordinary
  arithmetic plus an ornamental suffix.

### Causal mechanism under audit

The submitted hypothesis proposed accumulating a numeric universe term during
operations. The strongest rational form of that mechanism is not
`_universe = sum(a + b)`, but a scoped transition system:

```text
state x: declared nodes -> quantity
transfer tau(i, j, q): x[i] -= q; x[j] += q
total T(x): sum of declared balances
history L: append-only transfer events with provenance
```

The notation `0_local + 5_universe` is then read as a projection of the post
state across two scopes, not as ordinary addition of two independent stocks.

### Distinct dimensions locked

- quantity traceability;
- conservation falsifiability;
- state mechanism versus ontological marker;
- compositional consistency;
- balance equality versus historical equivalence.

## 2. Counter-Factual Steelman Setup

Assume the ledger formulation has ideal resources and observations:

- every modeled system declares its boundary and quantity domain;
- each accepted movement has a known source, destination, quantity, time, and
  evidence reference;
- balances are exact and every internal transition is atomically recorded;
- an environment node accounts for observed boundary exchange without being
  equated to mathematical infinity;
- unknown destinations remain `HOLD` rather than being manufactured as an
  infinite balancing term;
- materialized balances and append-only history can be replayed and compared;
- the infinity claim, if retained, is evaluated in a separate interpretive
  worldline with its own success and failure conditions.

In this strongest world, the ledger is a falsifiable conservation mechanism:
`D(x,x') = T(x') - T(x)` can be nonzero.

## 3. Dual-Stress Falsification Map

### Route A: Logical and systemic collapse

#### A1. The v4 text does not define one operation

The imported v4 source contains mutually incompatible rules:

| Source statement | Universe result for `5 - 5` | Universe result for `3 - 5` |
|---|---:|---:|
| introductory examples | `5` | `8` |
| Axiom 2: `(a + b)_universe` | `10` | `8` |
| piecewise formula | `5` | `5` |

The piecewise formula also returns `0_local` for every `a >= b`, so it loses a
positive remainder such as `5 - 3 = 2`. Consequently there is no unique
"v4-derived accumulator" to implement without making an additional decision.

**Falsification status:** complete against the claim that v4 already specifies
a coherent binary ledger operator. It does not falsify the broader local-zero
and traceable-transfer inquiry.

#### A2. `sum(a + b)` is not compositional

Suppose each subtraction appends `a + b` to a scalar accumulator while the
local label becomes `a - b`. Then:

```text
(a - b) - c:
  universe increment = (a + b) + ((a - b) + c) = 2a + c

a - (b + c):
  universe increment = a + (b + c) = a + b + c
```

The increments differ by `a - b`, even though the ordinary local result is the
same. The accumulator also contains no source, destination, or evidence, so a
balanced number cannot distinguish a real transfer from a fabricated one.

**Falsification status:** complete against `_universe = sum(a + b)` as a closed
arithmetic component.

#### A3. Order dependence has two meanings

If universe data is asserted to be part of an algebraic value determined only
by the final local value, history dependence is a contradiction. If it is an
event ledger, different operation orders are intentionally different histories
even when balances coincide. The submitted hypothesis did not separate these
two equality relations.

**Classification:** revisable defect. Separate balance/state equality from
history/provenance equality.

#### A4. A third semantics already exists

The unmerged branch `origin/codex/n-zero-paper-suite` contains commit
`3f74ee5` and `docs/papers/01-n-zero-conservation-model.md`. It models explicit
nodes, an environment account, finite balances, transfers, discrepancies, and
append-only provenance. It also separates this formal model from
`docs/papers/02-no-zero-universe-interpretation.md`, where infinity remains a
motivating hypothesis rather than a balancing constant.

This satisfies the submitted third falsifier: the quantity-ledger versus
infinity-constant binary is incomplete. More precisely, the useful split is:

1. local labels and ordinary arithmetic;
2. finite boundary-aware conservation state plus event provenance;
3. an independently evaluated infinity interpretation.

**Classification:** revisable defect, and direct evidence for the repair.

#### A5. Provenance cannot be inferred from arithmetic

An expression such as `5 - 5` does not establish that five objects moved, where
they moved, or whether the modeled quantity was conserved. A mathematically
balanced ledger can contain false, coerced, or duplicated events.

**Falsification condition:** if the model treats arithmetic balance as evidence
of a real transfer, the causal claim fails. The repair must require observation
or provenance for operational acceptance and allow unresolved destinations to
remain unknown.

#### A6. Current verification is not executable

`python3 -m pytest -q` fails during collection with an `IndentationError` at
`tests/test_nza.py:2`. After syntax repair, tests for floor division, power, and
other scalar operations must still be checked against methods present in
`src/nza/core.py`. This defect does not decide the semantics, but current test
claims cannot support either formulation.

### Route B: Cognitive and physical friction

#### B1. Cognitive bandwidth

Requiring boundary, source, destination, and provenance for every use of
subtraction would turn ordinary arithmetic into an unusable accounting ritual.
The mechanism is viable only where a conservation or transfer claim is being
made. Ordinary arithmetic must remain available as a projection or separate
layer.

#### B2. Physical latency

In real systems, the destination or measurement may arrive later than the local
event. Blocking all local action until global knowledge is available loses the
race to physical reality. The strongest repair records a pending or unresolved
event and permits domain-specific provisional action without pretending the
global balance is known.

For a purely formal model, physical latency is `not_applicable`; it becomes
material only when the model is used as evidence about an external system.

#### B3. Sterile-logic pressure

Calling an environment account "the universe" can make a chosen modeling
boundary sound metaphysically complete. Conversely, removing infinity from the
ledger can feel like abandoning the generative conviction behind NZA. Combining
the two to reduce discomfort would recreate the unfalsifiable constant. The
repair is parallel semantics with explicit authority boundaries, not a blended
term.

No unarticulated bodily objection strong enough for a Noise Veto was observed.
The cognitive burden and metaphysical overclaim are already expressible as
specific defects.

## 4. Evidence & Noise Assessment

### Supporting

- v4 preserves concrete finite quantities in its motivating examples.
- v5 defines a symbolic infinite constant and proves conservation by infinity
  absorption.
- `src/nza/core.py` returns `math.inf` independently of state.
- the unmerged paper-suite branch demonstrates a concrete boundary-aware repair
  with computed totals and explicit discrepancy.

### Contradicting

- v4's axioms, examples, and piecewise formula do not agree, so v4 is not itself
  an implementable formal specification.
- the submitted scalar `sum(a + b)` mechanism fails compositional equivalence.
- the existing third semantics makes the proposed binary framing incomplete.

### Unknown

- whether the Human Steward adopts the paper-suite branch's three-plane split;
- whether a domain-specific NZA ledger produces a novel useful result beyond
  established accounting/event-sourcing patterns;
- which independent success signals should govern the infinity interpretation;
- whether the unmerged paper-suite branch should be rebased, revised, or split
  into multiple PRs.

### Noise

No Noise Veto is triggered. There is a clear, articulable risk that the word
"universe" confers false completeness on an operational boundary and a separate
risk that formal repair erases the original infinite-horizon motive. Both are
preserved as distinct concerns.

## 5. Findings & Classification

| ID | Finding | Classification |
|---|---|---|
| F1 | v4 contains incompatible universe update rules | Revisable Defect for the research program; fatal to literal implementation of v4 as one operator |
| F2 | `sum(a + b)` is grouping-dependent and loses provenance | Fatal Contradiction for that scalar mechanism |
| F3 | balance equality and history equality were conflated | Revisable Defect |
| F4 | a boundary-aware third semantics already exists on an unmerged branch | Revisable Defect in the binary framing |
| F5 | infinity absorption cannot detect finite discrepancies | Confirmed support for the core criticism |
| F6 | arithmetic alone cannot prove an external transfer | Revisable Defect requiring evidence and Hold states |
| F7 | the current test suite fails during collection | Revisable implementation defect; epistemically independent |
| F8 | applying provenance-ledger semantics to all arithmetic overloads humans | Revisable scope defect |

## 6. Repair Boundary

The hypothesis may be revised only within this boundary:

1. Replace the scalar universe accumulator with explicit finite state over named
   nodes or scopes.
2. Represent movement as provenance-bearing events; do not infer a transfer
   merely from subtraction syntax.
3. Compute totals and expose discrepancies so conservation can fail.
4. Separate materialized balance equality from ledger-history equivalence.
5. Scope the ledger to domains making conservation/transfer claims; do not
   replace ordinary arithmetic globally.
6. Preserve infinity as a separate interpretive worldline, not an automatic
   residual used to balance operational state.
7. Preserve v4 and v5 as historical sources rather than rewriting either.

### Four-question revision gate

1. **Is the core preserved?** Yes. Local zero remains distinct from global
   disappearance, and the wider state becomes more—not less—traceable.
2. **Is this an ad hoc patch?** No. State/event separation is required by the
   distinction between current balance and history and applies generally.
3. **Is human friction addressed?** Yes, if the ledger is limited to explicit
   conservation claims and supports unresolved/held events.
4. **Does a distinct observable consequence remain?** Yes. An unbalanced
   transition produces a nonzero discrepancy instead of being absorbed by
   infinity.

## 7. Final Verdict

**`revise` — `epistemic_recommendation`.**

Advance the insight that constant infinity is not a conservation verifier.
Reject the literal v4 formulas and `sum(a + b)` scalar accumulator as the
mechanism. Reframe the testable core as a boundary-aware state and event ledger,
while preserving infinity as a non-merged interpretive worldline.

This verdict does not authorize implementation or merge. The Integrator must
decide whether to connect the existing `codex/n-zero-paper-suite` work, repair
the test baseline first, or request a narrower new worldline.

