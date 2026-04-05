# Rubato Sound Works - Website

Professional music production studio website built with Pelican (Python static site generator).

## 🎵 Features

- ✅ **Python-based** - No JavaScript knowledge required!
- ✅ **Low Cost** - Free hosting on Netlify or GitHub Pages (~$1/month for domain only)
- ✅ **Low Maintenance** - Static site, no server or database needed
- ✅ **Fast & Secure** - Static files are fast and secure
- ✅ **Easy to Update** - Edit simple Markdown files
- ✅ **Mobile Responsive** - Looks great on all devices
- ✅ **Configurable Pricing** - Enable/disable pricing page with a flag
- ✅ **WhatsApp Integration** - Direct contact via WhatsApp
- ✅ **YouTube Embeds** - Showcase your projects
- ✅ **Portfolio Section** - Display your work with photos and videos

## 📋 Prerequisites

- Python 3.11+ installed on your computer
- Git (for version control and deployment)
- A text editor (VS Code, Sublime Text, or any editor you prefer)

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip3 install -r requirements.txt
```

### 2. Configure Your Site

Edit `pelicanconf.py` to customize your site:

```python
# Basic Information
SITENAME = 'Rubato Sound Works'
EMAIL = 'your-email@example.com'
PHONE = '+91 YOUR NUMBER'
ADDRESS = 'Your Studio Address'

# WhatsApp Number (with country code, no spaces)
WHATSAPP_NUMBER = '919876543210'  # Replace with your number

# Enable/Disable Pricing Page
ENABLE_PRICING = True  # Set to False to hide pricing
```

### 3. Build the Site

```bash
pelican content
```

### 4. Preview Locally

```bash
pelican --listen
```

Then open your browser to `http://localhost:8000`

## 📝 Updating Content

All content is in the `content/pages/` folder as Markdown files.

### Update Services

Edit `content/pages/services.md`

### Update Portfolio

Edit `content/pages/portfolio.md` and:
1. Replace `YOUR_VIDEO_ID_X` with actual YouTube video IDs
2. Add project descriptions
3. Add studio photos to `content/images/` folder

### Update Pricing

Edit `content/pages/pricing.md` with your actual prices.

To hide the pricing page completely:
- Open `pelicanconf.py`
- Set `ENABLE_PRICING = False`

### Add Studio Photos

1. Add images to `content/images/` folder
2. Reference in markdown: `![Description](/images/photo.jpg)`

### Update Contact Info

Edit `content/pages/contact.md` and update `pelicanconf.py` with your details.

## 🎨 Customization

### Change Colors

Edit `themes/rubato-theme/static/css/style.css`:

```css
:root {
    --primary-color: #2563eb;  /* Main color */
    --secondary-color: #7c3aed;  /* Secondary color */
    --accent-color: #f59e0b;  /* Accent color */
}
```

### Modify Services List

Edit the `SERVICES` list in `pelicanconf.py`:

```python
SERVICES = [
    {
        'name': 'Your Service Name',
        'icon': '🎵',  # Use any emoji
        'description': 'Service description',
    },
    # Add more services...
]
```

### Update Pricing Plans

Edit the `PRICING_PLANS` list in `pelicanconf.py`.

## 🌐 Deployment Options

### Option 1: Netlify (Recommended - Easiest)

1. Create account at [netlify.com](https://netlify.com)
2. Connect your GitHub repository
3. Netlify will auto-detect settings from `netlify.toml`
4. Your site will deploy automatically on every push!

**Cost:** FREE (100GB bandwidth/month)

### Option 2: GitHub Pages (Completely Free)

1. Create a GitHub repository
2. Push your code to GitHub
3. Go to Settings → Pages
4. Enable GitHub Actions for deployment
5. The `.github/workflows/deploy.yml` will handle automatic deployment

**Cost:** FREE (Unlimited bandwidth)

### Option 3: Vercel

1. Create account at [vercel.com](https://vercel.com)
2. Import your GitHub repository
3. Build command: `pelican content -s publishconf.py`
4. Output directory: `output`
5. Deploy!

**Cost:** FREE (100GB bandwidth/month)

### Option 4: Manual/Self-Hosting

1. Build the site: `pelican content -s publishconf.py`
2. Upload the `output/` folder to any web server
3. Done!

## 💰 Cost Breakdown

| Item | Service | Cost |
|------|---------|------|
| Hosting | Netlify/GitHub Pages/Vercel | FREE |
| Domain | Namecheap/GoDaddy | $10-15/year |
| **Total** | | **~$1/month** |

## 🔧 Common Tasks

### Adding a New Page

1. Create a new `.md` file in `content/pages/`
2. Add front matter:
```markdown
Title: Page Title
Slug: page-url

# Your content here
```
3. Add to menu in `pelicanconf.py`:
```python
MENUITEMS = [
    ('Home', '/'),
    ('New Page', '/page-url.html'),  # Add this
    # ...
]
```

### Embedding YouTube Videos

In your markdown files:

```html
<div class="video-container">
    <iframe width="100%" height="400"
            src="https://www.youtube.com/embed/VIDEO_ID"
            frameborder="0" allowfullscreen>
    </iframe>
</div>
```

Replace `VIDEO_ID` with the actual YouTube video ID from the URL.

### Changing WhatsApp Number

Edit `pelicanconf.py`:

```python
WHATSAPP_NUMBER = '919876543210'  # Format: CountryCode + Number (no spaces)
```

### Updating Social Media Links

Edit `pelicanconf.py`:

```python
SOCIAL = (
    ('YouTube', 'https://youtube.com/@yourhandle'),
    ('Instagram', 'https://instagram.com/yourhandle'),
    ('Facebook', 'https://facebook.com/yourpage'),
)
```

## 📱 WhatsApp Integration

The site includes:
- Floating WhatsApp button (bottom right corner)
- WhatsApp links on contact page
- Pre-filled message for easy inquiries

To customize the default message, edit `pelicanconf.py`:

```python
WHATSAPP_MESSAGE = 'Hello! I would like to inquire about your services.'
```

## 🖼️ Image Guidelines

### Recommended Sizes
- Studio photos: 1920x1080px
- Project images: 800x600px
- Optimize images before uploading (use TinyPNG.com)

### Adding Images
1. Place images in `content/images/` folder
2. Reference in markdown: `![Alt text](/images/filename.jpg)`

## 🐛 Troubleshooting

### Site not building?
```bash
# Check Python version (should be 3.11+)
python3 --version

# Reinstall dependencies
pip3 install -r requirements.txt

# Try building again
pelican content
```

### Changes not showing?
```bash
# Clear cache and rebuild
rm -rf output/
pelican content
pelican --listen
```

### Port 8000 already in use?
```bash
pelican --listen --port 8001
```

## 📞 Support

For help with Pelican: [Pelican Documentation](https://docs.getpelican.com)

## 📄 License

This website is for Rubato Sound Works. Feel free to modify as needed.

## 🎯 Next Steps

1. **Customize Content**: Update all pages with your actual information
2. **Add Photos**: Upload studio photos to `content/images/`
3. **Add Projects**: Update portfolio with your YouTube videos
4. **Update Contact**: Replace placeholder contact details
5. **Deploy**: Push to GitHub and deploy on Netlify/GitHub Pages
6. **Domain**: Purchase and connect your custom domain

---

**Built with ❤️ using Pelican - A Python Static Site Generator**

