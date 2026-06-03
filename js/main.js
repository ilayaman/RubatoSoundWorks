// ===================================
// RUBATO SOUND WORKS - MAIN JAVASCRIPT
// JSON-Driven Content Management
// Feel the Rhythm. Shape the Sound.
// ===================================

let siteData = null;

// Load content from JSON
async function loadContent() {
    try {
        const response = await fetch('public/data/content.json');
        siteData = await response.json();
        initializeSite();
    } catch (error) {
        console.error('Error loading content:', error);
        // Fallback content if JSON fails to load
        loadFallbackContent();
    }
}

// Initialize all site sections
function initializeSite() {
    populateHero();
    populateServices();
    populatePortfolio();
    populateAbout();
    populateContact();
    populateFooter();
    initializeNavigation();
    initializeScrollEffects();
}

// ===================================
// HERO SECTION
// ===================================

function populateHero() {
    const { hero } = siteData;

    // Title with line breaks (RUBATO - bold, expressive, hero element)
    const titleHTML = hero.title.map(line =>
        `<span class="hero-title-line">${line}</span>`
    ).join('');
    document.getElementById('heroTitle').innerHTML = titleHTML;

    // Subtitle (SOUNDWORKS - lighter, supporting element)
    document.getElementById('heroSubtitle').textContent = hero.subtitle;

    // CTA Buttons
    const ctaHTML = hero.cta.map(button => {
        const btnClass = button.style === 'primary' ? 'btn btn-primary' : 'btn btn-secondary';
        return `<a href="${button.link}" class="${btnClass}">${button.text}</a>`;
    }).join('');
    document.getElementById('heroCta').innerHTML = ctaHTML;
}

// ===================================
// SERVICES SECTION
// ===================================

function populateServices() {
    const { services } = siteData;
    const grid = document.getElementById('servicesGrid');

    const servicesHTML = services.map(service => `
        <div class="service-card" data-aos="fade-up">
            <div class="service-icon">${service.icon}</div>
            <h3>${service.title}</h3>
            <p>${service.description}</p>
            ${service.features ? `
                <ul class="service-features">
                    ${service.features.map(feature => `<li>${feature}</li>`).join('')}
                </ul>
            ` : ''}
        </div>
    `).join('');

    grid.innerHTML = servicesHTML;
}

// ===================================
// PORTFOLIO SECTION
// ===================================

function populatePortfolio() {
    const { portfolio } = siteData;
    const grid = document.getElementById('portfolioGrid');

    const portfolioHTML = portfolio.map(item => `
        <div class="portfolio-item" data-aos="zoom-in">
            <div class="portfolio-image" style="background: linear-gradient(135deg, var(--gradient-start), var(--gradient-end));">
                ${item.image ? `<img src="${item.image}" alt="${item.title}" style="display:none;">` : ''}
            </div>
            <div class="portfolio-content">
                <div class="portfolio-type">${item.type}</div>
                <h3>${item.title}</h3>
                <div class="portfolio-artist">${item.artist}</div>
                <p class="portfolio-description">${item.description}</p>
            </div>
        </div>
    `).join('');

    grid.innerHTML = portfolioHTML;
}

// ===================================
// ABOUT SECTION
// ===================================

function populateAbout() {
    const { about } = siteData;

    document.getElementById('aboutTitle').textContent = about.title;
    document.getElementById('aboutDescription').textContent = about.description;

    const statsHTML = about.stats.map(stat => `
        <div class="stat-item" data-aos="flip-up">
            <span class="stat-number">${stat.number}</span>
            <span class="stat-label">${stat.label}</span>
        </div>
    `).join('');

    document.getElementById('aboutStats').innerHTML = statsHTML;
}

// ===================================
// CONTACT SECTION
// ===================================

function populateContact() {
    const { contact, site } = siteData;

    document.getElementById('contactTitle').textContent = contact.title;
    document.getElementById('contactDescription').textContent = contact.description;

    const detailsHTML = `
        <a href="mailto:${site.email}" class="contact-item">
            <span class="contact-icon">✉️</span>
            <span>${site.email}</span>
        </a>
        <a href="tel:${site.phone.replace(/\s/g, '')}" class="contact-item">
            <span class="contact-icon">📞</span>
            <span>${site.phone}</span>
        </a>
        <div class="contact-item">
            <span class="contact-icon">📍</span>
            <span>${site.address}</span>
        </div>
    `;

    document.getElementById('contactDetails').innerHTML = detailsHTML;

    // WhatsApp button
    const whatsappUrl = `https://wa.me/${site.whatsapp}?text=${encodeURIComponent(contact.whatsappMessage)}`;
    document.getElementById('whatsappBtn').href = whatsappUrl;
}

// ===================================
// FOOTER
// ===================================

function populateFooter() {
    const { site } = siteData;

    document.getElementById('footerName').textContent = site.name;

    if (site.social) {
        const socialHTML = Object.entries(site.social).map(([platform, url]) =>
            `<a href="${url}" target="_blank" rel="noopener">${platform.charAt(0).toUpperCase() + platform.slice(1)}</a>`
        ).join('');
        document.getElementById('footerSocial').innerHTML = socialHTML;
    }
}

// ===================================
// NAVIGATION
// ===================================

function initializeNavigation() {
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    const navLinks = document.querySelectorAll('.nav-link, .nav-link-cta');

    // Mobile menu toggle
    navToggle.addEventListener('click', () => {
        navToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Close menu on link click
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            navToggle.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

    // Active link on scroll
    window.addEventListener('scroll', () => {
        let current = '';
        const sections = document.querySelectorAll('section[id]');

        sections.forEach(section => {
            const sectionTop = section.offsetTop - 100;
            const sectionHeight = section.clientHeight;
            if (window.pageYOffset >= sectionTop && window.pageYOffset < sectionTop + sectionHeight) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('active');
            }
        });

        // Navbar background on scroll
        const nav = document.getElementById('nav');
        if (window.scrollY > 50) {
            nav.style.boxShadow = '0 4px 16px rgba(28, 25, 25, 0.1)';
        } else {
            nav.style.boxShadow = '0 2px 8px rgba(28, 25, 25, 0.05)';
        }
    });
}

// ===================================
// SCROLL EFFECTS & ANIMATIONS
// ===================================

function initializeScrollEffects() {
    // Simple fade-in on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -100px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);

    // Apply to elements with data-aos attribute
    document.querySelectorAll('[data-aos]').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    // Parallax effect for floating cards
    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const cards = document.querySelectorAll('.floating-card');
        cards.forEach((card, index) => {
            const speed = 0.1 + (index * 0.05);
            card.style.transform = `translateY(${scrolled * speed}px)`;
        });
    });
}

// ===================================
// FALLBACK CONTENT
// ===================================

function loadFallbackContent() {
    console.log('Loading fallback content...');
    document.getElementById('heroTitle').innerHTML = '<span>Where Sound</span><span>Meets Precision</span>';
    document.getElementById('heroSubtitle').textContent = 'Professional music production studio';
}

// ===================================
// INITIALIZE ON PAGE LOAD
// ===================================

document.addEventListener('DOMContentLoaded', loadContent);

// Smooth scroll for anchor links (initialized after DOM is ready)
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
});
