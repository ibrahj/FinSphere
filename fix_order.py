import re

with open('/Users/Ibrahim/Desktop/finsphere/index.html','r') as f:
    c = f.read()

cards = [
    ('nabed.png', 'NABED', 'نبض', 'رعاية صحية رقمية',
     'إعادة هيكلة الأعمال وتطوير الاستراتيجية المؤسسية والتخطيط المالي'),
    ('hamat_group.png', 'HAMAT Group', 'مجموعة هامات', 'خدمات المرافق',
     'استشارات جاهزية رأس المال ومراجعة القوائم المالية لدعم التموضع الاستراتيجي للنمو'),
    ('rwashin.png', 'Rwashin Compounds', 'رواشين', 'تطوير سكني',
     'بحث السوق وتحليل المشهد التنافسي لدعم قرارات الاستثمار والتطوير'),
    ('hamat_academy.png', 'HAMAT Academy', 'أكاديمية هامات', 'تعليم وتدريب',
     'تطوير الاستراتيجية المؤسسية وتخطيط النمو المؤسسي'),
    ('cfg.png', 'CFG Environment', 'CFG للبيئة', 'بيئة وطاقة',
     'بحث دخول السوق واستراتيجية إدارة الأداء'),
    ('wisework.png', 'WiseWork', 'وايز ورك', 'تقنية الأعمال',
     'استشارات جاهزية رأس المال والاستراتيجية المؤسسية وإطار إدارة أصحاب المصلحة'),
    ('idv.png', 'IDV', 'IDV', 'استثمار وتقنية',
     'استراتيجية إدارة الأداء وإعادة هيكلة الأعمال والاستشارات المالية'),
    ('samatwaiq.png', 'SAMA TWAIQ', 'سما طويق', 'تقنية الطائرات المسيرة',
     'استراتيجية إدارة الأداء وإعادة هيكلة الأعمال والاستشارات المالية'),
    ('invdro.png', 'Invdro', 'انفدرو', 'تقنية الطائرات المسيرة',
     'استراتيجية إدارة الأداء وإعادة هيكلة الأعمال والاستشارات المالية'),
    ('maysan.png', 'Maysan Co.', 'مايسان', 'استثمار وأعمال',
     'استشارات استراتيجية ومالية طويلة المدى'),
    ('alsouri.png', 'Alsouri Co.', 'شركة الصوري', 'مقاولات وعقارات',
     'الاستشارات الاستراتيجية ودراسات الجدوى المالية واستشارات التجريد'),
    ('ascor.png', 'Ascor Co.', 'أسكور', 'استثمار وأعمال',
     'استشارات استراتيجية ومالية طويلة المدى'),
    ('sju.png', 'Saudi Journalists Association', 'هيئة الصحفيين السعوديين', 'إعلام وصحافة',
     'الاستشارات المالية وإعادة هيكلة الأعمال والتخطيط المالي'),
    ('baljurashi.png', 'Baljurashi Boulevard', 'جادة بلجرشي', 'تطوير عقاري وسياحي',
     'بحث السوق واستشارات جاهزية رأس المال لدعم التموضع الاستثماري للمشروع'),
]

html = ''.join(
    f'<div class="flip-card"><div class="flip-inner"><div class="flip-front"><img src="logos/{logo}" alt="{alt}"/><p class="flip-sector">{sector}</p></div><div class="flip-back"><p class="flip-service">{service}</p><p class="flip-name">{name_ar}</p></div></div></div>'
    for logo, alt, name_ar, sector, service in cards
)

new = '<section class="section border-b"><p class="section-label">عملاؤنا وشركاؤنا</p><p style="font-family:var(--arabic);font-size:13px;color:var(--ink4);margin-bottom:2rem;">مرر على اي شعار لمعرفة طبيعة العمل المقدم</p><div class="flip-grid">' + html + '</div></section>'

c2 = re.sub(r'<section class="section border-b"><p class="section-label">عملاؤنا وشركاؤنا</p>.*?</section>', new, c, flags=re.DOTALL)

with open('/Users/Ibrahim/Desktop/finsphere/index.html', 'w') as f:
    f.write(c2)

print('done' if c2 != c else 'no change - pattern not found')
