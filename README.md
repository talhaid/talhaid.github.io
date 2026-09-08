# talhaid.tech – Personal Portfolio Website

Welcome to my personal portfolio website.
I’m a senior Information Systems Engineering student focused on analytics, data science, distributed systems, and AI/ML.

This website showcases my projects, skills, and contact information.

## 🔗 Live Website

[Visit talhaid.tech](https://talhaid.tech)

## 🛠️ Built With

- HTML5 & CSS3
- Tailwind CSS (compiled locally — no CDN at runtime)
- Self-hosted Inter webfont (no third-party font requests)
- GitHub Pages (for deployment)

## 🚀 Local Development

The stylesheet is built from `src/css/tailwind.css` into `assets/css/style.css`.
Rebuild it whenever you add or change classes in the HTML:

```bash
npm install     # once
npm run build   # produce assets/css/style.css (minified)
npm run watch   # rebuild automatically while editing
```

`assets/css/style.css` is committed, so GitHub Pages serves the site without a build step.

## 🔒 Security & Privacy

- Every page ships a strict `Content-Security-Policy` meta tag (`script-src 'self'`, no inline scripts)
- `referrer` policy set to `strict-origin-when-cross-origin`
- All `target="_blank"` links carry `rel="noopener noreferrer"`
- No third-party requests: no CDN, no analytics, no external fonts — nothing leaves the visitor's browser

## 📂 Sections

- **Home:** Hero section, introduction
- **About:** Background, skills, and education
- **Projects:** Key data-related projects
- **Skills:** Tools & technologies
- **Contact:** Ways to reach out

## 📫 Contact

Feel free to connect with me on:

- [GitHub](https://github.com/talhaid)
- [LinkedIn](https://linkedin.com/in/talhaid)
- [Portfolio Website](https://talhaid.tech)
