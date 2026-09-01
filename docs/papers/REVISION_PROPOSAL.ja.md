# Revision Proposal: N-Zero研究プログラムの再構成

**Status:** `proposal`

**Concept origin:** Kentaro / Human Steward

**Drafted by:** Codex / Scoped Execution Node

**Target:** N-Zero Arithmetic v5以後の研究・文書構成

**Last updated:** 2026-09-01

## 1. 提案

N-Zero Arithmeticを、完成済みの万能的算術体系として提示するのではなく、
次の三つのEvidence Planeを持つ研究プログラムへ再構成する。

1. **N-Zero Conservation Model (NZCM)**
   境界、局所状態、移動、残差、Provenanceを扱う形式モデル。
2. **No-Zero Universe Interpretation (NZUI)**
   局所的消失と存在論的無を区別する、反証条件付きの解釈仮説。
3. **N-Zero Ethics and Governance (NZEG)**
   Monku、被害、義務、履歴を局所的な非表示によって解決済みにしないための
   倫理・Governance提案。

三文書の概要は[`README.md`](README.md)に記載する。

## 2. 保持する核心

旧v5から次の問いを保持する。

> 局所的な観測から値が消えたとき、それだけで全体から消滅したと判断して
> よいのか。

この問いは、数学的ゼロの否定としてではなく、観測境界、移動先、履歴、残余を
明示する要求として再定義する。

## 3. 修正する主張

| 旧表現 | Revision後の扱い |
|---|---|
| 全ての値に`infinity_universe`を付ける | NodeとEnvironmentの有限な明示状態を使う |
| `total()`が常に∞なので保存される | 状態遷移前後の総量を計算し、不一致を検出する |
| ゼロと負数は存在しない | 数学的ゼロと負数を認め、存在論的意味と分離する |
| 5-5は宇宙の別地点への移動である | 移動を主張するならsource、destination、quantity、evidenceを要求する |
| 物理学へ適用できる | 現時点では類比。個別領域で予測と反証条件が必要 |
| 無限総量は豊穣倫理を導く | 倫理は独立に論証し、局所的希少性を否定しない |
| Pythonテストが理論を検証する | テストは実装と形式Invariantだけを検査する |

## 4. 新しい形式核

NZCMでは、状態を次のように表す。

```text
x: Nodes union {environment} -> Quantity
T(x) = sum of all declared balances
```

移動`tau(i, j, q)`は、`i`から`q`を減らし、`j`へ同量を加える。

```text
x'[i] = x[i] - q
x'[j] = x[j] + q
T(x') = T(x)
```

移動先が不明な場合は∞へ代入せず、`UNRESOLVED_DESTINATION`としてHoldする。
これにより、保存は公理的な表示ではなく、失敗を検出できるInvariantになる。

## 5. Apertureとの関係

N-ZeroはApertureの数学的証明または採用済みInvariantではない。一方、次の
認識論的構造は比較できる。

```text
local zero             != global disappearance
Issue close            != every effect resolved
connection stop        != dependency erased
Revert                 != history deletion
rejected Revision      != impossible future Fork
```

この接続はLineage上の解釈として保持し、Protocol要件には自動昇格させない。

## 6. 非目標

- 宇宙が有限か無限かを本Revisionで決定しない。
- 標準数学からゼロまたは負数を排除しない。
- 熱力学、量子論、一般相対論をN-Zeroで置換しない。
- 数学から直接、政治制度またはAI倫理を導出しない。
- 旧v5を削除または遡及的に書き換えない。

## 7. Reviewで判断すること

このRevisionのReviewは、少なくとも次を分けて判断する。

1. 三つのEvidence Planeへの分離を採用するか。
2. NZCMを次期実装仕様の候補として扱うか。
3. NZUIを検証前のInterpretationとして公開保持するか。
4. NZEGをApertureとは独立した倫理Draftとして扱うか。
5. 旧v5をHistorical Prototypeとして保存するか。

Approveは物理仮説の正しさ、数学的新規性、Apertureへの正式採用を意味しない。
意味するのは、これらを混同せず別々に検証できる構造へ移行することへの合意である。
