# Ping Sweep Tool (Python CLI)



A simple Python-based ping sweep tool that scans a subnet and identifies which hosts respond to ICMP echo requests.

This project demonstrates practical networking knowledge and Python scripting skills.

---

## Usage

Run the script:
```markdown
python3 ping_sweep.py
```

Enter a subnet:
```markdown
192.168.1.0/24
```

Example Output: 
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

## Skills Demonstrated

- Python scripting  
- ICMP ping automation  
- Network scanning  
- CLI tool development  
- Input validation  
- Networking fundamentals  

---

## Future Enhancements

- Parallel scanning (threading)
- JSON output mode
- Timeout configuration
- Web UI (Flask)
- GUI version (Tkinter)