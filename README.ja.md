<a id="top"></a>

<div align="center">

# AI Startup Skills · AI 起業 Skill パック

**アイデアの検証から会社の登記まで、一人会社で AI プロダクトを作るための 7 つのエージェントスキルを、一度にまとめてインストールできます。**

[![CI](https://github.com/huaxialucaicaizi/ai-startup-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/huaxialucaicaizi/ai-startup-skills/actions/workflows/ci.yml)
[![Non-Commercial / 非商业](https://img.shields.io/badge/License-Non--Commercial%20%2F%20非商业-blue.svg)](./LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/huaxialucaicaizi/ai-startup-skills?style=social)](https://github.com/huaxialucaicaizi/ai-startup-skills)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Claude%20Code%20%7C%20Cursor-blue)](https://learn.chatgpt.com/docs/build-skills)

[中文](./README.md#zh) | [English](./README.md#en) | [日本語](#ja)

</div>

---

<a id="ja"></a>

## 日本語

### 目次
- [ひとことで言うと](#ja-intro)
- [7 ステップのツールキット](#ja-steps)
- [バンドル版と単体版の違い](#ja-diff)
- [対象となる人](#ja-fit)
- [クイックスタート](#ja-quickstart)
- [使い方](#ja-usage)
- [原則](#ja-principles)
- [ディレクトリ構成](#ja-structure)
- [同期と更新](#ja-sync)
- [FAQ](#ja-faq)
- [コントリビュート](#ja-contrib)
- [作者](#ja-author)
- [ライセンス](#ja-license)

<a id="ja-intro"></a>
### ひとことで言うと

一人会社ツールキットのバンドルリポジトリです。7 つの独立したエージェントスキルと、1 つの **ルータースキル** で構成されています。何を作っていて、どこまで進んでいるかを伝えると、今どの段階にいるかを判断し、対応するサブスキルに引き継ぎます。

**課題**
- 一人で AI プロダクトを作ると、検証、事業計画書（BP）、政策の申請、ピッチ、グロース、価格設定、登記をすべて自分で考えなければなりません
- 7 つのスキルを 1 つずつインストールするのは手間がかかり、どれから使えばよいのかもわかりにくいです
- 各ステップの成果物（検証の根拠、BP、価格設定）は、次のステップに引き継がれるべきです

<a id="ja-steps"></a>
### 7 ステップのツールキット

各ステップは、単体でインストールできる独立したリポジトリでもあります：

| ステップ | スキル | 内容 |
|---|---|---|
| 1 | [**AI MVP Validation**](https://github.com/huaxialucaicaizi/ai-mvp-validation) | 開発や BP の作成に取りかかる前に需要を検証します |
| 2 | [**Business Plan Skill**](https://github.com/huaxialucaicaizi/business-plan-skill) | 事業計画書、ピッチの内容、インキュベーターやコンペティションへの申請 |
| 3 | [**OPC Policy Navigator**](https://github.com/huaxialucaicaizi/opc-policy-navigator) | 政策、補助金、計算資源クーポン、OPC コミュニティスペースを探します |
| 4 | [**AI Pitch Coach**](https://github.com/huaxialucaicaizi/ai-pitch-coach) | 産業パーク、インキュベーター、コンペティション向けのロードショーの原稿と審査員との質疑応答 |
| 5 | [**OPC Growth Playbook**](https://github.com/huaxialucaicaizi/opc-growth-playbook) | 小紅書、抖音、WeChat Channels でのコールドスタートからのグロース |
| 6 | [**OPC Pricing & Sales**](https://github.com/huaxialucaicaizi/opc-pricing-sales) | 価格設定、パッケージ、見積書、成約までのプロセス |
| 7 | [**OPC Registration & Compliance**](https://github.com/huaxialucaicaizi/opc-registration-compliance) | 事業形態の選択、登記のチェックリスト、年次報告とコンプライアンスのカレンダー |

<a id="ja-diff"></a>
### バンドル版と単体版の違い

| スキルを 1 つインストール | AI Startup Skills をインストール |
|---|---|
| どのスキルを使うかは自分で決める | ルーターが段階に応じて選ぶ |
| 各ステップの成果物はそれぞれ独立している | 成果物が次へ引き継がれる（検証の根拠 → BP → 政策 / ピッチ） |
| 7 つのリポジトリをインストール・更新する | 1 回のインストールと 1 つの `scripts/sync.sh` で済む |

1 つのステップだけが必要な場合は、その独立したリポジトリをインストールしてください。

<a id="ja-fit"></a>
### 対象となる人

**向いている人**
- 中国で AI ツール、アプリ、エージェントを開発している一人会社やアーリーステージの創業者
- 検証 → BP → 政策 → ピッチ → グロース → 価格設定 → 登記 の順に進めたい人

**向いていない人**
- 正式な法律や税務のアドバイスを求める場合：このツールキットは情報提供のみを目的としています。公式の原文と専門家を頼ってください
- VC からの資金調達のためのピッチ：ピッチコーチは産業パーク、インキュベーター、コンペティションを対象としています

<a id="ja-quickstart"></a>
### クイックスタート

**1. インストール**

このリポジトリをクローンし、`skills/` 以下の 7 つのサブスキルとルーターをスキルディレクトリに配置します。

Codex（ユーザースキルディレクトリ `~/.agents/skills`）：

```bash
git clone https://github.com/huaxialucaicaizi/ai-startup-skills.git
mkdir -p ~/.agents/skills
cp -R ai-startup-skills/skills/* ~/.agents/skills/
cp -R ai-startup-skills ~/.agents/skills/ai-startup-skills
```

Claude Code（ユーザースキルディレクトリ `~/.claude/skills`）：

```bash
git clone https://github.com/huaxialucaicaizi/ai-startup-skills.git
mkdir -p ~/.claude/skills
cp -R ai-startup-skills/skills/* ~/.claude/skills/
cp -R ai-startup-skills ~/.claude/skills/ai-startup-skills
```

エージェントスキルに対応したその他のツール（Cursor など）では、それぞれの方法でインストールできます。仕様：[OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills)。

**2. 使う**

```text
Use ai-startup-skills to tell me which startup stage I am at and what to do next: ___ (what you are building, what you have done)
```

または、ステップを直接呼び出します：

```text
Use opc-pricing-sales to price this AI product: ___
```

<a id="ja-usage"></a>
### 使い方

1. 何を作っていて、どこまで進んでいるかを伝えます
2. ルーターが段階を判断し、最大 2 つの質問をしてから、サブスキルを呼び出します
3. 各ステップの後に、次のステップとその理由を提案します
4. 新しい創業者向けのデフォルトの順序：1 → 2 → 3 / 7 → 4 → 5 → 6。ステップ 3 と 7 は並行して進められます。政策の申請には登記が必要になることがよくあります

<a id="ja-principles"></a>
### 原則

- **データを捏造しない**：架空のベンチマーク、事例、推薦の声は使いません。例は架空であることを明記します
- 政策、法律、プラットフォームのルールは **公式の情報源のみ** を使います
- **情報提供であり、法律や税務のアドバイスではありません**
- 各ステップの中では **サブスキルのルールが優先** されます

<a id="ja-structure"></a>
### ディレクトリ構成

```text
ai-startup-skills/
├── SKILL.md                 # router: routes to sub-skills by stage
├── agents/openai.yaml
├── skills/
│   ├── ai-mvp-validation/            # step 1
│   ├── business-plan-skill/          # step 2
│   ├── opc-policy-navigator/         # step 3
│   ├── ai-pitch-coach/               # step 4
│   ├── opc-growth-playbook/          # step 5
│   ├── opc-pricing-sales/            # step 6
│   └── opc-registration-compliance/  # step 7
├── scripts/
│   ├── validate.py          # checks router + 7 sub-skill frontmatter
│   └── sync.sh              # re-pulls the 7 standalone repos into skills/
├── CHANGELOG.md
└── LICENSE
```

<a id="ja-sync"></a>
### 同期と更新

サブスキルはそれぞれの独立したリポジトリから取り込まれています。最新版を取得するには：

```bash
./scripts/sync.sh
python3 scripts/validate.py
```

<a id="ja-faq"></a>
### FAQ

**Q: 7 つのステップをすべて進める必要がありますか？**<br>
A: いいえ。ルーターはまだ完了していない最も早いステップから始めます。また、ステップを直接指定することもできます。

**Q: バンドルの内容は独立したリポジトリと同じですか？**<br>
A: はい。`skills/` は `scripts/sync.sh` によって独立したリポジトリから同期されています。ステップ固有の問題は、そちらに報告してください。

**Q: 政策や法律の情報が古くなることはありますか？**<br>
A: はい。サブスキルは公式の情報源にのみリンクしています。原文を開いて最新版を確認してください。

**Q: 中国以外でも使えますか？**<br>
A: 検証、BP、ピッチ、価格設定の考え方は汎用的です。政策、登記、プラットフォームでのグロースは中国本土を対象としています。

<a id="ja-contrib"></a>
### コントリビュート

- 特定のステップに関する問題：その独立したリポジトリで Issue を作成してください
- ルーターやバンドルに関する問題：このリポジトリで [Issue](https://github.com/huaxialucaicaizi/ai-startup-skills/issues) を作成してください
- PR を出す前に `python3 scripts/validate.py` を実行してください
- 法律やプラットフォームのルールを引用する場合は、公式の情報源を明記してください

<a id="ja-author"></a>
### 作者

**华夏路菜菜子 (huaxialucaicaizi)**：中国の大手テック企業で AI プロダクトのグロースを率いた後、現在は AI 起業家として活動しています。一人会社ツールキットの作者です。

- GitHub：[@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

このツールキットが役に立ったら、Star ⭐ をいただけると嬉しいです。

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huaxialucaicaizi/ai-startup-skills&type=Date&t=20261026)](https://star-history.com/#huaxialucaicaizi/ai-startup-skills&Date)

<a id="ja-license"></a>
### ライセンス

非商用利用に限ります。個人の学習および非商用の利用は無料です。第三者の AI プロダクトや Skill ストアへの掲載には、作者の事前の許可が必要です。転載や掲載の許可については、GitHub で [@huaxialucaicaizi](https://github.com/huaxialucaicaizi) にご連絡ください。詳しくは [LICENSE](./LICENSE) をご覧ください。

[↑ トップに戻る](#top)
