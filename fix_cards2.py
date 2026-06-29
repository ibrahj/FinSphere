import re

with open('/Users/Ibrahim/Desktop/finsphere/index.html','r') as f:
    c = f.read()

cards = [
    ('hamat_group.png', 'HAMAT Group', 'مجموعة هامات', 'خدمات المرافق', 'Facilities Services',
     'استشارات جاهزية رأس المال ومراجعة القوائم المالية لدعم التموضع الاستراتيجي للنمو',
     'Capital readiness advisory and financial statements review to support strategic growth positioning'),
    ('rwashin.png', 'Rwashin Compounds', 'رواشين', 'تطوير سكني', 'Real Estate',
     'بحث السوق وتحليل المشهد التنافسي لدعم قرارات الاستثمار والتطوير',
     'Market research and competitive landscape analysis to inform investment and development decisions'),
    ('nabed.png', 'NABED', 'نبض', 'رعاية صحية رقمية', 'Digital Healthcare',
     'إعادة هيكلة الأعمال وتطوير الاستراتيجية المؤسسية والتخطيط المالي',
     'Business restructuring, corporate strategy development, and financial planning advisory'),
    ('cfg.png', 'CFG Environment', 'CFG للبيئة', 'بيئة وطاقة', 'Environment and Energy',
     'بحث دخول السوق واستراتيجية إدارة الأداء',
     'Market entry research and performance management strategy'),
    ('wisework.png', 'WiseWork', 'وايز ورك', 'تقنية الأعمال', 'Business Technology',
     'استشارات جاهزية رأس المال والاستراتيجية المؤسسية وإطار إدارة أصحاب المصلحة',
     'Capital readiness advisory, corporate strategy, and stakeholder engagement framework'),
    ('idv.png', 'IDV', 'IDV', 'استثمار وتقنية', 'Venture Studio and Tech',
     'استراتيجية إدارة الأداء وإعادة هيكلة الأعمال والاستشارات المالية',
     'Performance management strategy, business restructuring, and financial advisory'),
    ('samatwaiq.png', 'SAMA TWAIQ', 'سما طويق', 'تقنية الطائرات المسيرة', 'Drone Technology',
     'استراتيجية إدارة الأداء وإعادة هيكلة الأعمال والاستشارات المالية',
     'Performance management strategy, business restructuring, and financial advisory'),
    ('invdro.png', 'Invdro', 'انفدرو', 'تقنية الطائرات المسيرة', 'Drone Technology',
     'استراتيجية إدارة الأداء وإعادة هيكلة الأعمال والاستشارات المالية',
     'Performance management strategy, business restructuring, and financial advisory'),
    ('hamat_academy.png', 'HAMAT Academy', 'أكاديمية هامات', 'تعليم وتدريب', 'Education and Training',
     'تطوير الاستراتيجية المؤسسية وتخطيط النمو المؤسسي',
     'Corporate strategy development and institutional growth planning'),
    ('baljurashi.png', 'Baljurashi Boulevard', 'جادة بلجرشي', 'تطوير عقاري وسياحي', 'Real Estate and Tourism',
     'بحث السوق واستشارات جاهزية رأس المال لدعم التموضع الاستثماري للمشروع',
     'Market research and capital readiness advisory to support project investment positioning'),
    ('sju.png', 'Saudi Journalists Association', 'هيئة الصحفيين السعوديين', 'إعلام وصحافة', 'Media and Journalism',
     'الاستشارات المالية وإعادة هيكلة الأعمال والتخطيط المالي',
     'Financial advisory, business restructuring, and financial planning'),
    ('ascor.png', 'Ascor Co.', 'أسكور', 'استثمار وأعمال', 'Investment and Business',
     'استشارات استراتيجية ومالية طويلة المدى',
     'Long-term strategic and financial advisory'),
    ('alsouri.png', 'Alsouri Co.', 'شركة الصوري', 'مقاولات وعقارات', 'Contracting and Real Estate',
     'الاستشارات الاستراتيجية ودراسات الجدوى المالية واستشارات التجريد',
     'Strategic advisory, financial feasibility studies, and divestment advisory'),
    ('maysan.png', 'Maysan Co.', 'مايسان', 'استثمار وأعمال', 'Investment and Business',
     'استشارات استراتيجية ومالية طويلة المدى',
     'Long-term strategic and financial advisory'),
]

html = ''
for logo, alt, name_ar, sector_ar, sector_en, service_ar, service_en in cards:
    html += f'<div class="flip-card"><div class="flip-inner"><div class="flip-front"><img src="logos/{logo}" alt="{alt}"/><p class="flip-sector">{sector_ar}</p></div><div class="flip-back"><p class="flip-service">{service_ar}</p><p class="flip-name">{name_ar}</p></div></div></div>'

new = '<section class="section border-b"><p class="section-label">عملاؤنا وشركاؤنا</p><p style="font-family:var(--arabic);font-size:13px;color:var(--ink4);margin-bottom:2rem;">مرر على اي شعار لمعرفة طبيعة العمل المقدم</p><div class="flip-grid">' + html + '</div></section>'

c2 = re.sub(r'<section class="section border-b"><p class="section-label">عملاؤنا وشركاؤنا</p>.*?</section>', new, c, flags=re.DOTALL)

with open('/Users/Ibrahim/Desktop/finsphere/index.html', 'w') as f:
    f.write(c2)

print('done' if c2 != c else 'no change - pattern not found')
