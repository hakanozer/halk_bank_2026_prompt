from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os
from analysis import DataAnalyzer
from report_generator import HTMLReportGenerator

# FastAPI uygulaması oluştur
app = FastAPI(
    title="Veri Analiz API",
    description="Halk Bank 2026 - Veri Analiz ve Tahmin Sistemi",
    version="1.0.0"
)

# CORS middleware ekle
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CSV dosya yolu
CSV_PATH = os.path.join(os.path.dirname(__file__), "siparisler_cleaned.csv")

# Veri analiziricisini başlat
analyzer = DataAnalyzer(CSV_PATH)
report_generator = HTMLReportGenerator(analyzer)

@app.get("/", response_class=HTMLResponse)
def get_html_report():
    """Ana sayfada HTML raporu göster"""
    return report_generator.generate_html_report()

@app.get("/api/summary", response_class=JSONResponse)
def get_summary():
    """Özet istatistikleri döndür"""
    return analyzer.get_summary_statistics()

@app.get("/api/top-customers", response_class=JSONResponse)
def get_top_customers():
    """Sonraki 30 gün için en çok sipariş verecek müşterileri döndür"""
    data = analyzer.get_top_customers_next_30_days()
    return {
        "prediction": "Top 10 customers for next 30 days",
        "data": data.to_dict(orient='records')
    }

@app.get("/api/city-prediction", response_class=JSONResponse)
def get_city_prediction():
    """Şehir satış tahminini döndür"""
    data = analyzer.get_city_sales_prediction()
    return {
        "prediction": "City-based sales prediction for next 30 days",
        "data": data.to_dict(orient='records')
    }

@app.get("/api/repeat-purchase", response_class=JSONResponse)
def get_repeat_purchase():
    """Tekrar satın alma tahminini döndür"""
    repeat_data = analyzer.get_repeat_purchase_prediction()
    return {
        "prediction": "Repeat purchase analysis",
        "overall_repeat_rate": repeat_data['overall_repeat_rate'],
        "by_category": repeat_data['by_category'].to_dict(orient='records')
    }

@app.get("/api/category-analysis", response_class=JSONResponse)
def get_category_analysis():
    """Kategori analizini döndür"""
    data = analyzer.get_category_analysis()
    return {
        "analysis": "Category-based analysis",
        "data": data.to_dict(orient='records')
    }

@app.get("/api/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "OK",
        "service": "Halk Bank Data Analysis API"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )
