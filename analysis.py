import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestClassifier
import io
import base64

class DataAnalyzer:
    def __init__(self, csv_path):
        self.df = pd.read_csv(csv_path)
        self.df['tarih'] = pd.to_datetime(self.df['tarih'], format='%d-%m-%Y %H:%M:%S')
        self.current_date = datetime(2026, 6, 29)
        
    def get_top_customers_next_30_days(self):
        """Sonraki 30 gün için en çok sipariş verecek müşterileri tahmin et"""
        customer_frequency = self.df.groupby('musteri_adi').agg({
            'siparis_id': 'count',
            'toplam_harcama': 'sum',
            'tarih': ['min', 'max']
        }).reset_index()
        
        customer_frequency.columns = ['musteri_adi', 'siparis_sayisi', 'toplam_harcama', 'ilk_tarih', 'son_tarih']
        
        # Sipariş sıklığını hesapla (kaç gün içinde kaç sipariş)
        customer_frequency['gun_farki'] = (customer_frequency['son_tarih'] - customer_frequency['ilk_tarih']).dt.days
        customer_frequency['gun_farki'] = customer_frequency['gun_farki'].replace(0, 1)
        customer_frequency['gunluk_siparis_orani'] = customer_frequency['siparis_sayisi'] / customer_frequency['gun_farki']
        
        # 30 gün için beklenen sipariş sayısı
        customer_frequency['tahmin_30gun'] = (customer_frequency['gunluk_siparis_orani'] * 30).round(0).astype(int)
        customer_frequency = customer_frequency.sort_values('tahmin_30gun', ascending=False)
        
        return customer_frequency[['musteri_adi', 'siparis_sayisi', 'tahmin_30gun', 'toplam_harcama']].head(10)
    
    def get_city_sales_prediction(self):
        """Şehir bazında satış tahmini"""
        city_stats = self.df.groupby('sehir').agg({
            'siparis_id': 'count',
            'toplam_harcama': 'sum',
            'tarih': ['min', 'max']
        }).reset_index()
        
        city_stats.columns = ['sehir', 'siparis_sayisi', 'toplam_harcama', 'ilk_tarih', 'son_tarih']
        city_stats['gun_farki'] = (city_stats['son_tarih'] - city_stats['ilk_tarih']).dt.days
        city_stats['gun_farki'] = city_stats['gun_farki'].replace(0, 1)
        city_stats['gunluk_harcama'] = city_stats['toplam_harcama'] / city_stats['gun_farki']
        city_stats['tahmin_30gun_harcama'] = (city_stats['gunluk_harcama'] * 30).round(2)
        
        return city_stats[['sehir', 'siparis_sayisi', 'tahmin_30gun_harcama']].sort_values('tahmin_30gun_harcama', ascending=False)
    
    def get_repeat_purchase_prediction(self):
        """Tekrar satın alma tahmini"""
        customer_purchases = self.df.groupby('musteri_adi').size().reset_index(name='purchase_count')
        repeat_rate = round(customer_purchases[customer_purchases['purchase_count'] > 1].shape[0] / customer_purchases.shape[0] * 100, 2)
        
        # Kategoriye göre repeat purchase
        category_repeat = self.df.groupby(['musteri_adi', 'kategori']).size().reset_index(name='count')
        category_repeat = category_repeat[category_repeat['count'] > 1].groupby('kategori').size().reset_index(name='repeat_count')
        
        category_purchase = self.df.groupby('kategori')['siparis_id'].count().reset_index(name='total_purchases')
        category_repeat = category_repeat.merge(category_purchase, on='kategori')
        category_repeat['repeat_rate'] = (category_repeat['repeat_count'] / category_repeat['total_purchases'] * 100).round(2)
        
        return {
            'overall_repeat_rate': repeat_rate,
            'by_category': category_repeat[['kategori', 'repeat_rate']].sort_values('repeat_rate', ascending=False)
        }
    
    def get_summary_statistics(self):
        """Özet istatistikler"""
        return {
            'total_orders': len(self.df),
            'total_customers': self.df['musteri_adi'].nunique(),
            'total_revenue': self.df['toplam_harcama'].sum(),
            'avg_order_value': self.df['toplam_harcama'].mean(),
            'cities': self.df['sehir'].nunique(),
            'categories': self.df['kategori'].nunique()
        }
    
    def get_category_analysis(self):
        """Kategori analizi"""
        category_stats = self.df.groupby('kategori').agg({
            'siparis_id': 'count',
            'toplam_harcama': 'sum',
            'adet': 'mean'
        }).reset_index()
        
        category_stats.columns = ['kategori', 'siparis_sayisi', 'toplam_harcama', 'ortalama_adet']
        category_stats['ortalama_harcama'] = (category_stats['toplam_harcama'] / category_stats['siparis_sayisi']).round(2)
        
        return category_stats.sort_values('toplam_harcama', ascending=False)
    
    def get_trending_customers_last_week(self):
        """Son bir hafta içinde trend müşterileri analiz et"""
        week_ago = self.current_date - timedelta(days=7)
        
        # Son bir haftanın verilerini filtrele
        last_week_df = self.df[self.df['tarih'] >= week_ago]
        
        # Müşteri başına istatistikler
        trending_customers = last_week_df.groupby('musteri_adi').agg({
            'siparis_id': 'count',
            'toplam_harcama': 'sum',
            'tarih': ['min', 'max']
        }).reset_index()
        
        trending_customers.columns = ['musteri_adi', 'siparis_sayisi', 'toplam_harcama', 'ilk_siparis', 'son_siparis']
        
        # Sipariş sıklığı ve harcama artışını hesapla
        trending_customers['ort_siparis_degeri'] = (trending_customers['toplam_harcama'] / trending_customers['siparis_sayisi']).round(2)
        trending_customers['trend_skoru'] = (trending_customers['siparis_sayisi'] * trending_customers['ort_siparis_degeri']).round(2)
        
        return trending_customers[['musteri_adi', 'siparis_sayisi', 'toplam_harcama', 'ort_siparis_degeri', 'trend_skoru']].sort_values('trend_skoru', ascending=False).head(10)

