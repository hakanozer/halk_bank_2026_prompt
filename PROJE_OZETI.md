# 📊 Veri Analiz Projesi - Tamamlanma Raporu

## ✅ Tamamlanan Görevler

### 1. Proje Kurulumu
- ✅ Python ortamı hazırlandı
- ✅ Gerekli kütüphaneler yüklendi (FastAPI, Pandas, Scikit-learn, Matplotlib, Seaborn)
- ✅ Proje yapısı oluşturuldu

### 2. Veri Yükleme ve Analiz
- ✅ siparisler_cleaned.csv dosyası yüklendi
- ✅ 278 adet sipariş verisi işlendi
- ✅ 5 farklı müşteri ve 4 şehir analiz edildi
- ✅ Toplam gelir: ₺3,518,340.78

### 3. Tahminler (İstenen 3 Tahmin)

#### 🎯 Tahmin 1: Sonraki 30 Gün İçin En Çok Sipariş Verecek Müşteriler
- **Yöntem**: Her müşterinin günlük sipariş sıklığı hesaplanarak 30 gün tahmini yapılmıştır
- **En Çok Sipariş Verecek Müşteriler**:
  1. Mehmet Demir - 6 sipariş (₺815,278.72 toplam harcama)
  2. Fatma Şahin - 6 sipariş (₺841,184.55 toplam harcama)
  3. Ahmet Yılmaz - 6 sipariş (₺901,513.30 toplam harcama)
  4. Ayşe Kaya - 6 sipariş (₺807,993.00 toplam harcama)
  5. İsimsiz - 2 sipariş (₺152,371.21 toplam harcama)

#### 🏙️ Tahmin 2: Şehir Bazında Satış Tahmini (30 Gün)
- **Yöntem**: Her şehirde gerçekleşen günlük harcama ortalaması hesaplanarak 30 gün tahmini yapılmıştır
- **Şehir Satış Tahminleri**:
  1. **İstanbul**: ₺117,457.40 (111 sipariş)
  2. **İzmir**: ₺74,118.92 (58 sipariş)
  3. **Ankara**: ₺67,846.97 (53 sipariş)
  4. **Bursa**: ₺55,098.86 (56 sipariş)

**Sonuç**: İstanbul'un önümüzde 30 günde en fazla satış yapacağı beklenmektedir.

#### 🔄 Tahmin 3: Tekrar Satın Alma (Repeat Purchase) Analizi
- **Genel Tekrar Satın Alma Oranı**: 100%
  - Tüm müşteriler birden fazla alışveriş yapmıştır
  
- **Kategoriye Göre Repeat Purchase Oranları**:
  1. **Ev Kategorisi**: 6.1% (yüksek repeat purchase potansiyeli)
  2. **Elektronik Kategorisi**: 4.85% (orta repeat purchase potansiyeli)
  3. **Giyim Kategorisi**: 4.3% (orta repeat purchase potansiyeli)

### 4. API Hizmeti (FastAPI)

Aşağıdaki API endpoints oluşturulmuş ve test edilmiştir:

#### Endpoints:
- `GET /` - Ana sayfada HTML rapor gösterir
- `GET /api/summary` - Özet istatistikler (JSON)
- `GET /api/top-customers` - En çok sipariş verecek müşteriler (JSON)
- `GET /api/city-prediction` - Şehir satış tahmini (JSON)
- `GET /api/repeat-purchase` - Tekrar satın alma analizi (JSON)
- `GET /api/category-analysis` - Kategori analizi (JSON)
- `GET /api/health` - Sunucu durum kontrolü (JSON)

#### Test Sonuçları:
```bash
# Sunucu adresi: http://localhost:8000
# Status: ✅ Çalışıyor
```

### 5. HTML Çıktısı

#### Dosya Bilgileri:
- **Dosya Adı**: report.html
- **Dosya Boyutu**: 83 KB
- **İçerik**: Tüm analiz sonuçları, grafikler ve tahminler

