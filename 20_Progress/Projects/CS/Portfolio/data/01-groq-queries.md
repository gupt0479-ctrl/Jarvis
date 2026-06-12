---
tags: [portfolio, sanity, groq, queries]
---

# GROQ Queries Reference

> [[../INDEX|← Back to Index]] · [[../architecture/02-sanity-cms|Sanity CMS]]

All queries defined in `src/sanity/lib/queries.ts` (Community 15).

## Profile Queries (Community 62)

```groq
// PROFILE_QUERY — main profile
*[_type == "profile"][0]{
  firstName, lastName, headline, bio,
  avatar { asset->{ url } },
  socialLinks, skills, ...
}

// Get profile with full bio
*[_type == "profile"][0]{
  ...,
  longBio,
  highlights
}
```

## Experience Queries (Community 65)

```groq
// EXPERIENCE_QUERY — all work experience (newest first)
*[_type == "experience"] | order(startDate desc){
  _id, company, role, startDate, endDate,
  current, description, tags, category
}

// Get current position
*[_type == "experience" && current == true][0]{
  company, role, startDate
}

// EXPERIENCE_BY_ID_QUERY — single experience (used by chat tool)
*[_type == "experience" && _id == $id][0]{ ... }
```

## Project Queries (Community 43)

```groq
// PROJECTS_QUERY — all projects
*[_type == "project"] | order(order asc){
  _id, title, slug, description, techStack,
  liveUrl, githubUrl, featured, category, coverImage
}

// Featured projects only
*[_type == "project" && featured == true] | order(order asc)

// PROJECT_BY_SLUG_QUERY — single project
*[_type == "project" && slug.current == $slug][0]{ ... }

// Get projects by category
*[_type == "project" && category == "ai-ml"]{ ... }
```

## Skills Queries (Community 42)

```groq
// SKILLS_QUERY — all skills
*[_type == "skill"] | order(order asc){
  _id, name, category, proficiency, icon, featured
}

// Featured skills only
*[_type == "skill" && featured == true] | order(order asc){ ... }

// Skills by category
*[_type == "skill" && category == "frontend"] | order(name asc){ ... }

// Group skills by category
{ "frontend": *[_type == "skill" && category == "frontend"], ... }
```

## Education Queries

```groq
// EDUCATION_QUERY — newest first
*[_type == "education"] | order(endDate desc){
  _id, institution, degree, field, startDate, endDate, description
}
```

## Certifications Queries (Community 63)

```groq
// CERTS_SECTION_QUERY — all certs
*[_type == "certification"] | order(issueDate desc){
  _id, name, issuer, issueDate, expiryDate, credentialId, credentialUrl
}

// Active certifications (not expired)
*[_type == "certification" && (expiryDate == null || expiryDate > now())]{ ... }
```

## Achievements Queries (Community 64)

```groq
// ACHIEVEMENTS_SECTION_QUERY — all achievements
*[_type == "achievement"] | order(date desc){
  _id, title, description, date, featured, icon
}

// Featured achievements
*[_type == "achievement" && featured == true] | order(date desc){ ... }
```

## Blog Queries (Community 38)

```groq
// BLOG_SECTION_QUERY — all posts
*[_type == "blog"] | order(publishedAt desc){
  _id, title, slug, publishedAt, excerpt, category, tags, featured, coverImage
}

// Get blog post by slug
*[_type == "blog" && slug.current == $slug][0]{
  ...,
  content   // portable text
}

// Featured posts
*[_type == "blog" && featured == true] | order(publishedAt desc){ ... }

// Posts by category
*[_type == "blog" && category == "tutorial"] | order(publishedAt desc){ ... }

// Posts by tag
*[_type == "blog" && "React" in tags] | order(publishedAt desc){ ... }
```

## Site Settings Query (Community 62)

```groq
// SITE_SETTINGS_QUERY
*[_type == "siteSettings"][0]{
  siteTitle, siteDescription, email, resumeUrl, socialLinks
}
```

## Navigation Query

```groq
// NAVIGATION_QUERY
*[_type == "navigation"][0]{
  items[]{ label, href, external }
}
```

## Contact Queries (Community 51)

```groq
// All contact submissions (newest first)
*[_type == "contact"] | order(submittedAt desc){ ... }

// Unread contacts
*[_type == "contact" && status == "new"] | order(submittedAt desc){ ... }

// High priority
*[_type == "contact" && priority == "high"] | order(submittedAt desc){ ... }
```

## Chat Catalog Query

```groq
// CHAT_CATALOG_QUERY — full data for Orby's system prompt
// Fetches profile + all experiences + all projects + skills + education + certs + achievements
{ "profile": *[_type == "profile"][0]{...}, "experience": *[_type=="experience"]{...}, ... }
```

## Complex / Combined Queries (Community 50)

```groq
// Homepage data (everything you need for a homepage)
{
  "profile": *[_type == "profile"][0]{...},
  "featuredProjects": *[_type == "project" && featured == true]{...},
  "skills": *[_type == "skill" && featured == true]{...}
}

// About page data
{ "profile": ..., "education": ..., "achievements": ... }

// Portfolio page data
{ "projects": ..., "experience": ..., "skills": ... }
```

## Count & Statistics (Community 61)

```groq
// Count all documents
count(*)

// Count documents by type
count(*[_type == "project"])

// Count with filter
count(*[_type == "blog" && featured == true])
```

## Pro Tips (Community 56)

```groq
// Use projections to minimize payload:
*[_type == "project"]{ title, slug, description }   // only what you need

// Get image with metadata:
*[_type == "project"]{ coverImage{ asset->{ url, metadata } } }

// Reference resolution with ->:
*[_type == "blog"][0]{ author->{ name, avatar } }

// Count references:
count(*[_type == "blog" && featured == true])
```

## See Also
- [[00-sanity-schemas|Sanity Schemas]]
- [[../architecture/02-sanity-cms|Sanity CMS Layer]]
