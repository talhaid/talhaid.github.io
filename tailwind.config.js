/** @type {import('tailwindcss').Config} */
module.exports = {
  // Explicit paths: a bare './**/*.html' would also walk node_modules.
  content: [
    './index.html',
    './about/*.html',
    './projects/*.html',
    './skills/*.html',
    './contact/*.html',
    './assets/js/**/*.js',
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      },
    },
  },
  plugins: [],
};
