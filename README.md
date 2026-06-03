# Rubato Sound Works

**Feel the Rhythm. Shape the Sound.**

A modern, 3D immersive website for Rubato Sound Works music production studio, built with vanilla JavaScript and fully JSON-configurable content.

## 🎨 Design System

### Color Palette
- **Red** (#D62422) - Intensity, passion, and performance
- **Charcoal Black** (#1C1919) - Studio environment, dark and focused
- **Dynamic Gradient** (#EC3027 → #E33E78 → #FF7A27) - Live audio visualization
- **White** (#FFFFFF) - Readability and clarity

### Typography
- **Display Font**: Satoshi (substitute for Astro) - Bold, expressive, hero elements
- **Body Font**: Manrope - Lighter, supporting elements
- **Tone**: "Creative, but intentional" - Professional studio precision with artistic expression

## 📁 Project Structure

```
RubatoSoundWorks/
├── index.html              # Main HTML file
├── css/
│   └── style.css          # Complete styles with 3D effects
├── js/
│   └── main.js            # JSON-driven dynamic content
├── public/
│   └── data/
│       └── content.json   # All website content (EDIT THIS!)
├── content/
│   └── images/
│       ├── logo_colour.png
│       ├── logo_black.png
│       └── Vinyl.png
└── Branding_doc.pdf       # Brand guidelines
```

## 🚀 Quick Start

### 1. Edit Content
All website content is in `public/data/content.json`. Update:
- Site information (name, email, phone, address)
- Hero section text and buttons
- Services offered
- Portfolio projects
- About section stats
- Contact information
- Social media links

### 2. Test Locally
Simply open `index.html` in a browser, or use a local server:

```bash
# Python 3
python3 -m http.server 8000

# Node.js (if installed)
npx serve

# PHP
php -S localhost:8000
```

Visit `http://localhost:8000`

### 3. Deploy to GitHub Pages

1. **Commit your changes:**
```bash
git add .
git commit -m "Update website content"
git push origin main
```

2. **Enable GitHub Pages:**
   - Go to your repository settings
   - Navigate to "Pages"
   - Source: Deploy from `main` branch
   - Root folder: `/` (root)
   - Save

Your site will be live at: `https://yourusername.github.io/RubatoSoundWorks/`

## 🎯 Features

✅ **Fully JSON-Configurable** - Update all content without touching code  
✅ **Modern 3D Design** - Floating cards, parallax effects, animations  
✅ **Brand-Aligned** - Exact colors, typography, and visual style from branding doc  
✅ **Responsive** - Works perfectly on mobile, tablet, and desktop  
✅ **Performance Optimized** - Vanilla JavaScript, no heavy frameworks  
✅ **Smooth Animations** - Professional scroll effects and transitions  
✅ **WhatsApp Integration** - Direct messaging button  
✅ **SEO Ready** - Semantic HTML and meta tags  

## 📝 Customization Guide

### Update Colors
Edit CSS variables in `css/style.css`:
```css
:root {
    --red-primary: #D62422;
    --charcoal: #1C1919;
    --gradient-start: #EC3027;
    --gradient-mid: #E33E78;
    --gradient-end: #FF7A27;
}
```

### Add New Sections
1. Add HTML structure in `index.html`
2. Style in `css/style.css`
3. Add data to `public/data/content.json`
4. Populate with JavaScript in `js/main.js`

### Change Images
Replace files in `content/images/`:
- `logo_colour.png` - Main color logo
- `logo_black.png` - Black version
- `Vinyl.png` - Vinyl disc graphic

## 🌐 Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📄 License

© 2026 Rubato Sound Works. All rights reserved.

## 🛠️ Technical Stack

- **HTML5** - Semantic markup
- **CSS3** - Modern features (Grid, Flexbox, Custom Properties)
- **Vanilla JavaScript** - No dependencies
- **JSON** - Content management
- **GitHub Pages** - Free hosting

---

**Need help?** Open an issue or contact hello@rubatosoundworks.com
