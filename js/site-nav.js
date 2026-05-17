/**
 * Shared site navigation — single source of truth (v6).
 * Tabs: Home, About, Services, Gallery, Blog, Schedule, Contact
 */
(function () {
    var NAV_ITEMS = [
        { href: 'index.html', label: 'Home', id: 'home' },
        { href: 'about.html', label: 'About', id: 'about' },
        { href: 'services.html', label: 'Services', id: 'services' },
        { href: 'gallery.html', label: 'Gallery', id: 'gallery' },
        { href: 'blog/index.html', label: 'Blog', id: 'blog' },
        { href: 'schedule-appointment.html', label: 'Schedule', id: 'schedule' },
        { href: 'contact.html', label: 'Contact', id: 'contact' }
    ];

    var PAGE_MAP = {
        'index.html': 'home',
        '': 'home',
        'about.html': 'about',
        'services.html': 'services',
        'painting-st-augustine.html': 'services',
        'interior-painting-st-augustine.html': 'services',
        'exterior-painting-st-augustine.html': 'services',
        'painting-jacksonville.html': 'services',
        'service-areas.html': 'services',
        'faq.html': 'services',
        'gallery.html': 'gallery',
        'schedule-appointment.html': 'schedule',
        'contact.html': 'contact'
    };

    function linkPrefix() {
        var path = window.location.pathname || '';
        if (path.indexOf('/blog/') !== -1 || path.endsWith('/blog')) {
            return '../';
        }
        return '';
    }

    function currentPageId() {
        var path = window.location.pathname || '';
        if (path.indexOf('/blog/') !== -1 || path.endsWith('/blog')) {
            return 'blog';
        }
        var file = path.split('/').pop() || 'index.html';
        return PAGE_MAP[file] || 'home';
    }

    function buildNav() {
        var pre = linkPrefix();
        var activeId = currentPageId();
        var links = NAV_ITEMS.map(function (item) {
            var isActive = item.id === activeId;
            var cls = 'nav-link' + (isActive ? ' active' : '');
            var cur = isActive ? ' aria-current="page"' : '';
            return '<li class="nav-item"><a class="' + cls + '" href="' + pre + item.href + '"' + cur + '>' + item.label + '</a></li>';
        }).join('\n                    ');

        return (
            '<nav class="navbar navbar-expand-lg navbar-dark fixed-top" id="site-navbar">' +
            '<div class="container">' +
            '<a class="navbar-brand" href="' + pre + 'index.html" aria-label="Sunset Home Painting Home">' +
            '<img src="' + pre + 'images/Sunset Home 2.PNG" alt="Sunset Home Painting" class="logo-img">' +
            '<span>Sunset Home Painting</span></a>' +
            '<button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#siteNavbarCollapse" ' +
            'aria-controls="siteNavbarCollapse" aria-expanded="false" aria-label="Toggle navigation">' +
            '<span class="navbar-toggler-icon"></span></button>' +
            '<div class="collapse navbar-collapse" id="siteNavbarCollapse">' +
            '<ul class="navbar-nav ms-auto site-nav-list">' + links + '</ul>' +
            '</div></div></nav>'
        );
    }

    function mount() {
        var mountEl = document.getElementById('site-nav-mount');
        if (!mountEl) {
            return;
        }
        mountEl.outerHTML = buildNav();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', mount);
    } else {
        mount();
    }
})();
