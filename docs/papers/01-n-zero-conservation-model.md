# N-Zero Conservation Model

## A Boundary-Aware Ledger for Local Zero and Global Conservation

**Abbreviation:** NZCM

**Status:** `proposal`

**Claim type:** formal model

## Abstract

The N-Zero Conservation Model distinguishes a local zero from disappearance at
the boundary of a modeled system. It represents quantities as balances assigned
to explicit nodes, including an environment node when the system is open, and
represents changes as provenance-bearing transfers. Conservation is not encoded
as a constant infinity tag. It is an invariant that can be calculated before
and after each transition and can therefore fail.

NZCM does not deny the mathematical existence or usefulness of zero and
negative numbers. Its narrower claim is that a local value of zero does not,
without a boundary and transition record, establish global annihilation.

## 1. Scope

NZCM is suitable for systems in which a quantity, entitlement, obligation, or
record moves between identifiable accounts. Examples include inventory,
resource allocation, accounting, custody, and protocol state transitions.

NZCM alone does not establish:

- that every physical quantity is conserved;
- that the universe is closed, infinite, or cyclic;
- that an unobserved destination necessarily exists;
- that mathematical zero or signed coordinates are unreal;
- that conservation implies abundance or ethical fairness.

NZCM models every operational state with a finite declared boundary. This does
not assert that reality ends at that boundary. It separates what the model can
currently account for from what may exist outside its observation and access.

## 2. Definitions

### 2.1 Boundary

Let `N` be a finite set of modeled nodes. For an open model, add an environment
node `omega` representing exchange across the selected boundary.

```text
N* = N                         for a declared closed model
N* = N union {omega}           for a declared open model
```

`omega` is not infinity. It is an explicit account for quantities that cross
the modeled boundary. A model that cannot measure the environment may use an
`unknown` account, but must not silently claim conservation.

### 2.2 Quantity domain

For a conserved scalar quantity, let balances belong to an additive abelian
group `A`. Typical examples are integers for indivisible units or rational
numbers for exact divisible units.

Floating point values are implementation approximations and require a declared
tolerance. Domain-specific constraints may require every physical balance to be
nonnegative.

### 2.3 State

A state is a balance function:

```text
x: N* -> A
```

The total at the declared boundary is:

```text
T(x) = sum(x[n] for n in N*)
```

Unlike the v5 `total()` function, `T` is calculated from state and is not fixed
to a constant by definition.

### 2.4 Transfer

A transfer is a record:

```text
tau = (source, destination, quantity, timestamp, reference)
```

For `q` in `A`, transition `tau(i, j, q)` produces state `x'`:

```text
x'[i] = x[i] - q
x'[j] = x[j] + q
x'[k] = x[k]                 for every other node k
```

The reference identifies the observation, contract, or event authorizing the
transition. A transfer without adequate provenance may be mathematically
balanced while remaining institutionally invalid.

### 2.5 Local zero

Node `i` is locally zero in state `x` when:

```text
x[i] = 0
```

This says nothing by itself about `T(x)`, the existence of other nodes, or the
history that produced the state.

This distinction is the formal counterpart of the N-Zero Local Zero Axiom:

> `x[i] = 0` is a scoped state, not a representation of absolute nothingness.

Naming source, destination, quantity, and evidence is required to accept a
specific transfer into the operational ledger. Failure to identify a destination
does not turn local zero into proof of annihilation; it leaves the wider account
unresolved.

### 2.6 Provenance ledger

Let `L` be an append-only sequence of proposed, accepted, reversed, or held
transfers. The pair `(x, L)` distinguishes two states with the same balances but
different histories.

NZCM therefore treats balance equality and historical equivalence as separate
relations.

## 3. Core Invariants

### Invariant 1: Boundary declaration

Every conservation claim names the nodes, environment account, quantity, and
time interval included in the claim.

### Invariant 2: Balanced transition

For every accepted internal transfer:

```text
T(x') = T(x)
```

### Invariant 3: Provenance preservation

Every accepted state change has a corresponding ledger entry. Reversal appends
a compensating entry; it does not erase the original record.

### Invariant 4: Observable discrepancy

For any transition, define:

