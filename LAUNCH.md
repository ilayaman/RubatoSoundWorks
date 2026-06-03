# 🚀 Launch Guide - Rubato Sound Works

## Quick Test Locally

### Option 1: Python (Recommended)
```bash
python3 -m http.server 8000
```
Then open: http://localhost:8000

### Option 2: PHP
```bash
php -S localhost:8000
```

### Option 3: Just open the file
Simply open `index.html` in your browser (some features may not work due to CORS)

## Deploy to GitHub Pages

### Initial Setup
1. Make sure your repository is on GitHub
2. Go to Settings → Pages
3. Source: Deploy from `main` branch
4. Folder: `/` (root)
5. Save

### Update and Deploy
```bash
# 1. Edit content in public/data/content.json
# 2. Commit and push
git add .
git commit -m "Update website content"
git push origin main
```

GitHub will automatically build and deploy! 🎉

## 📝 Content Updates

**All content is in:** `public/data/content.json`

### Quick Edits:
- **Contact info**: Update `site.email`, `site.phone`, `site.address`
- **Hero text**: Edit `hero.title` and `hero.subtitle`
- **Services**: Modify the `services` array
- **Portfolio items**: Update `portfolio` array
- **Social links**: Change `site.social` URLs

### After editing:
1. Save the JSON file
2. Refresh your browser (if testing locally)
3. Or commit and push (if deploying)

## 🎨 Design Customization

### Change Colors
Edit `css/style.css`, lines 6-15:
```css
--red-primary: #D62422;
--charcoal: #1C1919;
--gradient-start: #EC3027;
--gradient-mid: #E33E78;
--gradient-end: #FF7A27;
```

### Replace Logo
Replace `content/images/logo_colour.png` with your new logo

### Add Images
Put images in `content/images/` and reference in JSON

## ✅ Checklist Before Going Live

- [ ] Update all contact information in `content.json`
- [ ] Replace placeholder content with real services
- [ ] Add actual portfolio items
- [ ] Test on mobile device
- [ ] Test all links (WhatsApp, email, phone)
- [ ] Verify social media URLs
- [ ] Check spelling and grammar
- [ ] Test in different browsers

## 🆘 Troubleshooting

**Website not loading?**
- Make sure you're using a local server (not just file://)
- Check browser console for errors (F12)

**JSON not loading?**
- Verify `content.json` is valid JSON (use jsonlint.com)
- Check file path is correct
- Clear browser cache

**Styles look wrong?**
- Hard refresh (Ctrl+Shift+R or Cmd+Shift+R)
- Check CSS file loaded in Network tab

## 📞 Support

Need help? Contact hello@rubatosoundworks.com
