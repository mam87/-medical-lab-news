const fs = require('fs');
const path = require('path');

// دالة لإنشاء أخبار عشوائية
function generateLatestNews() {
    const today = new Date().toLocaleDateString('ar-SA');
    const newsSources = ['CDC', 'WHO', 'FDA', 'ASCLS', 'Mayo Clinic', 'CMS'];
    const newsTypes = [
        { tag: 'outbreak', tagClass: 'tag-outbreak', tagName: 'وبائي' },
        { tag: 'tech', tagClass: 'tag-tech', tagName: 'تقني' },
        { tag: 'diagnostic', tagClass: 'tag-diagnostic', tagName: 'تشخيصي' },
        { tag: 'guideline', tagClass: 'tag-guideline', tagName: 'إرشادات' }
    ];
    
    const icons = ['shield-virus', 'globe', 'vial', 'file-medical-alt', 'users', 'robot'];
    const imageClasses = ['cdc', 'who', 'fda', 'local'];
    const sourceClasses = ['source-cdc', 'source-who', 'source-fda', 'source-local'];
    
    // عناوين الأخبار المحتملة
    const newsTitles = [
        'يصدر تقريراً جديداً حول تقنيات التشخيص',
        'يعلن عن بروتوكول جديد لفحص الأمراض المعدية',
        'يطلق مبادرة لمكافحة مقاومة المضادات الحيوية',
        'يحدث معايير الجودة في المختبرات الطبية',
        'يعتمد جهازاً جديداً للتحاليل السريعة',
        'يحذر من نقص الكوادر المتخصصة في المختبرات'
    ];
    
    // نصوص الأخبار المحتملة
    const newsExcerpts = [
        'أحدث التطورات في مجال المختبرات الطبية تشير إلى تغييرات هامة في الممارسات والتقنيات المستخدمة.',
        'الدراسات الحديثة تظهر تحسناً كبيراً في دقة وسرعة النتائج المخبرية باستخدام التقنيات الجديدة.',
        'الخبراء يوصون بتحديث البروتوكولات الحالية لمواكبة التطورات العلمية والتقنية في المجال.',
        'التقارير تشير إلى أهمية الاستثمار في التدريب والتطوير المستمر لكوادر المختبرات.',
        'الأبحاث الجديدة تفتح آفاقاً واعدة في مجال التشخيص المبكر للأمراض.'
    ];
    
    // إنشاء 6 أخبار عشوائية
    const news = [];
    for (let i = 0; i < 6; i++) {
        const sourceIndex = Math.floor(Math.random() * newsSources.length);
        const typeIndex = Math.floor(Math.random() * newsTypes.length);
        const imageClassIndex = Math.floor(Math.random() * imageClasses.length);
        const titleIndex = Math.floor(Math.random() * newsTitles.length);
        const excerptIndex = Math.floor(Math.random() * newsExcerpts.length);
        
        news.push({
            id: i + 1,
            title: `${newsSources[sourceIndex]} ${newsTitles[titleIndex]}`,
            excerpt: newsExcerpts[excerptIndex],
            source: newsSources[sourceIndex],
            sourceClass: sourceClasses[Math.min(sourceIndex, sourceClasses.length - 1)],
            imageClass: imageClasses[imageClassIndex],
            icon: icons[Math.min(i, icons.length - 1)],
            date: today,
            tag: newsTypes[typeIndex].tag,
            tagClass: newsTypes[typeIndex].tagClass,
            tagName: newsTypes[typeIndex].tagName
        });
    }
    
    return news;
}

// قراءة ملف HTML الحالي
const htmlPath = path.join(__dirname, '../index.html');
let htmlContent = fs.readFileSync(htmlPath, 'utf8');

// إنشاء بيانات الأخبار الجديدة
const latestNews = generateLatestNews();

// تحويل بيانات الأخبار إلى كود JavaScript
const newsDataScript = `
// بيانات الأخبار - تم التحديث تلقائياً في ${new Date().toLocaleDateString('ar-SA')}
let allNews = ${JSON.stringify(latestNews, null, 2)};
`;

// البحث عن قسم بيانات الأخبار واستبداله
const newsDataStart = '// News Data';
const newsDataEnd = '// Load News';
const startIndex = htmlContent.indexOf(newsDataStart);
const endIndex = htmlContent.indexOf(newsDataEnd);

if (startIndex !== -1 && endIndex !== -1) {
    // استبدال قسم بيانات الأخبار
    const beforeNewsData = htmlContent.substring(0, startIndex);
    const afterNewsData = htmlContent.substring(endIndex);
    
    // بناء محتوى HTML الجديد
    const newHtmlContent = beforeNewsData + newsDataScript + '\n\n' + afterNewsData;
    
    // كتابة ملف HTML المحدث
    fs.writeFileSync(htmlPath, newHtmlContent);
    console.log('✅ تم تحديث بيانات الأخبار بنجاح');
} else {
    console.error('❌ لم يتم العثور على قسم بيانات الأخبار في الملف');
}