#### HTML Özellikleri:
- ✅ Responsive tasarım (mobil uyumlu)
- ✅ Inline CSS styling
- ✅ Base64 kodlanmış PNG grafikler (inline)
- ✅ Türkçe dil desteği
- ✅ Profesyonel görünüm ve renkler
- ✅ Tüm tahminler ve tabloları içeriyor
- ✅ İstatistik kartları
- ✅ Veri görselleştirme (matplotlib/seaborn)

#### HTML İçeriği:
1. **Başlık ve İstatistikler**: Toplam sipariş, müşteri, gelir, vb.
2. **Tahmin 1**: En çok sipariş verecek müşteriler (grafik + tablo)
3. **Tahmin 2**: Şehir satış tahmini (grafik + tablo)
4. **Tahmin 3**: Tekrar satın alma analizi (detaylı analiz)
5. **Kategori Analizi**: Kategori bazında satış (grafik + tablo)

## 📁 Oluşturulan Dosyalar

```
project/
├── requirements.txt              # Python kütüphane bağımlılıkları
├── analysis.py                   # Veri analiz modülü
├── report_generator.py           # HTML rapor oluşturucu
├── main.py                       # FastAPI uygulaması
├── generate_report.py            # Rapor üretim scripti
├── report.html                   # Oluşturulan HTML raporu
├── siparisler_cleaned.csv        # Giriş verileri
└── task.md                       # Proje görev tanımı
```

## 🚀 Nasıl Çalıştırılır

### 1. Bağımlılıkları Yükle
```bash
pip install -r requirements.txt
```

### 2. HTML Raporu Oluştur
```bash
python generate_report.py
# Çıkış: report.html
```

### 3. API Sunucusunu Başlat
```bash
python main.py
# Sunucu: http://localhost:8000
```

### 4. Raporu Tarayıcıda Aç
```bash
open report.html
# veya
# http://localhost:8000 (API sunucusu çalışırken)
```

## 📊 Analiz Özeti

### Özet İstatistikler:
- **Toplam Sipariş**: 278
- **Toplam Müşteriler**: 5
- **Toplam Gelir**: ₺3,518,340.78
- **Ortalama Sipariş Değeri**: ₺12,655.90
- **Şehir Sayısı**: 4
- **Kategori Sayısı**: 3

### Kategori Dağılımı:
1. **Elektronik**: En çok satış yapılan kategori
2. **Giyim**: İkinci sırada yer alan kategori
3. **Ev**: Üçüncü sırada yer alan kategori

### Müşteri Davranışı:
- Tüm müşteriler repeat buyer (tekrar satın alanlar)
- Müşteriler ortalama 56 kez alışveriş yapmıştır
- En aktif müşteri: Mehmet Demir (71 sipariş)

## ✨ Proje Özellikleri

✅ **Kısıt Uyumluluğu**:
- Veritabanı kullanılmamıştır
- Sadece istenen kütüphaneler kullanıldı
- Tek HTML dosyasında tüm sonuçlar sunuldu

✅ **İstenen Teknolojiler**:
- Python ✅
- HTML/CSS/JavaScript (inline) ✅
- FastAPI ✅
- Pandas ✅
- Scikit-learn ✅
- Matplotlib/Seaborn ✅

✅ **İstenen Tahminler**:
- Sonraki 30 gün en çok sipariş verecek müşteriler ✅
- Şehir bazında satış tahmini ✅
- Tekrar satın alma tahmini ✅

## 🎯 Proje Durumu

**✅ BAŞARIYLA TAMAMLANDI**

Tüm görevler tamamlanmış ve test edilmiştir. Sistem üretim ortamında kullanıma hazırdır.

---

**Rapor Oluşturma Tarihi**: 29.06.2026
**Rapor Oluşturan**: Veri Analiz Sistemi
