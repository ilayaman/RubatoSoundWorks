# Quick Start Guide - Rubato Sound Works Website

## ✅ What's Already Done

Your website is **fully built and ready**! Here's what you have:

- ✅ Professional website with modern design
- ✅ 6 pages: Home, Services, Portfolio, Pricing, About, Contact
- ✅ WhatsApp integration (floating button + contact page)
- ✅ YouTube video embedding support
- ✅ Mobile-responsive design
- ✅ Configurable pricing page (enable/disable with a flag)
- ✅ All 7 services listed and described
- ✅ Deployment configs for Netlify, GitHub Pages, Vercel

## 🎯 Your Next Steps (In Order)

### 1. Preview Your Site (Right Now!)

Your site is running at: **http://localhost:8000**

Open it in your browser to see what it looks like!

### 2. Customize Your Information (15 minutes)

Edit `pelicanconf.py` and replace these placeholders:

```python
# Line 38: Your WhatsApp number
WHATSAPP_NUMBER = '919876543210'  # ← Change this!

# Line 92-94: Your contact info
EMAIL = 'info@rubatosoundworks.com'  # ← Change this!
PHONE = '+91 98765 43210'  # ← Change this!
ADDRESS = 'Your Studio Address, City, State, PIN'  # ← Change this!
```

**Enable/Disable Pricing:**
```python
# Line 32: Toggle pricing page visibility
ENABLE_PRICING = True  # Set to False to hide pricing
```

### 3. Add Your Content (30 minutes)

#### Add YouTube Videos
Edit `content/pages/portfolio.md`:
- Find `YOUR_VIDEO_ID_1`, `YOUR_VIDEO_ID_2`, etc.
- Replace with actual YouTube video IDs
- Example: If your video URL is `youtube.com/watch?v=dQw4w9WgXcQ`
- The video ID is: `dQw4w9WgXcQ`

#### Add Studio Photos
1. Add photos to `content/images/` folder
2. Name them: `studio-1.jpg`, `studio-2.jpg`, etc.
3. They'll automatically show in the portfolio!

#### Update Pricing
Edit `content/pages/pricing.md` with your actual prices.

### 4. Test Your Changes

```bash
# Rebuild the site
pelican content

# View at http://localhost:8000
# (Already running - just refresh your browser!)
```

### 5. Deploy to Internet (FREE!)

**Easiest: Netlify**

1. Create free account at [netlify.com](https://netlify.com)
2. Push your code to GitHub:
   ```bash
   git init
   git add .
   git commit -m "My studio website"
   ```
3. Create GitHub repo and push
4. On Netlify: "Add new site" → Import from GitHub
5. **Done!** Your site is live in 2 minutes!

**See full deployment guide:** Read `DEPLOYMENT.md`

---

## 📝 Common Customizations

### Change Colors

Edit `themes/rubato-theme/static/css/style.css` (line 9-11):

```css
--primary-color: #2563eb;  /* Change main color */
--secondary-color: #7c3aed;  /* Change secondary color */
```

### Add/Remove Services

Edit `SERVICES` list in `pelicanconf.py` (starting line 42).

### Change WhatsApp Message

Edit `pelicanconf.py` (line 39):

```python
WHATSAPP_MESSAGE = 'Your custom message here'
```

### Update Social Media

Edit `SOCIAL` in `pelicanconf.py` (line 27):

```python
SOCIAL = (
    ('YouTube', 'https://youtube.com/@yourhandle'),
    ('Instagram', 'https://instagram.com/yourhandle'),
)
```

---

## 🔧 Useful Commands

```bash
# Build the site
pelican content

# Start local server
pelican --listen

# Build for production
pelican content -s publishconf.py

# Clean and rebuild
rm -rf output/
pelican content

# Using Make (shortcut commands)
make html        # Build
make serve       # Serve locally
make publish     # Build for production
```

---

## 📱 Test Before Deploying

- [ ] All pages load correctly
- [ ] WhatsApp button works (click it!)
- [ ] YouTube videos embed properly
- [ ] All images display
- [ ] Contact information is correct
- [ ] Pricing shows/hides based on flag
- [ ] Site looks good on mobile (resize browser window)

---

## 💰 Total Cost

| Item | Cost |
|------|------|
| Hosting (Netlify/GitHub Pages) | **FREE** |
| Domain (optional) | $10-15/year |
| **Total** | **$0 - $15/year** |

---

## 🆘 Need Help?

**Build errors?**
```bash
pip3 install -r requirements.txt
pelican content
```

**Port already in use?**
```bash
pelican --listen --port 8001
```

**Changes not showing?**
- Stop the server (Ctrl+C)
- Rebuild: `pelican content`
- Restart: `pelican --listen`

---

## 📚 Full Documentation

- **README.md** - Complete feature list and usage
- **DEPLOYMENT.md** - Detailed deployment guide for all platforms
- **Pelican Docs** - https://docs.getpelican.com

---

## ✨ You're All Set!

Your professional music studio website is ready! 

**Current Status:**
- ✅ Website built successfully
- ✅ Running locally at http://localhost:8000
- ⏳ Waiting for your customization
- ⏳ Ready to deploy when you are

**Next:** Edit `pelicanconf.py` with your actual contact info and you're good to go! 🚀

---

Built with ❤️ using Pelican (Python Static Site Generator)
