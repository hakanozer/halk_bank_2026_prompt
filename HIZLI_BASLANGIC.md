# 🚀 Hızlı Başlangıç Rehberi

## Proje Kurulumu ve Çalıştırma

### 📋 Ön Koşullar
- Python 3.8+
- pip (Python paket yöneticisi)

### 1️⃣ Adım 1: Kütüphaneleri Yükle

```bash
cd /Users/hakan/Documents/GitHub/halk_bank_2026_prompt
pip install -r requirements.txt
```

### 2️⃣ Adım 2: HTML Raporu Oluştur (Seçenek A)

HTML raporunu hemen oluşturmak için:

```bash
python generate_report.py
```

**Çıkış**:
```
✅ Rapor başarıyla oluşturuldu: /Users/hakan/Documents/GitHub/halk_bank_2026_prompt/report.html
📄 Tarayıcıda açmak için: open report.html
```

### 3️⃣ Adım 3: API Sunucusunu Başlat (Seçenek B)

FastAPI sunucusunu çalıştırmak için:

```bash
python main.py
```

**Çıkış**:
```
INFO:     Started server process [89124]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```

### 📂 Dosya Açıklama

| Dosya | Açıklama |
|-------|----------|
| `main.py` | FastAPI uygulaması ve API endpoints |
| `analysis.py` | Veri analiz mantığı ve tahminler |
| `report_generator.py` | HTML rapor oluşturucu |
| `generate_report.py` | Rapor üretim scripti |
| `report.html` | Oluşturulan HTML çıktısı |
| `requirements.txt` | Python bağımlılıkları |
| `siparisler_cleaned.csv` | Giriş verileri |

---

## 🌐 API Kullanım Örnekleri

FastAPI sunucusu çalışırken aşağıdaki API endpoints'lerini kullanabilirsiniz:

### 1. Ana Sayfa (HTML Raporu)
```bash
curl http://localhost:8000/
```

### 2. Özet İstatistikler
```bash
curl http://localhost:8000/api/summary
```

**Örnek Çıkış**:
```json
{
    "total_orders": 278,
    "total_customers": 5,
    "total_revenue": 3518340.78,
    "avg_order_value": 12655.90,
    "cities": 4,
    "categories": 3
}
```

### 3. En Çok Sipariş Verecek Müşteriler
```bash
curl http://localhost:8000/api/top-customers | python -m json.tool
```

### 4. Şehir Satış Tahmini
```bash
curl http://localhost:8000/api/city-prediction | python -m json.tool
```

### 5. Tekrar Satın Alma Analizi
```bash
curl http://localhost:8000/api/repeat-purchase | python -m json.tool
```

### 6. Kategori Analizi
```bash
curl http://localhost:8000/api/category-analysis | python -m json.tool
```

### 7. Sunucu Durum Kontrolü
```bash
curl http://localhost:8000/api/health
```

---

## 🎨 HTML Raporu Özelikleri

- **Responsive Tasarım**: Mobil, tablet ve masaüstü cihazlarda uyumlu
- **İnline Grafikler**: Tüm grafikler base64 formatında HTML içine gömülü
- **Profesyonel Tasarım**: Modern renkler ve yazı tipi
- **Türkçe Dil**: Tüm içerik Türkçe olarak hazırlanmıştır
- **Tarama Motoru Uyumlu**: Standar HTML 5 yapısı

---

## 📊 Tahminler ve Analiz

### Tahmin 1: En Çok Sipariş Verecek Müşteriler (30 Gün)
Geçmiş sipariş sıklığına dayanarak, müşterilerin sonraki 30 gün içinde kaç sipariş vereceği tahmin edilmiştir.

**Top 3 Müşteriler**:
1. Mehmet Demir - 6 sipariş
2. Fatma Şahin - 6 sipariş
3. Ahmet Yılmaz - 6 sipariş

### Tahmin 2: Şehir Satış Tahmini (30 Gün)
Her şehirdeki günlük harcama ortalaması hesaplanarak, 30 gün tahmini yapılmıştır.

**Top 1 Şehir**:
1. İstanbul - ₺117,457.40

### Tahmin 3: Tekrar Satın Alma Analizi
Müşterilerin bir kategoride birden fazla alışveriş yapma oranı analiz edilmiştir.

**Genel Repeat Rate**: 100%
- Tüm müşteriler en az 2 kez alışveriş yapmıştır

---

## 🛠️ Sorun Giderme

### Problem: "ModuleNotFoundError"
**Çözüm**: Kütüphaneleri yeniden yükleyin
```bash
pip install --upgrade -r requirements.txt
```

### Problem: Port 8000 zaten kullanımda
**Çözüm**: Farklı bir port kullanın
```bash
python main.py --port 8001
```

### Problem: Grafiklerde Türkçe karakterler gösterilmiyor
**Çözüm**: Font problemidir ancak HTML çıktısında sorun olmaz

---

## 📞 Proje Bilgileri

- **Proje Adı**: Halk Bank 2026 - Veri Analiz Sistemi
- **Versiyon**: 1.0.0
- **Teknolojiler**: Python, FastAPI, Pandas, Scikit-learn, Matplotlib, Seaborn
- **Lisans**: Proprietary

---

**Başarılı Çalıştırmaları Dilerim! 🎉**
