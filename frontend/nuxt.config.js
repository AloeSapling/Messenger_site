// https://nuxt.com/docs/api/configuration/nuxt-config
import path from 'path'
import fs from 'fs'
export default defineNuxtConfig({
  devtools: {enabled: true},
  modules: ['@nuxtjs/tailwindcss'],
})