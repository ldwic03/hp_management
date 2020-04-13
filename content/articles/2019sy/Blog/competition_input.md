Title: はじめての競プロ：入力アンチョコメモ
Date: 2019.04.27
Modified: 2019.04.29
Tags: 競技プログラミング
Slug: competition_input
Author: 小川
Summary: AtCoderのABCで、これさえ覚えれば大丈夫！な入力のパターンについて解説します。

## 入力のパターン

**Python会競プロ部（？）へようこそ！**

はじめての方には**入力**が最初の鬼門だと思います。  
[AtCoder](https://atcoder.jp) のABCで、**これさえ覚えれば大丈夫！**な入力パターンは以下の通り。
最初は説明の意味がわからなくても、とりあえずコピペすれば動きます（何）。

**言語**は `Python3 (3.4.3)` (または `PyPy3 (2.4.0)`) を選択してね。

### 文字列を入力
```python
S = input()
```

### 整数ひとつを入力
```python
A = int(input())
```
`int()` が、文字列を整数 (integer) に変換する**呪文**です。

### 整数2つ〜を一行（空白区切り）で入力
```python
A, B = map(int, input().split())
```
```python
A, B, C = map(int, input().split())
```
まず `split()` で文字列を分割。
次に `map()` で `int()` をそれぞれに適用しています。

### 多数の整数を一行で入力
```python
x = list(map(int, input().split()))
```
`x` は0番目から始まる配列になる。n番目は `x[n]` で参照します。


## 使用例
### 問題1
整数A, Bが1行 (空白区切り) で

```
A B
```
のように与えられる。和 `A+B` を出力せよ。

**解答例**

```python
A, B = map(int, input().split())
print(A+B)
```

### 問題2
1行目に自然数 `N`, `K` (`N>=K`)、2行目にN個の整数 `x1,..,xN` が、

```
N K
x1 x2 x3 ... xN
```
のように与えられる。
このうちK番目の整数xKを出力せよ。

**解答例**

```python
N, K = map(int, input().split())
x = list(map(int, input().split()))
print(x[K-1])
```
配列が0番目からであることに注意。
`N` は実は使わなくてよい。  
ちょっと難しいパターンだが、B問題ではちょくちょく出てくる。

### 問題3
<s>(このパターンはたぶんC問題以降のみ。)</s> B問題にも時々出ます。  
1行目に自然数 `N`, `K` (`N>=K`)、2行目〜N+1行目に `N `個の整数 `x1,..,xN` が、

```
N K
x1
x2
x3
...
...
xN
```
のように与えられる。
このうち `K` 番目の整数 `xK` を出力せよ。

**解答例**

```python
N, K = map(int, input().split())
x = []
for i in range(N):
	x.append(int(input()))
print(x[K-1])
```
ループとの組み合わせ。<s>C問題</s> B問題以降でときどき必要。

以上です。おしまい。
