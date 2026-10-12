import re

print("=" * 45)
print("          PHISHING URL DETECTOR")
print("=" * 45)

url = input("Enter URL: ").strip()

print("\n[+] Analyzing URL...")
print("-" * 45)

score = 0
reasons = []

# Suspicious words
suspicious_words = [
    "login",
    "verify",
    "account",
    "update",
    "secure",
    "bank",
    "password"
]

for word in suspicious_words:
    if word in url.lower():
        score += 1
        reasons.append("Suspicious word found: " + word)

# IP address detection
ip_pattern = r"https?://\d+\.\d+\.\d+\.\d+"

if re.search(ip_pattern, url):
    score += 2
    reasons.append("URL uses an IP address")

# @ symbol detection
if "@" in url:
    score += 2
    reasons.append("URL contains @ symbol")

# Hyphen detection
if url.count("-") >= 3:
    score += 1
    reasons.append("Too many '-' characters")

# URL length
if len(url) > 75:
    score += 1
    reasons.append("URL is unusually long")

# HTTPS check
if not url.lower().startswith("https://"):
    score += 1
    reasons.append("URL does not use HTTPS")

# Final risk level
if score >= 5:
    risk = "HIGH RISK"
elif score >= 2:
    risk = "MEDIUM RISK"
else:
    risk = "LOW RISK"

print("URL        :", url)
print("Risk Score :", score)
print("Risk Level :", risk)

print("\nReasons:")

if reasons:
    for reason in reasons:
        print(" -", reason)
else:
    print(" - No suspicious indicators detected")

print("-" * 45)
print("Analysis completed.")
print("=" * 45)
