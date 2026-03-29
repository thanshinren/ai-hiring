SKILL_DICTIONARY = {
    "tools": {
        "siem": ["siem", "splunk", "qradar", "sentinel", "logrhythm"],
        "edr": ["edr", "crowdstrike", "defender", "carbon black"],
        "soar": ["soar", "cortex xsoar", "splunk soar"],
        "vulnerability_scanners": ["nessus", "qualys", "rapid7"],
        "forensics": ["encase", "ftk", "autopsy"],
        "cloud": ["aws", "azure", "gcp"],
    },

    "frameworks": {
        "mitre_attack": ["mitre", "mitre attack"],
        "nist": ["nist", "nist rmf"],
        "iso_27001": ["iso 27001"],
        "kill_chain": ["kill chain"],
        "zero_trust": ["zero trust", "ztna"],
    },

    "networking": {
        "protocols": ["tcp/ip", "dns", "http", "vpn"],
        "security_devices": ["firewall", "ids", "ips"],
    },

    "programming": {
        "languages": ["python", "powershell", "bash", "kql", "spl"],
    },

    "certifications": {
        "security_plus": ["security+", "sec+"],
        "cysa": ["cysa+", "cysa"],
        "ceh": ["ceh"],
        "cissp": ["cissp"],
        "gcfa": ["gcfa"],
        "gcih": ["gcih"],
    }
}
