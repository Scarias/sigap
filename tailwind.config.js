/** @type {import('tailwindcss').Config} */

export default {
  content: [
    './src/pages/**/*.{html,js,jsx,astro}',
    './src/components/**/*.{html,js,jsx,astro}',
  ],
  theme: {
    extend: {
      colors: {
        dark: {
          "primary": "#fef08a",
          "secondary": "#0284c7",
          "accent": "#f43f5e",
          "neutral": "#2a323c",
          "base-100": "#1d232a",
          "info": "#0d9488",
          "success": "#22c55e",
          "warning": "#f59e0b",
          "error": "#9f1239",
        },
      }
    },
  },
  plugins: [],
}