```text
D(x, x') = T(x') - T(x)
```

If `D != 0` and no boundary exchange explains it, the transition enters Hold.
The model reports a discrepancy rather than manufacturing an infinite residual.

### Invariant 5: Scope-specific conservation

Conservation of one declared quantity does not imply conservation of identity,
utility, rights, energy, information, or every other quantity.

### Invariant 6: Revisable boundary

The current node set is an operational scope, not a claim to exhaust reality.
Newly observed nodes and reservoirs may extend the boundary through a recorded
Revision. Before evidence is available, the model records the outside as unknown
rather than empty, infinite, or usable.

## 4. Elementary Results

### Theorem 1: Internal transfer conservation

For any state `x` and internal transfer `tau(i, j, q)`, `T(x') = T(x)`.

**Proof.** The transition subtracts `q` from `i`, adds `q` to `j`, and leaves
all other balances unchanged. The two changes cancel in the finite sum. QED.

### Theorem 2: Local zero does not imply global zero

There exist states with `x[i] = 0` and `T(x) != 0`.

**Proof.** Choose a second node `j` with `x[j] = q != 0` and all remaining
balances zero. Then `x[i] = 0` while `T(x) = q`. QED.

### Theorem 3: Equal balances do not imply equal provenance

There exist ledgers `L1 != L2` that produce the same state `x`.

**Proof.** An empty ledger and a ledger containing a transfer followed by its
compensating reversal can produce equal final balances. QED.

These results are elementary. The contribution claimed by NZCM is not a new
number system but a disciplined modeling pattern connecting boundary, state,
transition, and provenance.

## 5. Obligations and Negative Coordinates

Negative numbers remain valid mathematical coordinates. When the domain is
obligation rather than physical inventory, a directed claim may be clearer:

```text
debt(i -> j, q), where q >= 0
```

A node's net position may be calculated from incoming and outgoing claims. This
avoids confusing a negative balance with negative existence while preserving
the information represented by signed arithmetic.

## 6. Open Systems and Loss

If a quantity enters or leaves the selected system, the transition includes
`omega` as source or destination. If the destination is unknown, the ledger may
record:

```text
status = HOLD
reason = UNRESOLVED_DESTINATION
quantity = q
```

This is an epistemic state, not evidence that the quantity still exists. A Hold
preserves the unresolved question without deciding it prematurely.

Within the N-Zero research program, this Hold expresses a deliberate asymmetry:
unknown continuation is not treated as a verified transfer, but neither is lack
of a verified destination treated as proof of absolute nothingness.

### Boundary expansion

Discovery or construction of a new reachable reservoir extends the modeled node
set. A boundary expansion records:

```text
previous boundary
new node or reservoir
evidence of reachability
access path and controller
effective time
```

Potential resources outside the current boundary do not enter the operational
balance until they are observable and reachable. This keeps exploration open
without spending hypothetical abundance in the present ledger.

## 7. Reference Implementation Requirements

A conforming implementation should:

1. use an explicit quantity domain;
2. reject undeclared division by zero;
3. calculate totals from balances;
4. make source and destination mandatory for transfers;
5. distinguish accepted, rejected, held, and reversed entries;
6. expose boundary discrepancies;
7. preserve original provenance after reversal;
8. avoid representing unknown values as infinity.

Property-based tests should cover:

- conservation across arbitrary valid transfers;
- failure on unbalanced mutations;
- closure of operations in the declared domain;
- replay equivalence between ledger and materialized state;
- reversal without history deletion;
- floating point tolerance, if floating point is permitted.

## 8. Limitations

NZCM is an accounting and transition model. Conservation is conditional on the
chosen boundary, quantity, measurements, and transition rules. A balanced ledger
can still contain fraud, coercion, mistaken observations, or unjust ownership.
Those concerns require independent governance and evidence models.

An expanded resource boundary can also increase concentration when one node
controls the only access path. NZCM can expose that path and its controller but
does not by itself prevent monopoly.

## 9. Central Claim

The defensible N-Zero claim is:

> Local zero is a state of a scoped account. Global disappearance is a separate
> claim requiring an explicit boundary, a transition history, and evidence.
