import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
from datetime import datetime

class HTMLReportGenerator:
    def __init__(self, analyzer):
        self.analyzer = analyzer
        self.sns_style = sns.set_style("whitegrid")
        
    def fig_to_base64(self, fig):
        """Matplotlib figürünü base64 string'e dönüştür"""
        buffer = io.BytesIO()
        fig.savefig(buffer, format='png', dpi=100, bbox_inches='tight')
        buffer.seek(0)
        image_base64 = base64.b64encode(buffer.read()).decode()
        plt.close(fig)
        return image_base64
    
    def generate_top_customers_chart(self):
        """En çok sipariş verecek müşteriler grafiği"""
        data = self.analyzer.get_top_customers_next_30_days()
        
        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.barh(data['musteri_adi'], data['tahmin_30gun'], color='steelblue')
        
        ax.set_xlabel('Tahmin Edilen Sipariş Sayısı (30 gün)', fontsize=12, fontweight='bold')
        ax.set_ylabel('Müşteri Adı', fontsize=12, fontweight='bold')
        ax.set_title('Sonraki 30 Gün İçin En Çok Sipariş Verecek Müşteriler', fontsize=14, fontweight='bold')
        
        # Değerleri göster
        for i, (idx, row) in enumerate(data.iterrows()):
            ax.text(row['tahmin_30gun'] + 0.1, i, str(int(row['tahmin_30gun'])), 
                   va='center', fontsize=10)
        
        plt.tight_layout()
        return self.fig_to_base64(fig)
    
    def generate_city_sales_chart(self):
        """Şehir satış tahmini grafiği"""
        data = self.analyzer.get_city_sales_prediction()
        
        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.bar(data['sehir'], data['tahmin_30gun_harcama'], color='coral')
        
        ax.set_xlabel('Şehir', fontsize=12, fontweight='bold')
        ax.set_ylabel('Tahmin Edilen Harcama (₺)', fontsize=12, fontweight='bold')
        ax.set_title('Şehir Bazında Satış Tahmini (Sonraki 30 Gün)', fontsize=14, fontweight='bold')
        
        # Değerleri göster
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'₺{height:,.0f}',
                   ha='center', va='bottom', fontsize=10)
        
        plt.xticks(rotation=45)
        plt.tight_layout()
        return self.fig_to_base64(fig)
    
    def generate_category_chart(self):
        """Kategori analizi grafiği"""
        data = self.analyzer.get_category_analysis()
        
        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.bar(data['kategori'], data['toplam_harcama'], color='lightgreen')
        
        ax.set_xlabel('Kategori', fontsize=12, fontweight='bold')
        ax.set_ylabel('Toplam Harcama (₺)', fontsize=12, fontweight='bold')
        ax.set_title('Kategori Bazında Toplam Harcama', fontsize=14, fontweight='bold')
        
        # Değerleri göster
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'₺{height:,.0f}',
                   ha='center', va='bottom', fontsize=10)
        
        plt.xticks(rotation=45)
        plt.tight_layout()
        return self.fig_to_base64(fig)
    
    def generate_html_report(self):
        """Tam HTML raporu oluştur"""
        # İstatistikler
        stats = self.analyzer.get_summary_statistics()
        top_customers = self.analyzer.get_top_customers_next_30_days()
        city_prediction = self.analyzer.get_city_sales_prediction()
        repeat_purchase = self.analyzer.get_repeat_purchase_prediction()
        category_data = self.analyzer.get_category_analysis()
        
        # Grafikler
        customers_chart = self.generate_top_customers_chart()
        city_chart = self.generate_city_sales_chart()
        category_chart = self.generate_category_chart()
        
        html_content = f"""
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Veri Analiz Raporu</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: #333;
            line-height: 1.6;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        header {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin-bottom: 30px;
            text-align: center;
        }}
        
        header h1 {{
            color: #667eea;
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        
        header p {{
            color: #666;
            font-size: 1.1em;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .stat-card {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            text-align: center;
            border-left: 4px solid #667eea;
        }}
        
        .stat-card h3 {{
            color: #667eea;
            font-size: 0.9em;
            text-transform: uppercase;
            margin-bottom: 10px;
            letter-spacing: 1px;
        }}
        
        .stat-card .value {{
            font-size: 2em;
            font-weight: bold;
            color: #333;
        }}
        
        .section {{
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            margin-bottom: 30px;
        }}
        
        .section h2 {{
            color: #667eea;
            font-size: 1.8em;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #667eea;
        }}
        
        .prediction-box {{
            background: #f0f4ff;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 4px solid #764ba2;
        }}
        
        .prediction-box h3 {{
            color: #764ba2;
            margin-bottom: 15px;
            font-size: 1.2em;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        
        table thead {{
            background: #667eea;
            color: white;
        }}
        
        table th {{
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}
        
        table td {{
            padding: 12px 15px;
            border-bottom: 1px solid #ddd;
        }}
        
        table tbody tr:hover {{
            background: #f5f5f5;
        }}
        
        .chart-container {{
            text-align: center;
            margin: 30px 0;
        }}
        
        .chart-container img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        }}
        
        .highlight {{
            background: #fff3cd;
            padding: 15px;
            border-radius: 8px;
            margin: 15px 0;
            border-left: 4px solid #ffc107;
        }}
        
        .repeat-rate {{
            font-size: 2em;
            font-weight: bold;
            color: #764ba2;
            margin: 20px 0;
        }}
        
        footer {{
            text-align: center;
            color: white;
            padding: 20px;
            margin-top: 30px;
        }}
        
        @media (max-width: 768px) {{
            header h1 {{
                font-size: 1.8em;
            }}
            
            .section {{
                padding: 15px;
            }}
            
            table {{
                font-size: 0.9em;
            }}
            
            table th, table td {{
                padding: 8px;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📊 Veri Analiz Raporu</h1>
            <p>Halk Bank 2026 - Detaylı Analiz ve Tahminler</p>
            <p style="font-size: 0.9em; margin-top: 10px;">Rapor Tarihi: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}</p>
        </header>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h3>Toplam Siparişler</h3>
                <div class="value">{stats['total_orders']:,}</div>
            </div>
            <div class="stat-card">
                <h3>Toplam Müşteriler</h3>
                <div class="value">{stats['total_customers']}</div>
            </div>
            <div class="stat-card">
                <h3>Toplam Gelir</h3>
                <div class="value">₺{stats['total_revenue']:,.0f}</div>
            </div>
            <div class="stat-card">
                <h3>Ort. Sipariş Değeri</h3>
                <div class="value">₺{stats['avg_order_value']:,.0f}</div>
            </div>
        </div>
        
        <!-- TAHMIN 1: En Çok Sipariş Verecek Müşteriler -->
        <section class="section">
            <h2>🎯 Tahmin 1: Sonraki 30 Gün İçin En Çok Sipariş Verecek Müşteriler</h2>
            
            <div class="prediction-box">
                <h3>Analiz Yöntemi</h3>
                <p>Geçmiş sipariş verileri analiz edilerek, her müşterinin günlük sipariş sıklığı hesaplanmıştır. 
                Bu oran kullanılarak, sonraki 30 gün içinde beklenen sipariş sayısı tahmin edilmiştir.</p>
            </div>
            
            <div class="chart-container">
                <img src="data:image/png;base64,{customers_chart}" alt="En Çok Sipariş Verecek Müşteriler">
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>Müşteri Adı</th>
                        <th>Geçmiş Sipariş Sayısı</th>
                        <th>30 Gün Tahmini</th>
                        <th>Toplam Harcama</th>
                    </tr>
                </thead>
                <tbody>
"""
        
        for _, row in top_customers.iterrows():
            html_content += f"""
                    <tr>
                        <td><strong>{row['musteri_adi']}</strong></td>
                        <td>{int(row['siparis_sayisi'])}</td>
                        <td>{int(row['tahmin_30gun'])}</td>
                        <td>₺{row['toplam_harcama']:,.2f}</td>
                    </tr>
"""
        
        html_content += """
                </tbody>
            </table>
        </section>
        
        <!-- TAHMIN 2: Şehir Satış Tahmini -->
        <section class="section">
            <h2>🏙️ Tahmin 2: Şehir Bazında Satış Tahmini (30 Gün)</h2>
            
            <div class="prediction-box">
                <h3>Analiz Yöntemi</h3>
                <p>Her şehirde gerçekleşen harcamalar zaman serisine göre analiz edilerek, 
                günlük ortalama harcama hesaplanmıştır. Bu veriye dayanarak, sonraki 30 gün içinde 
                beklenen toplam harcama tahmin edilmiştir.</p>
            </div>
            
            <div class="chart-container">
                <img src="data:image/png;base64,{city_chart}" alt="Şehir Bazında Satış Tahmini">
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>Şehir</th>
                        <th>Geçmiş Sipariş Sayısı</th>
                        <th>30 Gün Satış Tahmini (₺)</th>
                    </tr>
                </thead>
                <tbody>
"""
        
        for _, row in city_prediction.iterrows():
            html_content += f"""
                    <tr>
                        <td><strong>{row['sehir']}</strong></td>
                        <td>{int(row['siparis_sayisi'])}</td>
                        <td>₺{row['tahmin_30gun_harcama']:,.2f}</td>
                    </tr>
"""
        
        html_content += """
                </tbody>
            </table>
        </section>
        
        <!-- TAHMIN 3: Tekrar Satın Alma Analizi -->
        <section class="section">
            <h2>🔄 Tahmin 3: Tekrar Satın Alma (Repeat Purchase) Analizi</h2>
            
            <div class="prediction-box">
                <h3>Analiz Yöntemi</h3>
                <p>Geçmiş veriler incelenererek, müşterilerin ne kadarının birden fazla alışveriş yaptığı 
                ve hangi kategorilerde repeat purchase oranının yüksek olduğu belirlenmiştir.</p>
            </div>
            
            <div class="highlight">
                <strong>📈 Genel Tekrar Satın Alma Oranı:</strong>
                <div class="repeat-rate">{repeat_purchase['overall_repeat_rate']}%</div>
                <p>Müşterilerin <strong>{repeat_purchase['overall_repeat_rate']}%</strong>'i birden fazla alışveriş yapmıştır.</p>
            </div>
            
            <h3 style="margin-top: 30px; color: #667eea;">Kategoriye Göre Tekrar Satın Alma Oranları</h3>
            <table>
                <thead>
                    <tr>
                        <th>Kategori</th>
                        <th>Tekrar Satın Alma Oranı (%)</th>
                    </tr>
                </thead>
                <tbody>
"""
        
        for _, row in repeat_purchase['by_category'].iterrows():
            html_content += f"""
                    <tr>
                        <td><strong>{row['kategori']}</strong></td>
                        <td>{row['repeat_rate']:.2f}%</td>
                    </tr>
"""
        
        html_content += """
                </tbody>
            </table>
        </section>
        
        <!-- Kategori Analizi -->
        <section class="section">
            <h2>📂 Kategori Analizi</h2>
            
            <div class="chart-container">
                <img src="data:image/png;base64,""" + category_chart + """" alt="Kategori Analizi">
            </div>
            
            <table>
                <thead>
                    <tr>
                        <th>Kategori</th>
                        <th>Sipariş Sayısı</th>
                        <th>Toplam Harcama</th>
                        <th>Ort. Harcama</th>
                    </tr>
                </thead>
                <tbody>
"""
        
        for _, row in category_data.iterrows():
            html_content += f"""
                    <tr>
                        <td><strong>{row['kategori']}</strong></td>
                        <td>{int(row['siparis_sayisi'])}</td>
                        <td>₺{row['toplam_harcama']:,.2f}</td>
                        <td>₺{row['ortalama_harcama']:,.2f}</td>
                    </tr>
"""
        
        html_content += """
                </tbody>
            </table>
        </section>
        
        <footer>
            <p>Bu rapor otomatik olarak üretilmiştir. Tüm tahminler geçmiş veriler ve istatistiksel analize dayanmaktadır.</p>
            <p>&copy; 2026 Halk Bank - Veri Analiz Sistemi</p>
        </footer>
    </div>
</body>
</html>
"""
        
        return html_content
