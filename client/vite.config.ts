import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';
import fs from 'fs';

export default defineConfig({
  plugins: [sveltekit()],
  build: { target: ['chrome100', 'chrome103'] },
  server: {
    https: {
      key: fs.readFileSync('../cert/certificate.key'),
      cert: fs.readFileSync('../cert/certificate.pem'),
    }
  },
});
