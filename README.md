# 🔐 Phishing URL Detector

A Python-based cybersecurity project that analyzes URLs and identifies suspicious characteristics using rule-based detection.

## 📌 Project Overview

The Phishing URL Detector is a beginner-friendly cybersecurity tool developed using Python on Kali Linux. It checks URLs for common phishing indicators and calculates a risk score to classify them as **Low Risk, Medium Risk, or High Risk**.

## ✨ Features

- 🔎 Suspicious keyword detection
- 🌐 IP address-based URL detection
- ⚠️ `@` symbol detection
- 🔗 Multiple hyphen detection
- 📏 URL length analysis
- 🔒 HTTPS usage check
- 📊 Risk score calculation
- 🚨 Risk level classification
- 📝 Displays reasons for suspicious results

## 🛠️ Technologies Used

- Kali Linux
- Python 3
- Regular Expressions (`re` module)

## 📂 Project Structure

```text
phishing-url-detector/
├── detector.py
└── README.md
```

## 🚀 How to Run

**Step 1: Open the project directory**

```bash
cd ~/phishing-url-detector
```

**Step 2: Run the program**

```bash
python3 detector.py
```

**Step 3: Enter a URL when prompted**

Example of a normal test URL:

```text
https://example.com
```

Example of a suspicious test URL:

```text
http://192.168.1.10/login/verify/account
```

These are demonstration inputs. Do not open suspicious URLs in a browser.

## ⚙️ How It Works

1. The user enters a URL.
2. The program checks for suspicious keywords and URL patterns.
3. It checks for an IP address, `@` symbol, multiple hyphens, excessive URL length, and absence of HTTPS.
4. Suspicious indicators contribute to a risk score.
5. The program displays the score, risk level, and detected reasons.

## 📊 Risk Classification

| Risk Score | Risk Level |
|---|---|
| 0–1 | Low Risk |
| 2–4 | Medium Risk |
| 5 or more | High Risk |

## 🎯 Project Objective

To demonstrate basic phishing URL analysis and introduce rule-based detection techniques used in cybersecurity.

## ⚠️ Limitations

This project uses simple rules and is intended for educational purposes. It does not verify URLs against live threat-intelligence databases. A low-risk result does not guarantee that a URL is safe, and legitimate URLs may sometimes be flagged as suspicious.

## 👨‍💻 Author

**Mohammed Nihal**

Cybersecurity Student
