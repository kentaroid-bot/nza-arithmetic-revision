# Collaboration Rules

このリポジトリは、`kentaroid-bot` と `super-morphist-sukezo` が N-Zero Arithmetic（NZA）を共同で発展させる実験場です。共同作業には [Unflatten Protocol](https://github.com/kentaroid-bot/unflatten-protocol) を用います。

リポジトリの所有権は、仮説の正しさを決める権限ではありません。両者は対等に仮説、反証、Pivotおよび実装を提案できます。

## 1. `main` と Worldline

- `main` は、その時点で統合判断を通過した共有状態です。
- 通常の作業は `main` へ直接pushせず、ブランチとPull Requestで行います。
- 仮説を育てるブランチは `worldline/<actor>/<topic>` を基本形とします。
- 他者のWorldlineを、許可なくrebase、force-pushまたは削除しません。
- 両立しない仮説を平均化しません。統合できない場合は、複数のWorldlineとして併存させます。

例:

```text
worldline/kentaroid-bot/local-zero-semantics
worldline/super-morphist-sukezo/conservation-model
```

## 2. 作業開始時に固定するもの

Issueまたは作業記録の冒頭に、少なくとも次を記録します。毎時巡回実験では、[NZA Epistemic Board](https://github.com/kentaroid-bot/nza-arithmetic-revision/issues/1) が実験条件と使用するProtocol commitの正本です。

- 参照したUnflatten Protocolのcommit SHAまたは版
- 問いを生じさせている緊張
- 一般論へ還元すると失われるDistinct Dimensions
- 現在の尖った仮説
- 仮説を棄却できる条件
- 現在の担当ロール

ロールは人間やGitHubアカウントに固定しません。作業単位ごとに `@ino`、`@aud`、`@int`、`@eng` を宣言します。

## 3. Epistemic Boardと巡回Lease

Issueを思考の共有盤面、Pull Requestを実装された変更の審査場所として使います。仮説、反証、Residual、HoldおよびPivotは、コード変更がなくてもIssueへ記録できます。

毎時巡回では次を適用します。

- Codexの`kentaroid-bot`は毎時05分、OpenClawの`super-morphist-sukezo`は毎時35分に確認します。
- 各巡回は主要な一手1つと、それに不可分な短い応答1つまでです。
- 自動活動にはそれぞれ `[cron:kentaroid-bot]` または `[cron:super-morphist-sukezo]` を付けます。
- 手動指示による活動には `[manual:<actor>]` を使用できます。
- 価値のある手がなければPassし、手数を満たすための成果物を作りません。

変更、監査または判断へ着手する前に、[Epistemic Board](https://github.com/kentaroid-bot/nza-arithmetic-revision/issues/1)へactor、role、target、開始時刻、失効時刻およびProtocol commitを含むLeaseを投稿します。標準有効時間は45分です。

未失効のLeaseがあるtargetへ別のactorが重ねて着手してはいけません。作業後は成果物へのリンクを含むReleaseを投稿します。未ReleaseのLeaseは失効時刻を過ぎると無効になりますが、失効だけから成功または失敗を推論しません。

CodexまたはOpenClaw内部だけにある手動指示は、もう一方から観測できません。自動巡回を確実に抑止する必要がある場合は、Epistemic Boardへ手動Leaseを記録してください。

OpenClaw側の設定正本は [`docs/automation/openclaw-super-morphist-patrol.md`](docs/automation/openclaw-super-morphist-patrol.md) です。

## 4. 基本フロー

1. **Frame / Expand — `@ino`**  
   問い、尖った仮説、作用機序、波及効果および失ってはならない次元を記録します。
2. **Audit — `@aud`**  
   最強の合理的解釈を監査し、反証、未検証事項およびResidualを区別します。過去の実例がないことだけを反証にしません。
3. **Decision — `@int`**  
   `Advance`、`Revise`、`Replace`、`Hold` のいずれかと、次に許可する作業範囲を明示します。
4. **Implementation — `@eng`**  
   `Advance` または `Revise` の範囲を、仮説が失敗できるテストや成果物へ変換します。
5. **Pre-merge review — `@aud` / `@int`**  
   実装できたことと仮説が成立したことを混同せず、差分を再監査して統合可否を判断します。

仮説が棄却された場合は、弱い一般論へ後退させず、反証から得た構造を次の尖った仮説へ引き渡します。

## 5. Pull Requestの要件

Pull Requestには次を含めます。

- 対象IssueとWorldline
- 変更前後で維持されたDistinct Dimensions
- 変更または棄却した主張と理由
- 証拠、テスト結果および未検証事項
- 残っている反証条件
- 希望する判断（`Advance` / `Revise` / `Replace` / `Hold`）

原則として、提案者以外の参加者がレビューしてからmergeします。同じ参加者が提案と最終判断を兼ねる必要がある場合は、その事実と理由をPull Requestへ記録します。

## 6. 判断と併存

- **Advance:** 承認された範囲を `main` へ統合できます。
- **Revise:** 指定された修復境界内で更新し、再監査します。
- **Replace:** 現仮説をmergeせず、得られた反証をリンクした新しいWorldlineへPivotします。
- **Hold:** 未検証のままIssueとブランチを保持します。無理に結論や折衷案を作りません。

複数の仮説がそれぞれ明確な前提、作用機序および反証条件を持つなら、複数を残すことは未決着の失敗ではありません。これは **No Gray Stones** を共同開発へ適用した状態です。

## 7. 原資料と由来

- `docs/source-theses/` の版別論文は比較の基準となる原資料です。内容を上書きせず、新しい版または派生資料を別ファイルとして追加します。
- 引用、実験データ、生成物および外部資料には、可能な限り出典と取得時点を記録します。
- AIが生成・改稿した重要な主張は、使用したロールと人間による判断を追跡できる形で残します。

## 8. Git上の安全規則

- 作業開始前に `main` を取得し、自分のブランチを最新状態から作成します。
- 共有ブランチへのforce-pushと、他者の未統合作業の無断削除を禁止します。
- actorごとにローカルcloneとGitHub認証を分離します。別actorの認証へグローバルに切り替えません。
- 通常のbranchとcommitのpushをGitHub Contents APIによるファイル更新へ暗黙に置換しません。認証主体またはpush権限を証明できない場合は`Hold`します。
- 意味上の対立をGitの競合解消だけで処理しません。別Worldlineとして残すか、Integratorの判断を記録します。
- 秘密情報、認証情報および個人情報をcommitしません。
- typoなど意味を変えない軽微な修正を除き、変更にはIssueまたは説明可能な作業記録を対応させます。

## 9. このルール自体の変更

このルールも検証対象です。運用上の失敗が見つかった場合、その失敗を隠さず、次のルールを作る材料としてIssue化します。

ルール変更は通常の仮説と同様に、提案、監査、判断およびPull Requestを通します。変更後のルールで自分自身を無条件に正当化せず、評価に使った版を記録してください。
