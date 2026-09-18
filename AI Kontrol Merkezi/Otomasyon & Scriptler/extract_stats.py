#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, re, csv, json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
VAULT_DIR = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
DATA_DIR = os.path.join(VAULT_DIR, "Files")
CSV_FILE = os.path.join(DATA_DIR, "meta_analysis_matrix.csv")

CSV_HEADERS = [
    "DOI",
    "Study_Year",
    "First_Author",
    "Study_Type",
    "Sample_Size_Intervention",
    "Sample_Size_Control",
    "Mean_Change",
    "SD_Change",
    "Effect_Size",
    "P_Value",
    "Evidence_Direction",
    "Primary_Outcome"
]

def init_csv():
    os.makedirs(DATA_DIR, exist_ok=True)
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(CSV_HEADERS)
        print(f"[+] {CSV_FILE} olusturuldu.")

def extract_numeric_parameters(text):
    data = {
        "DOI": "",
        "Study_Year": "",
        "First_Author": "",
        "Study_Type": "RCT",
        "Sample_Size_Intervention": "",
        "Sample_Size_Control": "",
        "Mean_Change": "",
        "SD_Change": "",
        "Effect_Size": "",
        "P_Value": "",
        "Evidence_Direction": "inconclusive",
        "Primary_Outcome": ""
    }
    doi_match = re.search(r"(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)", text)
    if doi_match:
        data["DOI"] = doi_match.group(1).rstrip(".")

    year_match = re.search(r"\b(19\d\d|20\d\d)\b", text)
    if year_match:
        data["Study_Year"] = year_match.group(1)

    n_match = re.search(r"\b(?:n|N)\s*=\s*(\d+)", text)
    if n_match:
        data["Sample_Size_Intervention"] = n_match.group(1)

    p_match = re.search(r"\b[pP]\s*([<=><])\s*([01]?\.?\d+)", text)
    if p_match:
        data["P_Value"] = f"p {p_match.group(1)} {p_match.group(2)}"
        try:
            val = float(p_match.group(2))
            if p_match.group(1) == "<" or val < 0.05:
                data["Evidence_Direction"] = "positive"
            elif val >= 0.05:
                data["Evidence_Direction"] = "null"
        except Exception:
            pass

    eff_match = re.search(r"\b(MD|SMD|OR|HR|RR)\s*[:=]\s*([-\d\.]+)", text, re.IGNORECASE)
    if eff_match:
        data["Effect_Size"] = f"{eff_match.group(1).upper()} = {eff_match.group(2)}"

    return data

def append_to_matrix(data_dict):
    init_csv()
    doi = data_dict.get("DOI", "").strip()
    if doi:
        try:
            with open(CSV_FILE, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if row.get("DOI") == doi:
                        print(f"[-] DOI {doi} zaten matriste mevcut, atlandi.")
                        return False
        except Exception:
            pass

    row = [data_dict.get(h, "") for h in CSV_HEADERS]
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(row)
    print(f"[+] Matrise yeni veri eklendi: {data_dict.get('DOI') or data_dict.get('First_Author', 'Kayit')}")
    return True

if __name__ == "__main__":
    init_csv()
    if len(sys.argv) > 1:
        input_text = " ".join(sys.argv[1:])
        extracted = extract_numeric_parameters(input_text)
        append_to_matrix(extracted)
    else:
        print("Kullanim: python3 extract_stats.py \"Makale metni veya abstract...\"")
