#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# Basic Settings
AUTHOR = 'Rubato Sound Works'
SITENAME = 'Rubato Sound Works'
SITEURL = ''
SITE_DESCRIPTION = 'Professional Music Production Studio - Mixing, Mastering, Recording, and Sound Design'

PATH = 'content'
TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll - Social Links
LINKS = (
    ('YouTube', 'https://youtube.com/@rubatosoundworks'),
    ('Instagram', 'https://instagram.com/rubatosoundworks'),
)

# Social widget (Optional - add your social media handles)
SOCIAL = (
    ('YouTube', 'https://youtube.com/@rubatosoundworks'),
    ('Instagram', 'https://instagram.com/rubatosoundworks'),
    ('Facebook', 'https://facebook.com/rubatosoundworks'),
)

DEFAULT_PAGINATION = False

# ===== CUSTOM SETTINGS FOR RUBATO SOUND WORKS =====

# Enable/Disable Pricing Page (Set to False to hide pricing)
ENABLE_PRICING = True

# WhatsApp Contact Number (with country code, no spaces or special characters)
WHATSAPP_NUMBER = '7010862601'  # Replace with your actual number
WHATSAPP_MESSAGE = 'Hello! I would like to inquire about your services.'

# Services offered
SERVICES = [
    {
        'name': 'Mixing and Mastering',
        'icon': '🎚️',
        'description': 'Professional mixing and mastering to bring your tracks to industry standards.',
    },
    {
        'name': 'Recording Studio',
        'icon': '🎤',
        'description': 'State-of-the-art recording facilities for vocals, instruments, and more.',
    },
    {
        'name': 'Dubbing',
        'icon': '🎬',
        'description': 'High-quality dubbing services for films, series, and multimedia content.',
    },
    {
        'name': 'SFX (Sound Effects)',
        'icon': '🔊',
        'description': 'Custom sound effects design and production for any project.',
    },
    {
        'name': 'Short Film Scoring',
        'icon': '🎼',
        'description': 'Original music composition and scoring for short films and documentaries.',
    },
    {
        'name': 'Song Recording',
        'icon': '🎵',
        'description': 'Professional song recording sessions with experienced engineers.',
    },
    {
        'name': 'Music Production',
        'icon': '🎹',
        'description': 'Full music production services from pre-production to final mix.',
    },
]

# Pricing Plans (configurable - only shown if ENABLE_PRICING = True)
PRICING_PLANS = [
    {
        'service': 'Mixing and Mastering',
        'price': '₹5,000 - ₹15,000',
        'unit': 'per song',
        'features': ['Professional mixing', 'Industry-standard mastering', 'Unlimited revisions', '24-48 hour delivery'],
    },
    {
        'service': 'Recording Studio',
        'price': '₹2,000 - ₹5,000',
        'unit': 'per hour',
        'features': ['Professional acoustics', 'High-end microphones', 'Experienced engineers', 'Comfortable environment'],
    },
    {
        'service': 'Song Recording',
        'price': '₹8,000 - ₹25,000',
        'unit': 'per song',
        'features': ['Full production', 'Recording + Mixing', 'Session musicians (if needed)', 'Commercial use rights'],
    },
]

# Contact Information
EMAIL = 'inprogress@mail.com'
PHONE = '+91 70108 62601'
ADDRESS = 'Zamin Pallavaram, Chennai, Tamil Nadu, 600043'

# Static paths (for images, videos, etc.)
STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

# Theme settings
THEME = 'themes/rubato-theme'

# URL settings
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

# Plugins (optional - uncomment if you install plugins)
# PLUGIN_PATHS = ['pelican-plugins']
# PLUGINS = []

# Display pages in menu
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Menu items
MENUITEMS = [
    ('Home', '/'),
    ('Services', '/services.html'),
    ('Portfolio', '/portfolio.html'),
    ('About', '/about.html'),
    ('Contact', '/contact.html'),
]

# Add pricing to menu if enabled
if ENABLE_PRICING:
    MENUITEMS.insert(3, ('Pricing', '/pricing.html'))

# Use relative URLs for portability across different domains
RELATIVE_URLS = True
