/**
 * Google Analytics 4 (gtag.js) — uses SUNSET_GA_ID from site-config.js
 */
(function () {
    var id = typeof window.SUNSET_GA_ID === 'string' ? window.SUNSET_GA_ID.trim() : '';
    if (!id || id === 'G-XXXXXXXXXX' || !/^G-[A-Z0-9]+$/i.test(id)) {
        return;
    }

    var script = document.createElement('script');
    script.async = true;
    script.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(id);
    document.head.appendChild(script);

    window.dataLayer = window.dataLayer || [];
    function gtag() {
        window.dataLayer.push(arguments);
    }
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', id);
})();
