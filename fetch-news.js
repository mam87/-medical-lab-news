// fetch-news.js
const axios = require('axios');
const fs = require('fs');

const API_KEY = process.env.NEWS_API_KEY; // سيتم توفيره من GitHub Secrets
const QUERY = 'medical laboratory OR CDC OR FDA OR "clinical lab"';
const PAGE_SIZE = 6;
const LANGUAGE = 'en'; // يمكن تغييره إلى 'ar' إذا أردت أخبار عربية (لكن المحتوى قد يكون أقل)

async function fetchNews() {
    try {
        const url = `https://newsapi.org/v2/everything?q=${encodeURIComponent(QUERY)}&pageSize=${PAGE_SIZE}&language=${LANGUAGE}&sortBy=publishedAt&apiKey=${API_KEY}`;
        const response = await axios.get(url);
        const articles = response.data.articles;

        const news = articles.map((article, index) => {
            // استخراج اسم المصدر
            let sourceName = article.source.name || 'مصدر عام';
            let sourceClass = 'source-local';
            let sourceIcon = 'hospital';
            if (sourceName.includes('CDC')) {
                sourceClass = 'source-cdc';
                sourceIcon = 'shield-alt';
            } else if (sourceName.includes('WHO') || sourceName.includes('World Health')) {
                sourceClass = 'source-who';
                sourceIcon = 'globe';
            } else if (sourceName.includes('FDA')) {
                sourceClass = 'source-fda';
                sourceIcon = 'flask';
            }

            // تحديد التصنيف (tag) بناءً على الكلمات المفتاحية
            let tag = 'tech';
            let tagName = 'تقني';
            let tagClass = 'tag-tech';
            const titleAndDesc = (article.title + ' ' + (article.description || '')).toLowerCase();
            if (titleAndDesc.includes('outbreak') || titleAndDesc.includes('salmonella') || titleAndDesc.includes('infection')) {
                tag = 'outbreak';
                tagName = 'وبائي';
                tagClass = 'tag-outbreak';
            } else if (titleAndDesc.includes('diagnostic') || titleAndDesc.includes('test') || titleAndDesc.includes('hba1c') || titleAndDesc.includes('assay')) {
                tag = 'diagnostic';
                tagName = 'تشخيصي';
                tagClass = 'tag-diagnostic';
            } else if (titleAndDesc.includes('medicare') || titleAndDesc.includes('guideline') || titleAndDesc.includes('cms')) {
                tag = 'guideline';
                tagName = 'إرشادات';
                tagClass = 'tag-guideline';
            }

            // تنسيق التاريخ
            const publishedDate = new Date(article.publishedAt);
            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            const dateStr = publishedDate.toLocaleDateString('ar-SA', options);

            return {
                id: index + 1,
                title: article.title,
                excerpt: article.description || 'لا يوجد وصف متاح',
                source: sourceName,
                sourceClass: sourceClass,
                sourceIcon: sourceIcon,
                date: dateStr,
                tag: tag,
                tagClass: tagClass,
                tagName: tagName
            };
        });

        // كتابة الملف news.json
        fs.writeFileSync('news.json', JSON.stringify(news, null, 2));
        console.log('✅ تم جلب الأخبار وحفظها في news.json');
    } catch (error) {
        console.error('❌ خطأ في جلب الأخبار:', error.message);
        process.exit(1);
    }
}

fetchNews();
