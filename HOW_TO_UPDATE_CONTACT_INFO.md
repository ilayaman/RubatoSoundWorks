# How to Update Contact Information

## 📋 Quick Reference: All Files to Update

When changing contact information (WhatsApp, phone, email, address), update these files:

---

## 1️⃣ Main Configuration (Primary Source) ⭐

**File:** `pelicanconf.py`

This is the **MOST IMPORTANT** file! Update here first:

```python
# Line 43 - WhatsApp Number (format: country code + number, no spaces or +)
WHATSAPP_NUMBER = '917010862601'  # Example: 91 (India) + 7010862601

# Lines 108-110 - Contact Details
EMAIL = 'inprogress@mail.com'
PHONE = '+91 70108 62601'
ADDRESS = 'Zamin Pallavaram, Chennai, Tamil Nadu, 600043'
```

**What uses this:**
- Footer on all pages (automatically)
- WhatsApp floating button (automatically)
- Home page contact section (automatically)

---

## 2️⃣ Contact Page Content

**File:** `content/pages/contact.md`

Update these sections:

### WhatsApp Links (2 places):
```markdown
# Line 15 - First WhatsApp button
<a href="https://wa.me/917010862601?text=...

# Line 96 - Second WhatsApp button  
<a href="https://wa.me/917010862601?text=...
```

### Email:
```markdown
# Line 24
**inprogress@mail.com**
```

### Phone:
```markdown
# Line 29
**+91 70108 62601**
```

### Address:
```markdown
# Lines 42-44
Rubato Sound Works  
Zamin Pallavaram  
Chennai, Tamil Nadu, 600043
```

---

## 3️⃣ Social Media Links

**File:** `pelicanconf.py` (lines 27-31)

```python
SOCIAL = (
    ('YouTube', 'https://youtube.com/@rubatosoundworks'),
    ('Instagram', 'https://instagram.com/rubatosoundworks'),
    ('Facebook', 'https://facebook.com/rubatosoundworks'),
)
```

Also appears in:
- `content/pages/contact.md` (lines 67-69)

---

## 🔄 After Making Changes

### Step 1: Rebuild the site
```bash
pelican content -s publishconf.py
```

### Step 2: Test locally (optional)
```bash
pelican --listen
# Visit http://localhost:8000 to preview
```

### Step 3: Push to GitHub
```bash
git add .
git commit -m "Update contact information"
git push
```

### Step 4: Wait for Netlify
Netlify will automatically rebuild in 2-3 minutes.

---

## ✅ Checklist When Updating Contact Info

Use this checklist to make sure you update everything:

- [ ] `pelicanconf.py` - WHATSAPP_NUMBER (line 43)
- [ ] `pelicanconf.py` - EMAIL (line 108)
- [ ] `pelicanconf.py` - PHONE (line 109)
- [ ] `pelicanconf.py` - ADDRESS (line 110)
- [ ] `content/pages/contact.md` - WhatsApp link #1 (line 15)
- [ ] `content/pages/contact.md` - WhatsApp link #2 (line 96)
- [ ] `content/pages/contact.md` - Email (line 24)
- [ ] `content/pages/contact.md` - Phone (line 29)
- [ ] `content/pages/contact.md` - Address (lines 42-44)
- [ ] Rebuild site: `pelican content -s publishconf.py`
- [ ] Push to GitHub: `git push`

---

## 🎯 Quick Update Process

**Just need to change phone/WhatsApp quickly?**

1. Edit `pelicanconf.py` - lines 43, 109
2. Edit `content/pages/contact.md` - lines 15, 29, 96
3. Run:
   ```bash
   pelican content -s publishconf.py
   git add .
   git commit -m "Update phone number"
   git push
   ```
4. Done! Live in 3 minutes.

---

## 🔍 Find & Replace Method

**Pro tip:** Use your text editor's "Find and Replace" feature:

1. **Find:** `919876543210`
2. **Replace with:** Your new WhatsApp number
3. **Files:** Search in all `.md` and `.py` files
4. Replace all occurrences

Same for email:
1. **Find:** `info@rubatosoundworks.com`
2. **Replace with:** Your new email
3. Replace all

---

## ⚠️ Common Mistakes

### WhatsApp Number Format
❌ Wrong: `+91 7010862601` or `91-7010862601`
✅ Correct: `917010862601` (no spaces, no +, no dashes)

### Email Format
❌ Wrong: `Email: info@example.com`
✅ Correct: `info@example.com` (just the email)

### Phone Display Format
✅ Correct: `+91 70108 62601` (with + and spaces for display)

---

## 📱 WhatsApp Message Customization

To change the pre-filled WhatsApp message:

**File:** `pelicanconf.py` (line 39)

```python
WHATSAPP_MESSAGE = 'Hello! I would like to inquire about your services.'
```

This appears in the WhatsApp link like:
```
https://wa.me/917010862601?text=Your%20message%20here
```

---

## 🆘 Need Help?

If contact info isn't updating:

1. **Check the file paths** - Make sure you're editing the right files
2. **Rebuild the site** - Run `pelican content -s publishconf.py`
3. **Clear browser cache** - Press Ctrl+Shift+R (or Cmd+Shift+R on Mac)
4. **Wait for Netlify** - Deploys take 2-3 minutes after pushing

---

**Updated:** 2026-04-06
