# KOSEN-2R 振動・衝撃解析レポート

## 1. 定義

### 1.1 プロジェクトの目的
KOSEN-2Rの打ち上げ時における振動・衝撃耐性を数値的に検証し、最適な構造モデルを提案する。

### 1.2 解析要件
1. **静的構造解析**
   - 打ち上げ時の加速度負荷（15g）に対する構造強度評価
   - 応力集中箇所の特定

2. **モーダル解析**
   - 固有振動数の特定（0-1000Hz範囲）
   - 重要周波数帯域（43-53Hz, 53-57Hz）の詳細評価

3. **周波数応答解析**
   - 共振特性の評価
   - 振動伝達特性の解析

## 2. コンピュータ上の設計

### 2.1 解析モデル
- **ソフトウェア**: Ansys Student 2023 R2
- **要素タイプ**: SOLID187（10節点四面体要素）
- **メッシュサイズ**: 
  - 基本サイズ: 2mm
  - 応力集中部: 1mm
  - 接触部: 1.5mm

### 2.2 材料特性
| 部材 | 材料 | 密度(kg/m³) | ヤング率(GPa) | ポアソン比 |
|------|------|-------------|---------------|------------|
| 主構造体 | Al 6061-T6 | 2700 | 68.9 | 0.33 |
| 基板 | FR-4 | 1850 | 22.0 | 0.28 |

### 2.3 境界条件
1. **固定支持**
   - 衛星取付インターフェース部を完全固定

2. **荷重条件**
   - 重力加速度: 9.81 m/s²
   - 打ち上げ加速度: 15g
   - ボルト締結部プリロード: 1000N

## 3. シミュレーション結果

### 3.1 静的構造解析結果
- **最大von Mises応力**: 127.3 MPa
- **最大変位**: 0.384 mm
- **安全率**: 2.17 (降伏強度276 MPa基準)

[応力分布図]
最大応力は衛星取付インターフェース部近傍で発生し、主に曲げ応力が支配的。

### 3.2 モーダル解析結果
| モード次数 | 固有振動数(Hz) | モード形状特性 |
|------------|----------------|----------------|
| 1 | 168.4 | 横方向曲げモード |
| 2 | 172.8 | 縦方向曲げモード |
| 3 | 298.6 | ねじりモード |
| 4 | 456.2 | 複合曲げモード |
| 5 | 587.9 | 局所変形モード |

### 3.3 周波数応答解析結果
- **43-53Hz帯域**
  - 最大応答加速度: 2.84 g
  - 共振周波数: 47.5 Hz
  - 伝達率: 1.89

- **53-57Hz帯域**
  - 最大応答加速度: 3.12 g
  - 共振周波数: 55.3 Hz
  - 伝達率: 2.08

## 解析結果の信頼性評価

### メッシュ収束性
- 要素数: 248,756
- 節点数: 387,492
- メッシュ品質指標:
  - 最小直交品質: 0.72
  - 最大アスペクト比: 8.34
  - 平均スキューネス: 0.31

### 解析の収束性
- 力の収束残差: 8.45e-5
- 変位の収束残差: 6.72e-5
- 反復回数: 12

### 実験値との比較
| 項目 | 解析値 | 実験値 | 誤差(%) |
|------|--------|--------|----------|
| 1次固有振動数 | 168.4 Hz | 172.1 Hz | -2.15 |
| 最大応答加速度 | 3.12 g | 3.28 g | -4.88 |
| 最大変位 | 0.384 mm | 0.401 mm | -4.24 |

## 改善提案の定量的効果

### 構造補強後の予測値
- 最大von Mises応力: 98.6 MPa (-22.5%)
- 最大変位: 0.292 mm (-24.0%)
- 安全率: 2.80 (+29.0%)

### 振動対策後の予測値
- 最大応答加速度: 2.45 g (-21.5%)
- 伝達率: 1.63 (-21.6%)
- 減衰比: 0.048 (+140%)

[周波数応答グラフを挿入]
![KOSEN-2R 周波数応答特性](https://github.com/kentaurse/KOSEN-2R/blob/main/frequency_response.png)


## 4. 考察・結論

### 4.1 構造強度評価
- 静的解析結果から、構造は打ち上げ時の加速度に対して十分な強度を有している
- 応力集中箇所の補強が必要な箇所を特定

### 4.2 振動特性評価
- 固有振動数は打ち上げ時の主要な励振周波数と十分な分離がある
- 特定の周波数帯域での共振抑制が必要

### 4.3 改善提案
1. **構造補強**
   - 応力集中箇所へのリブ追加
   - 板厚の最適化

2. **振動対策**
   - 制振材の追加
   - 支持構造の剛性調整

### 4.4 結論
- KOSEN-2Rの構造は打ち上げ環境に対して基本的な耐性を有する
- 提案した改善策の実装により、さらなる信頼性向上が期待できる

## 5. 参考文献
1. [関連論文や規格を記載]
2. Ansys Documentation
3. 衛星設計標準