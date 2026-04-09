# Color Scheme Update - Pastel Red Palette

## 🎨 New Color Palette

The website has been updated with a bright but subtle pastel red color scheme perfect for a modern music studio brand.

---

## 🎯 Color Variables

### **Primary Colors:**
```css
--primary-color: #FF6B6B    /* Soft coral red - main brand color */
--secondary-color: #FF8A80  /* Lighter warm red - hover states */
--accent-color: #FFB5A7     /* Peach tone - borders, icons */
```

### **Background Colors:**
```css
--bg-light: #FFF5F5         /* Light pastel background for sections */
--bg-soft: #FFD6D6          /* Softer pastel for cards */
--bg-white: #ffffff         /* Pure white for main content */
```

### **Text Colors:**
```css
--text-dark: #2B2B2B        /* Main text - high contrast */
--text-light: #7A7A7A       /* Muted text - descriptions */
```

### **Border & Shadows:**
```css
--border-color: #FFB5A7     /* Accent color for borders */
--shadow-sm: rgba(255, 107, 107, 0.1)
--shadow-md: rgba(255, 107, 107, 0.15)
--shadow-lg: rgba(255, 107, 107, 0.2)
--shadow-xl: rgba(255, 107, 107, 0.25)
```

---

## 🎨 Where Colors Are Applied

### **Primary Color (#FF6B6B):**
- ✅ Primary buttons (CTA, "Our Services", etc.)
- ✅ Links throughout the site
- ✅ Active navigation states
- ✅ Main call-to-action elements

### **Secondary Color (#FF8A80):**
- ✅ Button hover states
- ✅ Social link hover backgrounds
- ✅ Interactive element highlights

### **Accent Color (#FFB5A7):**
- ✅ Borders (page headers, cards)
- ✅ Blockquote left border
- ✅ Testimonial borders
- ✅ Subtle UI decorations
- ✅ Icon accents

### **Gradient:**
```css
background: linear-gradient(135deg, #FF6B6B 0%, #FFB5A7 100%);
```

**Applied to:**
- ✅ Hero section (homepage)
- ✅ CTA sections
- ✅ Call-to-action banners

### **Background Colors:**
- ✅ Services overview section: `#FFF5F5`
- ✅ Card backgrounds: `#ffffff`
- ✅ Alternating sections: `#FFF5F5`

---

## 🎯 Design Principles Maintained

### **✅ Contrast & Readability:**
- Dark text (#2B2B2B) on light backgrounds
- White text on gradient backgrounds
- WCAG AA compliant contrast ratios

### **✅ Soft & Warm Aesthetic:**
- Pastel tones throughout
- No harsh or neon colors
- Subtle, premium feel

### **✅ Musical Brand Identity:**
- Warm, inviting color palette
- Professional yet creative
- Energetic but not overwhelming

### **✅ Minimal & Modern:**
- Clean color transitions
- Subtle gradients
- Consistent application

---

## 📊 Before vs After

### **Old Color Scheme (Blue/Purple):**
```
Primary: #2563eb (bright blue)
Secondary: #7c3aed (purple)
Accent: #f59e0b (orange)
Gradient: #667eea → #764ba2 (blue-purple)
```

### **New Color Scheme (Pastel Red):**
```
Primary: #FF6B6B (soft coral red)
Secondary: #FF8A80 (warm red)
Accent: #FFB5A7 (peach)
Gradient: #FF6B6B → #FFB5A7 (coral-peach)
```

---

## 🎨 Usage Examples

### **Buttons:**
```css
/* Primary button */
background: #FF6B6B;
color: white;

/* Hover state */
background: #FF8A80;
```

### **Hero Section:**
```css
background: linear-gradient(135deg, #FF6B6B 0%, #FFB5A7 100%);
color: white;
```

### **Cards:**
```css
background: #ffffff;
border: 1px solid #FFB5A7;
box-shadow: 0 4px 6px rgba(255, 107, 107, 0.15);
```

### **Links:**
```css
color: #FF6B6B;

/* Hover */
color: #FF8A80;
```

---

## 🔄 How to Modify Colors in Future

All colors are defined as CSS variables in:
```
themes/rubato-theme/static/css/style.css (lines 9-24)
```

**To change the entire color scheme:**
1. Edit the `:root` variables
2. Rebuild: `pelican content -s publishconf.py`
3. Push: `git push`

**Example - Change to different red tones:**
```css
:root {
    --primary-color: #E63946;     /* Darker red */
    --secondary-color: #F1FAEE;   /* Light cream */
    --accent-color: #A8DADC;      /* Teal accent */
}
```

---

## ✅ What Was NOT Changed

### **Layout & Structure:**
- ✅ Grid layouts remain the same
- ✅ Spacing unchanged
- ✅ Component structure intact

### **Typography:**
- ✅ Font families unchanged
- ✅ Font sizes same
- ✅ Font weights consistent

### **Components:**
- ✅ All UI elements present
- ✅ Navigation structure same
- ✅ Footer layout unchanged

### **Functionality:**
- ✅ All features working
- ✅ WhatsApp integration intact
- ✅ Dynamic content unchanged

---

## 🎯 Brand Alignment

The pastel red color scheme aligns with:

✅ **Music Studio Vibe:**
- Warm and inviting (like a recording studio)
- Creative but professional
- Energetic without being harsh

✅ **Modern Aesthetic:**
- Soft pastels are trending
- Premium, high-end feel
- Minimalist and clean

✅ **Emotional Impact:**
- Red = passion, creativity, energy
- Pastel = approachable, friendly
- Perfect for music/audio brand

---

## 📱 Responsive Behavior

Colors work perfectly across all devices:
- ✅ Desktop: Full gradients, all colors visible
- ✅ Tablet: Same color scheme, optimized layouts
- ✅ Mobile: Consistent branding, readable text

---

## 🚀 Deployment Status

- ✅ **Local build:** Completed successfully
- ✅ **Pushed to GitHub:** main branch
- ✅ **GitHub Pages:** Will auto-deploy in 2-3 minutes
- ✅ **Live URL:** https://rubatosoundworks.com

---

**The website now features a cohesive, premium pastel red color scheme perfectly suited for a modern music studio brand!** 🎵🎨
