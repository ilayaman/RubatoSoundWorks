# How to Comment Out Content in Pelican

## 🔧 Comment Syntax Reference

When you want to hide content from appearing on the website (but keep it in your source files for reference), use comments.

---

## 📝 **In Markdown Files (.md)**

### **HTML Comments (Recommended):**

```markdown
<!-- This is a comment - won't show on website -->

<!-- 
Multi-line comment
Can span multiple lines
Won't appear on site
-->
```

### **Examples:**

**Hide a paragraph:**
```markdown
<!-- This paragraph won't appear on the website -->
```

**Hide an image:**
```markdown
<!-- ![Studio Photo](/images/studio-1.jpg) -->
```

**Hide a section:**
```markdown
<!-- 
## This Section is Hidden

All of this content
won't appear on the site
until you remove the comment tags
-->
```

**Hide a note:**
```markdown
<!-- **Note:** This is for internal reference only -->
```

---

## 🐍 **In Python Config (pelicanconf.py)**

### **Python Comments:**

```python
# Single line comment

"""
Multi-line comment
(docstring)
"""

# Comment out a variable:
# EMAIL = 'old@email.com'  # This won't be used
EMAIL = 'new@email.com'    # This will be used
```

### **Example: Temporarily Disable a Project**

```python
FEATURED_PROJECTS = [
    {
        'title': 'Active Project',
        'youtube_id': 'abc123',
        # ... rest of the config
    },
    # Temporarily hidden - uncomment to show again
    # {
    #     'title': 'Hidden Project',
    #     'youtube_id': 'xyz789',
    #     # ... rest of the config
    # },
]
```

---

## 🎨 **In CSS Files (.css)**

```css
/* Single line comment */

/*
Multi-line comment
Can span multiple lines
*/

/* Temporarily disable a style rule: */
/*
.btn-primary {
    background: red;
}
*/
```

---

## 📄 **In HTML Templates (.html)**

```html
<!-- HTML comment -->

<!-- 
Multi-line HTML comment
Won't appear in source or rendered page
-->

<!-- Temporarily hide an element:
<div class="section">
    This won't render
</div>
-->
```

---

## ⚡ **Jinja2 Comments (In Templates)**

For content that uses Jinja2 syntax:

```jinja2
{# This is a Jinja2 comment - won't appear anywhere #}

{#
Multi-line Jinja2 comment
Completely removed during rendering
#}

{# Temporarily disable a loop:
{% for project in FEATURED_PROJECTS %}
    {{ project.title }}
{% endfor %}
#}
```

---

## 🎯 **Practical Examples**

### **1. Hide Developer Notes in Markdown:**

```markdown
# Contact Us

Get in touch with us today!

<!-- 
TODO: Add office hours once confirmed
TODO: Update phone number after porting
-->

📧 Email: {{ EMAIL }}
```

### **2. Temporarily Remove a Service:**

```python
# In pelicanconf.py
SERVICES = [
    {
        'name': 'Mixing and Mastering',
        'icon': '🎚️',
        'description': '...',
    },
    # Temporarily disabled - uncomment when ready
    # {
    #     'name': 'Podcast Editing',
    #     'icon': '🎙️',
    #     'description': '...',
    # },
]
```

### **3. Hide a Testimonial:**

```python
TESTIMONIALS = [
    {
        'text': 'Great service!',
        'author': 'John Doe',
        'role': 'Artist',
    },
    # Waiting for approval - hide for now
    # {
    #     'text': 'Pending testimonial...',
    #     'author': 'Jane Smith',
    #     'role': 'Producer',
    # },
]
```

### **4. Hide Section in Markdown:**

```markdown
## Client Testimonials

<!-- Coming soon! Waiting for client approvals
{% for testimonial in TESTIMONIALS %}
> "{{ testimonial.text }}"
{% endfor %}
-->

We'll be adding client testimonials soon!
```

---

## ✅ **Best Practices**

### **Do:**
- ✅ Use comments for temporary notes
- ✅ Use comments to disable content temporarily
- ✅ Leave helpful context in comments
- ✅ Use comments for TODOs

### **Don't:**
- ❌ Leave sensitive information in comments (passwords, API keys)
- ❌ Commit commented-out code long-term (clean it up!)
- ❌ Use comments instead of deleting (if you won't use it, delete it!)

---

## 🔍 **Comment vs Delete**

### **Use Comments When:**
- Testing changes (want to easily revert)
- Temporarily disabling a feature
- Leaving notes for yourself/team
- Planning future additions

### **Delete When:**
- Content is permanently removed
- Old code no longer needed
- Cleaning up before deployment

**Remember:** Git tracks all changes, so you can always recover deleted content from history!

---

## 🚀 **Quick Reference**

| File Type | Comment Syntax | Example |
|-----------|----------------|---------|
| **Markdown (.md)** | `<!-- comment -->` | `<!-- Hidden text -->` |
| **Python (.py)** | `# comment` | `# This is a note` |
| **CSS (.css)** | `/* comment */` | `/* Disabled style */` |
| **HTML (.html)** | `<!-- comment -->` | `<!-- Hidden div -->` |
| **Jinja2 (templates)** | `{# comment #}` | `{# Internal note #}` |

---

## 📋 **Common Use Cases**

### **1. Hide "Under Construction" Content:**
```markdown
## Portfolio

Check out our work!

<!-- 
Projects coming soon!
Currently updating portfolio with new work.
-->
```

### **2. Prepare Future Content:**
```python
# In pelicanconf.py
SERVICES = [
    {'name': 'Mixing', ...},     # Live
    {'name': 'Recording', ...},  # Live
    # {'name': 'Mastering', ...},  # Launch next month
]
```

### **3. A/B Test Descriptions:**
```markdown
Our professional music production services...

<!-- Alternative description (testing):
World-class audio production for artists and filmmakers...
-->
```

---

## ✨ **Your Recent Changes**

I just commented out these notes for you:

**1. In `contact.md`:**
```markdown
<!-- Note: Contact details are configured in pelicanconf.py. -->
```

**2. In `portfolio.md`:**
```markdown
<!-- 
Note: All portfolio content is managed in pelicanconf.py
-->
```

These notes won't appear on the website anymore, but you can still see them in the source files!

---

## 🔄 **To Uncomment (Show Again):**

Just remove the comment tags:

**Before (hidden):**
```markdown
<!-- This is hidden -->
```

**After (visible):**
```markdown
This is hidden
```

---

**Pro Tip:** Use comments liberally during development, then clean them up before major releases! 🎯
