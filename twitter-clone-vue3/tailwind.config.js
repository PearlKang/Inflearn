/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  content: [],
  theme: {
    extend: {
      colors: {
        primary: "#1DA1F2",
        dark: "#1A91DA",
        light: "#A5D0F5",
        lighter: "#D4E5F4",
      },
    },
  },
  plugins: [],
};
