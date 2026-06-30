#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

# Read the existing HTML file
with open('report.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add Bootstrap script before </body>
bootstrap_script = '''    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>'''

content = content.replace('    </div>\n</body>\n</html>', bootstrap_script)

# Pattern for finding chart containers followed by tables
# This will find the first chart section (Tahmin 1)
pattern1 = r'(<div class="chart-container">\s*<img src="data:image/png;base64,[^"]*" alt="[^"]*">?\s*</div>)'

# Section 1 replacement
accordion1 = r'''<div class="accordion" id="accordion1">
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1" aria-expanded="false" aria-controls="collapse1">
                            📊 Grafik: En Çok Sipariş Verecek Müşteriler
                        </button>
                    </h2>
                    <div id="collapse1" class="accordion-collapse collapse" data-bs-parent="#accordion1">
                        <div class="accordion-body">
                            \1
                        </div>
                    </div>
                </div>
            </div>'''

# Replace first occurrence (Section 1)
content = re.sub(pattern1, accordion1, content, count=1)

# Section 2 - City chart - use a specific marker before it
pattern2_before = r'(<!-- TAHMIN 2: Şehir Satış Tahmini -->.*?<div class="prediction-box">.*?</div>)\s*(<div class="chart-container">\s*<img src="data:image/png;base64,[^"]*" alt="[^"]*">?\s*</div>)'

accordion2 = r'''\1
            
            <div class="accordion" id="accordion2">
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse2" aria-expanded="false" aria-controls="collapse2">
                            📊 Grafik: Şehir Bazında Satış Tahmini
                        </button>
                    </h2>
                    <div id="collapse2" class="accordion-collapse collapse" data-bs-parent="#accordion2">
                        <div class="accordion-body">
                            \2
                        </div>
                    </div>
                </div>
            </div>'''

content = re.sub(pattern2_before, accordion2, content, count=1, flags=re.DOTALL)

# Section 3 - Category chart
pattern3_before = r'(<!-- Kategori Analizi -->.*?<h2>📂 Kategori Analizi</h2>)\s*(<div class="chart-container">\s*<img src="data:image/png;base64,[^"]*" alt="[^"]*">?\s*</div>)'

accordion3 = r'''\1
            
            <div class="accordion" id="accordion3">
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse3" aria-expanded="false" aria-controls="collapse3">
                            📊 Grafik: Kategori Analizi
                        </button>
                    </h2>
                    <div id="collapse3" class="accordion-collapse collapse" data-bs-parent="#accordion3">
                        <div class="accordion-body">
                            \2
                        </div>
                    </div>
                </div>
            </div>'''

content = re.sub(pattern3_before, accordion3, content, count=1, flags=re.DOTALL)

# Write the updated HTML file
with open('report.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ HTML file updated successfully with Bootstrap accordions!")
print("   - Added Bootstrap CDN link")
print("   - Wrapped all charts in accordion sections")
print("   - Added Bootstrap JavaScript bundle")
