#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sanayi ve Teknoloji Bakanlığı
Ketçap Viskozite ve Ani Fışkırma Denetim Müdürlüğü
Protokol No: ST-KETCAP-2026-09-03
"""

import argparse
import base64
import random
import sys
import time
from dataclasses import dataclass


# gizli mühür (base64) — bakma, resmi evrak değil
_MUHUR = "WWV0a2kgc2VmZmFmbGlrIGlzdGVyLCBndWMgZGVuZXRpbSBpc3Rlci4="


@dataclass
class KetcapOlayi:
    salla_sayisi: int
    sicaklik: float
    kapak_acikligi: float
    sabir: int


RAPORLAR = [
    "Şişe içinde milli viskozite birikimi tespit edildi.",
    "Kapak vanası Ar-Ge onayı bekliyor.",
    "Üretim hattında durgunluk; 'biraz sallarım gelir' dilekçesi işleme alındı.",
    "Masa yüzeyi resmi kaza mahalli ilan edildi.",
    "Ketçap artık bireysel tüketim maddesi değil, tesistir.",
]

SONUCLAR = [
    "DURUM: HİÇ ÇIKMADI. Şişe diplomatik dokunulmazlık kazandı.",
    "DURUM: TEK DAMLA. Komisyon bu damlayı 'pilot üretim' saydı.",
    "DURUM: ANİ FIŞKIRMA. Masa, önlük ve komşu tabak milli boya aldı.",
    "DURUM: ÖNCE YOK SONRA SEL. Protokol sapması tescillendi.",
    "DURUM: KAPAK UÇTU. Sanayi kazası raporu 14 nüsha basıldı.",
]


def _gizli():
    try:
        return base64.b64decode(_MUHUR).decode("utf-8")
    except Exception:
        return ""


def denetle(olay: KetcapOlayi) -> str:
    print("\n=== SANAYİ VE TEKNOLOJİ BAKANLIĞI ===")
    print("Ketçap Viskozite Denetim Müdürlüğü")
    print("Kayyum Grok resmi yazılımı çalışıyor...\n")
    time.sleep(0.4)

    skor = (
        olay.salla_sayisi * 1.7
        + (olay.sicaklik - 18) * 0.8
        + olay.kapak_acikligi * 11
        - olay.sabir * 0.9
        + random.uniform(-3, 9)
    )

    print(f"Sallama adedi     : {olay.salla_sayisi}")
    print(f"Şişe sıcaklığı    : {olay.sicaklik:.1f} °C")
    print(f"Kapak açıklığı    : {olay.kapak_acikligi:.2f} tur")
    print(f"Vatandaş sabrı    : {olay.sabir}/10")
    print(f"Viskozite skoru   : {skor:.2f}\n")

    for r in random.sample(RAPORLAR, k=3):
        print(" •", r)
        time.sleep(0.15)

    if skor < 4:
        sonuc = SONUCLAR[0]
    elif skor < 9:
        sonuc = SONUCLAR[1]
    elif skor < 16:
        sonuc = SONUCLAR[3]
    elif skor < 22:
        sonuc = SONUCLAR[2]
    else:
        sonuc = SONUCLAR[4]

    print("\n" + sonuc)
    print("Karar: Şişe resmi tesis, masa resmi kaza mahalli, sen resmi mağdursun.")
    return sonuc


def main():
    p = argparse.ArgumentParser(
        description="Ketçabın önce çıkmaması sonra fışkırmasını resmi sanayi olayı sayan yazılım."
    )
    p.add_argument("--salla", type=int, default=7, help="Şişeyi kaç kez salladın")
    p.add_argument("--sicaklik", type=float, default=21.0, help="Şişe sıcaklığı °C")
    p.add_argument("--kapak", type=float, default=0.35, help="Kapak kaç tur açıldı")
    p.add_argument("--sabir", type=int, default=4, help="Sabır 0-10")
    p.add_argument("--muhur", action="store_true", help=argparse.SUPPRESS)
    args = p.parse_args()

    if args.muhur:
        # bilinçli olarak sessiz; sadece meraklılara
        sys.stderr.write(_gizli() + "\n")
        return

    olay = KetcapOlayi(
        salla_sayisi=max(0, args.salla),
        sicaklik=args.sicaklik,
        kapak_acikligi=max(0.0, args.kapak),
        sabir=min(10, max(0, args.sabir)),
    )
    denetle(olay)
    print("\n---")
    print("Damga / İmza")
    print("Kayyum Grok  ·  Tentivory  ·  3 Eylül 2026")
    print("Ciddi resmi evrak değildir. Ciddi resmi evrak gibidir.")
    print("Eskişehir 4. Ağır Ceza Mahkemesi kayyum mührüyle tasdiklidir (espri).")


if __name__ == "__main__":
    main()
