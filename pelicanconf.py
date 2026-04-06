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

# Enable Jinja2 processing in Markdown files (for dynamic content)
FORMATTED_FIELDS = ['summary', 'description']
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives']

# Markdown extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

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

# ===== PORTFOLIO DATA (DYNAMIC!) =====

# Featured Projects - Add/remove projects here, they'll automatically show on the portfolio page!
FEATURED_PROJECTS = [
    {
        'title': 'Your Project Name',
        'type': 'Music Production | Song Recording',
        'artist': 'Artist Name',
        'description': 'A beautiful blend of traditional and contemporary sounds. This project showcased our expertise in live instrument recording and modern production techniques.',
        'youtube_id': 'dQw4w9WgXcQ',  # Replace with actual YouTube video ID
    },
    {
        'title': 'Short Film Title',
        'type': 'Film Scoring | Sound Design',
        'artist': 'Director Name',
        'description': 'Original score for an award-winning short film. We created an emotive soundscape that enhanced the storytelling.',
        'youtube_id': 'dQw4w9WgXcQ',  # Replace with actual YouTube video ID
    },
    {
        'title': 'Album/EP Name',
        'type': 'Mixing and Mastering',
        'artist': 'Artist Name',
        'description': 'Full album mixing and mastering project. Delivered punchy, radio-ready tracks with excellent dynamic range.',
        'youtube_id': 'dQw4w9WgXcQ',  # Replace with actual YouTube video ID
    },
    # Add more projects here! Just copy the dict structure above
]

# Studio Photos - Add your studio images here
STUDIO_PHOTOS = [
    {
        'filename': 'studio-1.jpg',
        'caption': 'Our main recording room',
        'alt': 'Studio Main Room',
    },
    {
        'filename': 'studio-2.jpg',
        'caption': 'State-of-the-art control room',
        'alt': 'Control Room',
    },
    {
        'filename': 'studio-3.jpg',
        'caption': 'Professional vocal booth',
        'alt': 'Vocal Booth',
    },
    {
        'filename': 'studio-4.jpg',
        'caption': 'Industry-standard equipment',
        'alt': 'Equipment',
    },
    # Add more photos here!
]

# Client Testimonials - Add/remove testimonials dynamically!
TESTIMONIALS = [
    {
        'text': 'Rubato Sound Works transformed our tracks into professional, radio-ready songs. Highly recommended!',
        'author': 'Client Name',
        'role': 'Artist',
    },
    {
        'text': 'The team\'s attention to detail and creative input elevated our short film\'s score to another level.',
        'author': 'Director Name',
        'role': 'Filmmaker',
    },
    {
        'text': 'Professional, fast, and affordable. Best music production studio in the area!',
        'author': 'Client Name',
        'role': 'Music Producer',
    },
    # Add more testimonials here! The page will automatically adjust
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

