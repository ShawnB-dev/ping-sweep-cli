# Ping Sweep Tool / Ping Sweep ツール

This project provides a simple Python-based ping sweep tool for discovering active hosts in a subnet.  
本プロジェクトは、指定したサブネット内のアクティブホストを検出する Python ベースの ping スイープツールです。

---

## Features / 機能

- ICMP ping host discovery  
- IPv4 subnet scanning  
- Summary statistics  
- CLI-based workflow  

---

## Usage / 使い方
```markdown
python3 ping_sweep.py
```

Enter a subnet / サブネットを入力：
```markdown
192.168.1.0/24
```


---

## Output Example / 出力例
```markdown
[+] 192.168.1.1 is alive [-] 192.168.1.2 is down
```


---

## Roadmap / ロードマップ

- Parallel scanning / 並列スキャン  
- JSON output / JSON 出力  
- Timeout configuration / タイムアウト設定  
- Web UI / Web UI  
