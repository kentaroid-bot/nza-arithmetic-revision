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

N-Zeroは次を**Local Zero Axiom（局所ゼロ公理）**として置く。

> `5 - 5 = 0`は、選択された局所Accountがゼロになったことを示す。
> それは絶対的な無を示さない。

物理的解釈では、5はその局所関係から離れ、別の状態、場所、変換関係へ参加する。
現在の観測者がその経路を特定できない場合も、局所ゼロを絶対的消滅の証明には
しない。

`source`、`destination`、`quantity`、`evidence`は、具体的な移動経路を確定して
Operational Ledgerへ採用するために要求する。Local Zero Axiomを保持するための
前提条件ではない。移動先を確認できない場合は、絶対的な無ではなく
`UNRESOLVED_DESTINATION`としてHoldする。

その背景には、次の人間側の認識がある。

> 今見えている世界が私たちの全てである。しかし、現在の私たちがすべてを
> 見ているわけではない。

ここから二つの原則を同時に置く。

- **Abundance Horizon:** 現在の観測・到達境界を、存在全体の最終境界と
  決めつけない。境界拡張、変換、循環、別経路を探索し続ける。
- **Scarcity Discipline:** 現在到達できる資源は有限として扱い、未確認の
  未来資源を現在の配分へ先取りしない。

多惑星化はAbundance Horizonを物理的に実行する一候補である。ただし、宇宙船、
航路、Energy、通信、居住権を単一主体が握れば、宇宙規模のGateway Captureに
なり得る。

## 3. 修正する主張

| 旧表現 | Revision後の扱い |
|---|---|
| 全ての値に`infinity_universe`を付ける | NodeとEnvironmentの有限な明示状態を使う |
| `total()`が常に∞なので保存される | 状態遷移前後の総量を計算し、不一致を検出する |
| ゼロと負数は存在しない | 数学的ゼロと負数を認め、存在論的意味と分離する |
| 5-5は宇宙の別地点への移動である | Local Zero Axiomとして保持する。具体的な移動先の確定だけはsource、destination、quantity、evidenceを要求する |
| 物理学へ適用できる | 現時点では類比。個別領域で予測と反証条件が必要 |
| 無限総量は自動的に豊穣倫理を導く | 宇宙無限性は仮説として保持し、現在のAccessと局所的希少性を別に測る |
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

ここでいう関係性の無限は、同じEdgeへの永久接続ではない。ある関係が終了しても、
Node、影響、義務、記録、別の接続可能性まで終端化しないというContinuity
Postulateである。Exit、Hold、Fork、別Meshへの接続も、関係Topologyを紡ぐ
変化として含む。

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
6. Abundance HorizonとScarcity DisciplineをN-Zeroの対となる原則として
   採用するか。

Approveは物理仮説の正しさ、数学的新規性、Apertureへの正式採用を意味しない。
意味するのは、これらを混同せず別々に検証できる構造へ移行することへの合意である。
