#!/usr/bin/env python3
"""Derive uz_UZ_2026 (new-alphabet) dictionary from uz_UZ.

Mechanical transliteration per the 2026 Uzbek Latin alphabet reform:
    Sh/sh -> Ş/ş   Ch/ch -> Ç/ç   Oʻ/oʻ -> Ö/ö   Gʻ/gʻ -> Ğ/ğ

Run from repo root: python3 scripts/convert_2026.py
"""
import re

SRC_AFF = "uz_UZ.aff"
SRC_DIC = "uz_UZ.dic"
OUT_AFF = "uz_UZ_2026.aff"
OUT_DIC = "uz_UZ_2026.dic"

_SH = re.compile("sh", re.IGNORECASE)
_CH = re.compile("ch", re.IGNORECASE)
_OA = re.compile("[oO]ʻ")
_GA = re.compile("[gG]ʻ")


def collapse(text: str) -> str:
    text = _SH.sub(lambda m: "Ş" if m.group(0)[0].isupper() else "ş", text)
    text = _CH.sub(lambda m: "Ç" if m.group(0)[0].isupper() else "ç", text)
    text = _OA.sub(lambda m: "Ö" if m.group(0)[0] == "O" else "ö", text)
    text = _GA.sub(lambda m: "Ğ" if m.group(0)[0] == "G" else "ğ", text)
    return text


NEW_TRY = "TRY - abcçdefgğhijklmnoöpqrsştuvwxyzABCÇDEFGĞHIJKLMNOÖPQRSŞTUVWXYZʼ\n"
NEW_WORDCHARS = "WORDCHARS -.'ʼ‘’\n"
NEW_REP = """REP 41
REP o' ö
REP O' Ö
REP g' ğ
REP G' Ğ
REP ' ʼ
REP ts s
REP s ts
REP x h
REP h x
REP o ö
REP O Ö
REP ö o
REP Ö O
REP u ö
REP U Ö
REP ö u
REP Ö U
REP g ğ
REP G Ğ
REP ğ g
REP Ğ G
REP iz ingiz
REP in ing
REP led layd
REP w ş
REP 4 ç
REP 6 ö
REP i e
REP e i
REP s z
REP a e
REP e ay
REP ug öğ
REP ux öh
REP x ks
REP sh ş
REP Sh Ş
REP SH Ş
REP ch ç
REP Ch Ç
REP CH Ç
"""


def convert_aff():
    with open(SRC_AFF, encoding="utf-8") as f:
        lines = f.readlines()

    out = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.rstrip("\n")

        if stripped.startswith("(c) 2019") or stripped.startswith("# (c) 2019"):
            out.append(line)
            i += 1
            continue

        if stripped.startswith("TRY "):
            out.append(NEW_TRY)
            i += 1
            continue

        if stripped.startswith("WORDCHARS "):
            out.append(NEW_WORDCHARS)
            i += 1
            continue

        if re.match(r"^REP \d+$", stripped):
            out.append(NEW_REP)
            i += 1
            while i < n and lines[i].startswith("REP "):
                i += 1
            continue

        if stripped.startswith("SFX ") or stripped.startswith("PFX "):
            parts = stripped.split()
            if len(parts) == 5 and len(parts[1]) == 1:
                kind, flag, strip, add, cond = parts
                add_body, sep, add_flags = add.partition("/")
                new_strip = collapse(strip)
                new_add_body = collapse(add_body)
                new_add = new_add_body + (sep + add_flags if sep else "")
                new_cond = collapse(cond)
                if new_cond == "[^kgqğ]":
                    new_cond = "[^kgqğö]"
                out.append(f"{kind} {flag} {new_strip} {new_add} {new_cond}\n")
                i += 1
                continue

        out.append(line)
        i += 1

    with open(OUT_AFF, "w", encoding="utf-8") as f:
        f.write("# Derived from uz_UZ.aff: mechanical transliteration to the\n")
        f.write("# 2026 Uzbek Latin alphabet (Sh->Ş, Ch->Ç, Oʻ->Ö, Gʻ->Ğ).\n")
        f.write("# See scripts/convert_2026.py.\n")
        f.writelines(out)


def convert_dic():
    with open(SRC_DIC, encoding="utf-8") as f:
        lines = f.readlines()

    out = [lines[0]]
    for line in lines[1:]:
        stripped = line.rstrip("\n")
        if not stripped:
            continue
        word, sep, flags = stripped.partition("/")
        new_word = collapse(word)
        out.append(new_word + (sep + flags if sep else "") + "\n")

    with open(OUT_DIC, "w", encoding="utf-8") as f:
        f.writelines(out)


if __name__ == "__main__":
    convert_aff()
    convert_dic()
    print("wrote", OUT_AFF, "and", OUT_DIC)
