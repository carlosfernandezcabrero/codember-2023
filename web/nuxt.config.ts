// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: false },
  css: [
    '~/assets/css/global.css',
    'vue-toast-notification/dist/theme-default.css'
  ],
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {}
    }
  },
  runtimeConfig: {
    public: {
      apiUrl: 'http://localhost:5000/api/v1'
    }
  }
})
