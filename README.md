#  Kcal-calculator-AI

**AI-Powered Food Classification & Calorie Estimation**  
**AI による食品分類・カロリー推定システム**

---

##  Language / 言語

- [English](#english)
- [日本語](#japanese)

---

<a name="english"></a>
# 🇬🇧 English

## Introduction — What is this?

Kcal-calculator-AI is a serverless food classification system that uses deep learning to identify food from a photo and instantly return its estimated calorie content.
You take a picture. The AI tells you what it is and how many calories it contains per 100g. That's it. No typing, no searching, no manual logging.
The system currently recognises 10 food categories: 
**Pizza, Sushi, Ramen, Hamburger, Caesar Salad, Fried Rice, Steak, Hot Dog, Ice Cream, and Gyoza**.

---

## Concept 

I am creating this small AI project to learn Python, FastAPI, Google Colab, and PyTorch. Even though I might use AI to help generate the code, my goal is to learn by asking about every single line it creates. I plan to ask questions frequently to make the learning process fun. I hope to apply these skills in my future career.

---

## How it works

```
User uploads a photo
        ↓
FastAPI receives the image file
        ↓
PIL opens and converts to RGB
        ↓
Image resized to 224×224 and normalized
        ↓
MobileNetV2 (fine-tuned on Food-101) runs inference
        ↓
Predicted class mapped to calorie database
        ↓
JSON response returned to user
```

**Model details:**
- Architecture: MobileNetV2 (pretrained on ImageNet)
- Training method: Transfer Learning — final classifier layer replaced and fine-tuned
- Dataset: Food-101 (10 selected classes, ~75,000 training images)
- Training platform: Google Colab (T4 GPU)
- Input size: 224 × 224 pixels
- Normalization: ImageNet mean/std `[0.485, 0.456, 0.406]` / `[0.229, 0.224, 0.225]`

**API response example:**
```json
{
  "food": "ramen",
  "confidence": 91.4,
  "kcal_per_100g": 436,
  "portion_note": "Estimate assumes 100g. Adjust for actual portion."
}
```

---

## Tech Stack
```
├── app/
│   ├── main.py          # FastAPI Logic
│   ├── model.py         # AI Inference Logic
│   ├── calorie_db.py    # Food Data & Kcal
│   └── model.pth        # Trained Weights (Git-ignored if large)
├── Dockerfile
└── requirements.txt
```
---

## How to use

### Run locally

**1. Clone the repository**
```bash
git clone https://github.com/ToeyAumpon/Kcal-calculator-AI.git
cd Kcal-calculator-AI
```

**2. Install dependencies**
```bash
pip install fastapi uvicorn pillow python-multipart torch torchvision
```

**3. Place your trained model**

Download `model.pth` and place it inside the `app/` folder:
```
app/
└── model.pth
```

**4. Start the server**
```bash
python -m uvicorn app.main:app --reload
```

**5. Open the API docs**

Go to `http://localhost:8000/docs` in your browser.  
Click **POST /predict → Try it out → Choose File → Execute**.

---

## Features planned for implementation

- [ ] Support more food categories (expanding beyond 10 classes)
- [ ] Portion size estimation from image (not just per 100g)
- [ ] Meal history logging with daily calorie totals
- [ ] Simple web front-end for browser-based uploads
- [ ] Nutrition breakdown beyond calories (protein, carbs, fat)
- [ ] Mobile app integration via REST API

---

## Final note

This project taught me that building a real AI system is less about the model and more about everything around it — data pipelines, API design, containerization, and deployment. The model is maybe 20% of the work.

If you're reading this and considering a similar project, start small (10 classes, not 101), use Transfer Learning (don't train from scratch), and get something working end-to-end before making it perfect.


---

<a name="japanese"></a>
# 🇯🇵 日本語

## はじめに 

Kcal-calculator-AI は、ディープラーニングを活用した食品分類システムです。料理の写真を1枚送るだけで、AIが食品の種類を識別し、100gあたりの推定カロリーを即座に返します。
入力するのは写真だけ。文字を打つ必要も、手動で調べる必要もありません。
現在対応している食品は10種類です：**ピザ、寿司、ラーメン、ハンバーガー、シーザーサラダ、チャーハン、ステーキ、ホットドッグ、アイスクリーム、餃子**

---

## コンセプト

Python、FastAPI、Google Colab、PyTorchを学ぶために、この小さなAIプロジェクトを作っています。AIを使ってコードを生成することもありますが、生成されたすべてのコードについて質問し、仕組みを理解することで学習したいと思っています。楽しみながら学ぶために、何度も質問するつもりです。将来、仕事でこれらのスキルを活かせるようになることが目標です。

---

## デモ

*(Coming soon — ライブURLは近日公開予定)*

---

## 環境・技術スタック
---

```
├── app/
│   ├── main.py          # FastAPI Logic
│   ├── model.py         # AI Inference Logic
│   ├── calorie_db.py    # Food Data & Kcal
│   └── model.pth        # Trained Weights (Git-ignored if large)
├── Dockerfile
└── requirements.txt
```
---


## 利用方法

### ローカルで動かす

**1. リポジトリをクローン**
```bash
git clone https://github.com/ToeyAumpon/Kcal-calculator-AI.git
cd Kcal-calculator-AI
```

**2. 依存パッケージをインストール**
```bash
pip install fastapi uvicorn pillow python-multipart torch torchvision
```

**3. 学習済みモデルを配置**

`model.pth` を `app/` フォルダ内に置きます：
```
app/
└── model.pth
```

**4. サーバーを起動**
```bash
python -m uvicorn app.main:app --reload
```

**5. APIドキュメントを開く**

ブラウザで `http://localhost:8000/docs` にアクセス。  
**POST /predict → Try it out → ファイルを選択 → Execute** で動作確認できます。


その後 `http://localhost:8000/docs` にアクセスしてください。

---

## 実装予定の機能

[ ] 対応食品カテゴリの拡張 (10クラス以上)
[ ] 画像からの食事量推定 (100g固定ではなく実際の量に対応)
[ ] 食事履歴の記録と1日の合計カロリー表示
[ ] ブラウザからアップロードできるシンプルなWebフロントエンド
[ ] カロリー以外の栄養素情報 (タンパク質・炭水化物・脂質) の表示
[ ] REST APIを通じたモバイルアプリとの連携

---

## 終わりに

このプロジェクトを通じて学んだのは、本物のAIシステムの構築において、モデル自体よりもその周辺の仕組み（データパイプライン、API設計、コンテナ化、デプロイメント）が重要であるということです。モデル自体の作業は、全体の約20%に過ぎないかもしれません。

---
