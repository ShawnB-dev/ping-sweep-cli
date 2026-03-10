# Ping Sweep ツール（Python CLI）

このツールは、指定したサブネット内のホストに ICMP ping を送信し、応答があるホストを一覧表示します。

ネットワークエンジニアが日常的に行う作業を自動化する、実用的な Python スクリプトです。

---

## 使い方
```markdown
python3 ping_sweep.py
```


サブネットを入力します：
```markdown
192.168.1.0/24
```


出力例：
```markdown
=== Ping Sweep: 192.168.1.0/24 === 
[+] 192.168.1.1 is alive 
[-] 192.168.1.2 is down 
... 

=== Summary === 
Total hosts: 254 
Alive: 12 
Down: 242
```

---

## このプロジェクトで示せるスキル

- Python スクリプト開発  
- ICMP ping 自動化  
- ネットワークスキャン  
- CLI ツール設計  
- 入力バリデーション  
- ネットワーク基礎知識  

---

## 今後の拡張案

- 並列スキャン（スレッド）
- JSON 出力モード
- タイムアウト設定
- Web UI（Flask）
- GUI（Tkinter）
