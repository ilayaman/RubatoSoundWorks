# Dynamic Portfolio Management Guide

## 🎯 You Got It! Portfolio is Now Completely Dynamic!

Your portfolio page is now **100% data-driven**. Add/remove projects, photos, or testimonials in ONE file, and the page automatically adjusts!

---

## 🚀 How It Works Now

### **Before (Hardcoded - Bad!):**
```markdown
### Project 1: [Your Project Name]
**Type:** Music Production
...
<iframe src="...YOUR_VIDEO_ID_1..."></iframe>

### Project 2: [Another Project]
**Type:** Film Scoring
...
<iframe src="...YOUR_VIDEO_ID_2..."></iframe>
```

**Problem:** To add a 4th project, you'd have to:
1. Copy-paste HTML
2. Manually edit all fields
3. Risk formatting errors

---

### **After (Dynamic - Good!):**
```python
# pelicanconf.py - Just add to this list!
FEATURED_PROJECTS = [
    {'title': 'Project 1', 'youtube_id': 'abc123', ...},
    {'title': 'Project 2', 'youtube_id': 'def456', ...},
    {'title': 'Project 3', 'youtube_id': 'ghi789', ...},
    # Add as many as you want!
]
```

**Solution:** To add a 4th project:
1. Add one dict to the list
2. Done! Page updates automatically ✨

---

## 📝 How to Add Content

### **1. Add a New Featured Project**

**File:** `pelicanconf.py` (lines 109-133)

```python
FEATURED_PROJECTS = [
    # Existing projects...
    
    # Add your new project here:
    {
        'title': 'My Latest Song',
        'type': 'Song Recording | Mixing',
        'artist': 'Artist Name',
        'description': 'A powerful ballad with orchestral elements...',
        'youtube_id': 'YOUR_YOUTUBE_ID',  # Just the ID, not full URL!
    },
]
```

**That's it!** The portfolio page will automatically:
- ✅ Create a new section
- ✅ Embed the YouTube video
- ✅ Format everything perfectly
- ✅ Add separators

---

### **2. Add Studio Photos**

**File:** `pelicanconf.py` (lines 135-157)

**Step 1:** Add photo to `content/images/` folder
- Example: `content/images/studio-5.jpg`

**Step 2:** Add to config:
```python
STUDIO_PHOTOS = [
    # Existing photos...
    
    # Add new photo:
    {
        'filename': 'studio-5.jpg',
        'caption': 'Our mixing console',
        'alt': 'Mixing Console',
    },
]
```

**Done!** Photo appears on the portfolio page automatically.

---

### **3. Add Client Testimonials**

**File:** `pelicanconf.py` (lines 159-178)

```python
TESTIMONIALS = [
    # Existing testimonials...
    
    # Add new testimonial:
    {
        'text': 'Amazing experience! Professional quality at reasonable prices.',
        'author': 'John Doe',
        'role': 'Independent Artist',
    },
]
```

**That's it!** The testimonial appears with perfect formatting.

---

## 🔄 How the Loop Works

### **In `portfolio.md`:**

```markdown
{% for project in FEATURED_PROJECTS %}
### {{ project.title }}
**Type:** {{ project.type }}
...
{% endfor %}
```

This is a **Jinja2 for-loop** (like Python!)

**What it does:**
1. Loops through each project in `FEATURED_PROJECTS`
2. Creates a section for each one
3. Fills in the data automatically

**If you have:**
- 2 projects → Shows 2 sections
- 5 projects → Shows 5 sections
- 10 projects → Shows 10 sections

**Completely automatic!** 🎉

---

## 📊 Data Structure Examples

### **YouTube Video ID**

**Full URL:**
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
                                 ^^^^^^^^^^^
                                 This part only!
```

**What to put in config:**
```python
'youtube_id': 'dQw4w9WgXcQ',  # ← Just the ID
```

**For embedded videos:**
```
https://www.youtube.com/embed/abc123xyz
                              ^^^^^^^^^
                              This part!
