<a id="top"></a>

<div align="center">

# AI Startup Skills · AI 起業 Skill パック

**アイデア検証から会社設立まで。一人会社で AI プロダクトを作る 7 つの Agent Skill を、一度のインストールで揃えます。**

[![CI](https://github.com/huaxialucaicaizi/ai-startup-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/huaxialucaicaizi/ai-startup-skills/actions/workflows/ci.yml)
[![Non-Commercial / 非商业](https://img.shields.io/badge/License-Non--Commercial%20%2F%20非商业-blue.svg)](./LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/huaxialucaicaizi/ai-startup-skills?style=social)](https://github.com/huaxialucaicaizi/ai-startup-skills)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-Codex%20%7C%20Claude%20Code%20%7C%20Cursor-blue)](https://learn.chatgpt.com/docs/build-skills)

<a href="assets/promo/ai-startup-skills-promo.mp4"><img src="assets/promo/cover.jpg" alt="AI 创业 Skill 包宣传片 · Promo film" width="720"></a>

▶ 35秒の紹介動画を見る · Watch the 35-second film

[中文](./README.md#zh) | [English](./README.md#en) | [日本語](#ja)

</div>

---

<a id="ja"></a>

## 日本語

### 目次
- [一言でいうと](#ja-intro)
- [7 ステップのツールキット](#ja-steps)
- [合集と単体インストールの違い](#ja-diff)
- [向いている人 / 向いていない人](#ja-fit)
- [クイックスタート](#ja-quickstart)
- [使い方](#ja-usage)
- [原則](#ja-principles)
- [ディレクトリ構成](#ja-structure)
- [同期と更新](#ja-sync)
- [よくある質問](#ja-faq)
- [コントリビュートとフィードバック](#ja-contrib)
- [作者](#ja-author)
- [ライセンス](#ja-license)

<a id="ja-intro"></a>
### 一言でいうと

「一人会社ツールキット」の合集リポジトリです。独立した 7 つの Agent Skill をまとめ、さらに**ルーター skill** を付けています。何を作っているか、どこまで進んだかを伝えれば、今どの起業段階にいるかを判断し、対応するサブ skill を呼び出します。

**課題**
- 一人で AI プロダクトを作ると、検証、BP 作成、政策申請、ロードショー、顧客獲得、価格設定、登記まで、すべて自分で調べる必要がある
- 7 つの skill を別々に入れるのは手間で、どれから使えばよいかも分かりにくい
- 各ステップの成果物（検証の根拠、BP、価格設定）は次のステップにつなげて使うべきで、バラバラに書いてはいけない

<a id="ja-steps"></a>
### 7 ステップのツールキット

各ステップは、単体でもインストールできる独立リポジトリです：

| ステップ | Skill | 何を解決するか |
|---|---|---|
| 1 | [**AI MVP Validation · AI プロダクト MVP 検証**](https://github.com/huaxialucaicaizi/ai-mvp-validation) | コードや BP を書く前に、まず需要があるかを検証する |
| 2 | [**Business Plan Skill · 事業計画書**](https://github.com/huaxialucaicaizi/business-plan-skill) | BP、ロードショー資料、インキュベーターやコンテストの申請 |
| 3 | [**OPC Policy Navigator · 一人会社政策ナビ**](https://github.com/huaxialucaicaizi/opc-policy-navigator) | 申請できる政策、補助金、計算資源クーポン、OPC コミュニティを調べる |
| 4 | [**AI Pitch Coach · ロードショーコーチ**](https://github.com/huaxialucaicaizi/ai-pitch-coach) | 産業パーク、インキュベーター、起業コンテスト向けのロードショー原稿と審査員 Q&A |
| 5 | [**OPC Growth Playbook · 一人会社の顧客獲得**](https://github.com/huaxialucaicaizi/opc-growth-playbook) | 小紅書、抖音、動画号でのコールドスタートによる顧客獲得 |
| 6 | [**OPC Pricing & Sales · 価格設定と成約**](https://github.com/huaxialucaicaizi/opc-pricing-sales) | 価格設定、プラン、見積書、私域での成約 |
| 7 | [**OPC Registration & Compliance · 一人会社の登記とコンプライアンス**](https://github.com/huaxialucaicaizi/opc-registration-compliance) | 事業主体の選定、登記チェックリスト、年次報告とコンプライアンスカレンダー |

<a id="ja-diff"></a>
### 合集と単体インストールの違い

| いずれか 1 つの skill を単体インストール | AI 起業 Skill パックをインストール |
|---|---|
| どれを使うかは自分で判断する | ルーター skill が段階に応じて選ぶ |
| 各ステップの成果物は独立している | 前のステップの結果を次へ渡す（検証の根拠 → BP → 政策申請 / ロードショー） |
| 7 つのリポジトリを別々に入れて更新する | 一度入れれば、`scripts/sync.sh` で一括同期できる |

その 1 ステップだけが必要なら、対応する独立リポジトリを入れてください。

<a id="ja-fit"></a>
### 向いている人 / 向いていない人

**向いている人**
- 中国で AI ツール、AI アプリ、Agent を作っている一人会社とアーリーステージの創業者
- 「検証 → BP → 政策 → ロードショー → 顧客獲得 → 価格設定 → 登記」を順に進めたい人

**向いていない人**
- 正式な法律・税務の助言が必要な場合：本ツールキットは情報の参照用です。公式の原文と専門家の意見に従ってください
- VC 向けの資金調達ピッチ：ロードショーコーチが対象にしているのは産業パーク、インキュベーター、起業コンテストです

<a id="ja-quickstart"></a>
### クイックスタート

**1. インストール**

本リポジトリをクローンし、`skills/` 以下の 7 つのサブ skill とルーターを、スキルディレクトリにまとめて置きます。

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

Agent Skills に対応したほかのツール（Cursor など）でも、それぞれの方法でインストールできます。仕様は [OpenAI Codex skills](https://learn.chatgpt.com/docs/build-skills) を参照してください。

**2. 使い始める**

```text
ai-startup-skills を使って、今どの起業段階にいるか、次に何をすべきかを教えて：___（作っているプロダクト、ここまで進んだこと）
```

ステップを直接指定することもできます。例：

```text
opc-pricing-sales を使って、この AI プロダクトの価格を決めて：___
```

<a id="ja-usage"></a>
### 使い方

1. 何を作っているか、どこまで進んだかを明確に伝える
2. ルーターが段階を判断し、質問は最大 2 つまで。その後、対応するサブ skill を呼び出す
3. 各ステップのあと、次に何をすべきかとその理由を提示する
4. 新規創業者の既定の順：1 → 2 → 3 / 7 → 4 → 5 → 6。ステップ 3 と 7 は並行できる。政策申請の前に、事業主体の登記が必要になることが多い

<a id="ja-principles"></a>
### 原則

- **データを捏造しない**：業界平均、事例、ユーザー評価をでっち上げない。例はすべてフィクションと明記する
- **公式ソースだけを使う**：政策、法令、プラットフォーム規則には公式原文のリンクを付ける
- **情報の参照であり、法律・税務の助言ではない**
- **サブ skill のルールが優先**：あるステップに入ったら、そのステップの SKILL.md に従う

<a id="ja-structure"></a>
### ディレクトリ構成

```text
ai-startup-skills/
├── SKILL.md                 # ルーター：段階に応じてサブ skill へ振り分ける
├── agents/openai.yaml
├── skills/
│   ├── ai-mvp-validation/            # ステップ 1
│   ├── business-plan-skill/          # ステップ 2
│   ├── opc-policy-navigator/         # ステップ 3
│   ├── ai-pitch-coach/               # ステップ 4
│   ├── opc-growth-playbook/          # ステップ 5
│   ├── opc-pricing-sales/            # ステップ 6
│   └── opc-registration-compliance/  # ステップ 7
├── scripts/
│   ├── validate.py          # ルーターと 7 つのサブ skill の frontmatter を検証
│   └── sync.sh              # 7 つの独立リポジトリから skills/ へ再取得
├── CHANGELOG.md
└── LICENSE
```

<a id="ja-sync"></a>
### 同期と更新

7 つのサブ skill の源泉は、それぞれの独立リポジトリです。最新版を取り込むには：

```bash
./scripts/sync.sh
python3 scripts/validate.py
```

<a id="ja-faq"></a>
### よくある質問

**Q：7 ステップをすべて通す必要がありますか？**<br>
A：不要です。ルーターは、まだ終わっていない最も早いステップから始めます。ステップを直接指定することもできます。

**Q：合集と独立リポジトリの内容は同じですか？**<br>
A：同じです。`skills/` の内容は `scripts/sync.sh` が独立リポジトリから同期しています。ステップ固有の問題は、まず対応する独立リポジトリへ報告してください。

**Q：政策や法令の情報は古くなりませんか？**<br>
A：古くなります。サブ skill は公式リンクだけを引用しています。使う前に原文を開いて最新版を確認してください。

**Q：中国以外の市場でも使えますか？**<br>
A：検証、BP、ロードショー、価格設定の考え方は汎用です。政策ナビ、登記とコンプライアンス、プラットフォームでの顧客獲得は、主に中国大陸向けです。

<a id="ja-contrib"></a>
### コントリビュートとフィードバック

- 特定ステップの問題や提案：対応する独立リポジトリで Issue を開いてください
- ルーターや合集の構成に関する問題：本リポジトリで [Issue](https://github.com/huaxialucaicaizi/ai-startup-skills/issues) を開いてください
- PR を出す前に `python3 scripts/validate.py` を実行してください
- 法令やプラットフォーム規則を引用する場合は、公式原文のリンクを付けてください

<a id="ja-author"></a>
### 作者

**华夏路菜菜子**：元大手テック企業の AI プロダクトグロース担当。現在は AI 起業家、「一人会社ツールキット」の作者。

- GitHub：[@huaxialucaicaizi](https://github.com/huaxialucaicaizi)

このツールキットが役に立ったら、Star ⭐ をいただけると嬉しいです。

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=huaxialucaicaizi/ai-startup-skills&type=Date&t=20261026)](https://star-history.com/#huaxialucaicaizi/ai-startup-skills&Date)

<a id="ja-license"></a>
### ライセンス

本プロジェクトは商用利用を禁止します。個人の学習および非商用目的であれば無料で利用できます。作者の事前の許可なく、本プロジェクトを第三者の AI プロダクトや Skill ストアに掲載してはなりません。転載または掲載を希望する場合は、GitHub で作者 [@huaxialucaicaizi](https://github.com/huaxialucaicaizi) までご連絡ください。詳細は [LICENSE](./LICENSE) を参照してください。

[↑ 先頭に戻る](#top)
