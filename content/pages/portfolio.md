Title: Portfolio
Slug: portfolio
Template: portfolio

# Our Work

Check out some of our recent projects and client work. We're proud of the diverse range of audio we've produced.

---

## Featured Projects

{% for project in FEATURED_PROJECTS %}
### {{ project.title }}
**Type:** {{ project.type }}
**Artist/Client:** {{ project.artist }}

{{ project.description }}

**Watch on YouTube:**
<div class="video-container">
    <iframe width="100%" height="400" src="https://www.youtube.com/embed/{{ project.youtube_id }}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

---

{% endfor %}

## Studio Photos

{% for photo in STUDIO_PHOTOS %}
![{{ photo.alt }}](/images/{{ photo.filename }})
*{{ photo.caption }}*

{% endfor %}

---

## Client Testimonials

{% for testimonial in TESTIMONIALS %}
> "{{ testimonial.text }}"
> **- {{ testimonial.author }}, {{ testimonial.role }}**

{% endfor %}

---

## Want to Work With Us?

Let's create something amazing together!

[Get in Touch](/contact.html){: .btn .btn-primary}

---

<!--
Note: All portfolio content is managed in pelicanconf.py:
- Edit FEATURED_PROJECTS to add/remove projects (just change YouTube video IDs!)
- Edit STUDIO_PHOTOS to add/remove studio images (add images to content/images/ folder)
- Edit TESTIMONIALS to add/remove client testimonials
- Add as many as you want - the page adjusts automatically!
-->
