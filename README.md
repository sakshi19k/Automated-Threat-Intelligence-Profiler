# Automated Cyber Threat Intelligence Profiler

An automated, Python-based Cyber Threat Intelligence (CTI) tool designed to ingest Indicators of Compromise (IOCs), enrich them using open-source intelligence (OSINT), and map advanced threat actor behaviors to the industry-standard MITRE ATT&CK framework.

This project bridges the gap between raw technical logging data and actionable, strategic threat profiling—a core operational workflow for Security Operations Center (SOC) and Threat Intelligence analysts.



## 🚀 Features

* **Automated OSINT Enrichment:** Interrogates external threat databases using secure API integrations to dynamically fetch live security vendor reputation scores.
* **Triage Optimization:** Automatically parses complex nested JSON payloads to instantly highlight malicious and suspicious risk flags.
* **Strategic Threat Mapping:** Contextualizes technical indicators (IPs/domains) by linking malicious activity back to the historical Tactics, Techniques, and Procedures (TTPs) of specific Advanced Persistent Threats (APTs), such as APT29 (Cozy Bear).



## 🛠️ Tech Stack & Concepts

* **Language:** Python 3
* **Libraries:** `requests`, `json`
* **API Integrations:** VirusTotal API, AlienVault OTX
* **Frameworks:** MITRE ATT&CK Framework, Threat Intelligence Lifecycle



## 📋 How It Works: The CTI Loop

1. **Collection:** The script accepts a public network indicator (IPv4 address) flagged during daily security operations or pulled from active threat feeds.
2. **Analysis & Enrichment:** The script securely queries OSINT aggregators to check how global security engines classify the indicator.
3. **Strategic Profiling:** The discovered malware infrastructure is analyzed alongside known threat groups using the MITRE ATT&CK Matrix to understand the attacker's ultimate objectives.



## 💻 Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/sakshi19k/Automated-Threat-Intelligence-Profiler.git](https://github.com/sakshi19k/Automated-Threat-Intelligence-Profiler.git)
cd Automated-Threat-Intelligence-Profiler
