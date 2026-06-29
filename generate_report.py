#!/usr/bin/env python3
"""
HTML raporu oluşturan script
"""
import os
from analysis import DataAnalyzer
from report_generator import HTMLReportGenerator

def main():
    # CSV dosya yolunu belirle
    csv_path = os.path.join(os.path.dirname(__file__), "siparisler_cleaned.csv")
    
    # Veri analiziricisini başlat
    print("📊 Veri yükleniyor...")
    analyzer = DataAnalyzer(csv_path)
    
    # Report generator oluştur
    print("📈 Rapor oluşturuluyor...")
    report_generator = HTMLReportGenerator(analyzer)
    
    # HTML raporu oluştur
    html_content = report_generator.generate_html_report()
    
    # HTML dosyasını kaydet
    output_path = os.path.join(os.path.dirname(__file__), "report.html")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Rapor başarıyla oluşturuldu: {output_path}")
    print(f"📄 Tarayıcıda açmak için: open {output_path}")

if __name__ == "__main__":
    main()