```

---

### **Photo Filenames**

```python
STUDIO_PHOTOS = [
    {
        'filename': 'studio-1.jpg',      # Must match file in content/images/
        'caption': 'What shows below',   # Text under the image
        'alt': 'For screen readers',     # Accessibility
    },
]
```

---

## 🎯 Real-World Examples

### **Example 1: Add a 4th Project**

```python
# In pelicanconf.py, just add to the list:
FEATURED_PROJECTS = [
    # ... existing 3 projects ...
    
    {
        'title': 'Corporate Advertisement Jingle',
        'type': 'Music Production | Voice Over',
        'artist': 'XYZ Corporation',
        'description': 'Catchy 30-second jingle for regional TV campaign.',
        'youtube_id': 'new_video_id',
    },
]
```

**Result:** Portfolio page now shows 4 projects automatically!

---

### **Example 2: Add More Studio Photos**

```python
STUDIO_PHOTOS = [
    # ... existing 4 photos ...
    
    {'filename': 'studio-5.jpg', 'caption': 'Guitar collection', 'alt': 'Guitars'},
    {'filename': 'studio-6.jpg', 'caption': 'Drum booth', 'alt': 'Drums'},
    {'filename': 'studio-7.jpg', 'caption': 'Lounge area', 'alt': 'Lounge'},
]
```

**Result:** Portfolio page shows 7 photos instead of 4!

---

### **Example 3: Start with Just 1 Testimonial**

```python
TESTIMONIALS = [
    {
        'text': 'Excellent work! Very professional.',
        'author': 'First Client',
        'role': 'Musician',
    },
]
```

**Result:** Shows just 1 testimonial. As you get more reviews, add them to the list!

---

## ✅ Complete Workflow

### **To Add a New Project:**

1. **Get YouTube video ID** from your project video
2. **Open:** `pelicanconf.py`
3. **Find:** `FEATURED_PROJECTS` (line 109)
4. **Add:**
   ```python
   {
       'title': 'Your Project',
       'type': 'Service Type',
       'artist': 'Artist/Client',
       'description': 'What you did...',
       'youtube_id': 'video_id_here',
   },
   ```
5. **Save** the file
6. **Rebuild:**
   ```bash
   pelican content -s publishconf.py
   git add .
   git commit -m "Add new project to portfolio"
   git push
   ```
7. **Done!** Live on Netlify in 3 minutes ✨

---

## 🧪 Testing Locally

```bash
# Build the site
pelican content

# Start local server
pelican --listen

# Visit http://localhost:8000/portfolio.html
# See your changes immediately!
```

---

## 🎨 Advanced: Conditional Display

You can even add logic! For example, only show projects with videos:

```python
# In portfolio.md
{% for project in FEATURED_PROJECTS %}
  {% if project.youtube_id %}
    <!-- Show project -->
  {% endif %}
{% endfor %}
```

Or show featured projects first:

```python
# In pelicanconf.py
{
    'title': 'My Best Work',
    'featured': True,  # Add this flag
    ...
}
```

---

## 📋 Quick Reference

| What to Add | Where | How |
|-------------|-------|-----|
| **New Project** | `pelicanconf.py` line 109 | Add dict to `FEATURED_PROJECTS` |
| **New Photo** | `pelicanconf.py` line 135 | Add dict to `STUDIO_PHOTOS` |
| **New Testimonial** | `pelicanconf.py` line 159 | Add dict to `TESTIMONIALS` |
| **Remove Item** | Same locations | Delete the dict entry |
| **Reorder Items** | Same locations | Change order in list |

---

## 💡 Benefits of This Approach

### **Before (Static HTML):**
- ❌ Copy-paste code for each project
- ❌ Risk of formatting errors
- ❌ Hard to maintain consistency
- ❌ Time-consuming updates

### **Now (Data-Driven):**
- ✅ Add data, not code
- ✅ Automatic formatting
- ✅ Always consistent
- ✅ 30-second updates

---

## 🎯 Summary

**Your Question:** Can we make portfolio dynamic (2 items = show 2, 3 items = show 3)?

**Answer:** YES! Now fully implemented!

**What's Dynamic:**
- ✅ Featured Projects (add/remove in `FEATURED_PROJECTS`)
- ✅ Studio Photos (add/remove in `STUDIO_PHOTOS`)
- ✅ Testimonials (add/remove in `TESTIMONIALS`)

**How to Update:**
1. Edit `pelicanconf.py` (one file!)
2. Add/remove items from the lists
3. Rebuild and push
4. Page adjusts automatically!

**This is exactly how professional CMS systems work!** 🚀

---

**You now have a scalable, maintainable, data-driven portfolio system!** 🎉
