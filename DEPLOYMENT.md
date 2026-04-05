# Deployment Guide for Rubato Sound Works

Complete step-by-step guide to deploy your website.

## 🚀 Deployment Options Comparison

| Feature | Netlify | GitHub Pages | Vercel | Cloudflare Pages |
|---------|---------|--------------|--------|------------------|
| **Cost** | FREE | FREE | FREE | FREE |
| **Bandwidth** | 100GB/month | Unlimited | 100GB/month | Unlimited |
| **Build Minutes** | 300/month | Unlimited | Unlimited | 500/month |
| **Custom Domain** | ✅ Free | ✅ Free | ✅ Free | ✅ Free |
| **SSL Certificate** | ✅ Auto | ✅ Auto | ✅ Auto | ✅ Auto |
| **Ease of Setup** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Deploy Speed** | Fast | Medium | Fast | Very Fast |
| **Best For** | General use | Simple sites | All projects | High traffic |

**Recommendation:** Start with **Netlify** or **GitHub Pages** - both are excellent and completely free.

---

## Option 1: Deploy to Netlify (Recommended)

### Step 1: Prepare Your Code

1. Make sure all your changes are committed to Git:
```bash
git init
git add .
git commit -m "Initial commit"
```

2. Create a GitHub repository and push:
```bash
git remote add origin https://github.com/yourusername/rubatosoundworks.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Netlify

1. Go to [netlify.com](https://netlify.com) and sign up (free)
2. Click "Add new site" → "Import an existing project"
3. Choose "GitHub" and authorize Netlify
4. Select your repository
5. Netlify will auto-detect settings from `netlify.toml`:
   - Build command: `pelican content -s publishconf.py`
   - Publish directory: `output`
6. Click "Deploy site"

### Step 3: Configure Custom Domain (Optional)

1. In Netlify dashboard, go to "Domain settings"
2. Click "Add custom domain"
3. Enter your domain (e.g., `rubatosoundworks.com`)
4. Follow DNS configuration instructions from your domain registrar

**Your site is now live! 🎉**

Every time you push to GitHub, Netlify will automatically rebuild and deploy.

---

## Option 2: Deploy to GitHub Pages

### Step 1: Prepare Repository

1. Create a GitHub repository
2. Push your code:
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/rubatosoundworks.git
git push -u origin main
```

### Step 2: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click "Settings" → "Pages"
3. Under "Source", select "GitHub Actions"
4. The workflow file `.github/workflows/deploy.yml` is already configured!

### Step 3: Deploy

1. Any push to the `main` branch will trigger automatic deployment
2. Wait 2-3 minutes for the first build
3. Your site will be live at `https://yourusername.github.io/rubatosoundworks/`

### Step 4: Custom Domain (Optional)

1. In GitHub Pages settings, add your custom domain
2. Create a `CNAME` file in your repository:
```bash
echo "rubatosoundworks.com" > content/extra/CNAME
```
3. Update `pelicanconf.py`:
```python
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}
```
4. Configure DNS at your domain registrar

---

## Option 3: Deploy to Vercel

### Step 1: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/rubatosoundworks.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Vercel

1. Go to [vercel.com](https://vercel.com) and sign up
2. Click "Add New Project"
3. Import your GitHub repository
4. Configure build settings:
   - **Build Command:** `pelican content -s publishconf.py`
   - **Output Directory:** `output`
5. Click "Deploy"

---

## 📱 Before Going Live Checklist

### 1. Update Configuration

Edit `pelicanconf.py`:

- [ ] Change `WHATSAPP_NUMBER` to your actual number
- [ ] Update `EMAIL`, `PHONE`, `ADDRESS`
- [ ] Set `SITEURL` in `publishconf.py` to your actual domain
- [ ] Update social media links in `SOCIAL`

### 2. Update Content

- [ ] Replace placeholder text in all pages
- [ ] Add your actual YouTube video IDs in portfolio.md
- [ ] Upload studio photos to `content/images/`
- [ ] Update pricing with your actual rates
- [ ] Add your actual services and descriptions

### 3. Test Everything

- [ ] Build locally: `pelican content`
- [ ] Test locally: `pelican --listen`
- [ ] Check all pages load correctly
- [ ] Test WhatsApp links
- [ ] Verify YouTube embeds work
- [ ] Test on mobile (use browser dev tools)
- [ ] Check all images display correctly

### 4. SEO & Performance

- [ ] Add Google Analytics (optional)
- [ ] Compress all images
- [ ] Update meta descriptions
- [ ] Test site speed

---

## 🌐 Custom Domain Setup

### Buying a Domain

**Recommended Registrars:**
- [Namecheap](https://namecheap.com) - ~$12/year
- [Google Domains](https://domains.google) - ~$12/year  
- [Porkbun](https://porkbun.com) - ~$10/year

### Connecting to Netlify

1. In Netlify: Domain settings → Add custom domain
2. In your domain registrar's DNS settings, add:
   - **A Record**: `@` → `75.2.60.5`
   - **CNAME**: `www` → `your-site.netlify.app`
3. Wait 24-48 hours for DNS propagation
4. Netlify will auto-provision SSL certificate

### Connecting to GitHub Pages

1. In GitHub Pages settings, add custom domain
2. In your domain registrar's DNS settings:
   - **A Record**: `@` → `185.199.108.153`
   - **A Record**: `@` → `185.199.109.153`
   - **A Record**: `@` → `185.199.110.153`
   - **A Record**: `@` → `185.199.111.153`
   - **CNAME**: `www` → `yourusername.github.io`

---

## 🔄 Updating Your Site

### Make Changes

1. Edit content files in `content/pages/`
2. Test locally: `pelican --listen`
3. Commit and push:
```bash
git add .
git commit -m "Update content"
git push
```

### Automatic Deployment

- **Netlify:** Auto-deploys on push (2-3 minutes)
- **GitHub Pages:** Auto-deploys on push (2-3 minutes)
- **Vercel:** Auto-deploys on push (1-2 minutes)

---

## 🆘 Troubleshooting

**Build fails on deployment:**
- Check `requirements.txt` is present
- Verify Python version in deploy settings
- Check build logs for specific errors

**Site shows 404:**
- Verify `output/` folder was created
- Check publish directory setting
- Confirm index.html exists in output

**Images not loading:**
- Check image paths (should be `/images/filename.jpg`)
- Verify images are in `content/images/`
- Check file names (case-sensitive on some servers)

---

## 📊 Post-Launch

### Analytics (Optional)

Add Google Analytics to track visitors:
1. Get tracking ID from Google Analytics
2. Edit `publishconf.py`:
```python
GOOGLE_ANALYTICS = 'UA-XXXXX-Y'
```

### Performance Monitoring

- Use [Google PageSpeed Insights](https://pagespeed.web.dev)
- Monitor uptime with [UptimeRobot](https://uptimerobot.com) (free)

---

**You're all set! 🎉 Your website is now live and professional!**
