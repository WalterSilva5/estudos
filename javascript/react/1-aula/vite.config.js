import {
  defineConfig
} from 'vite'
import reactRefresh from '@vitejs/plugin-react-refresh'
import react from "vite-preset-react";

// https://vitejs.dev/config/
export default defineConfig({
  esbuild: {
    jsxInject: `import React from 'react'`
  },
  plugins: [react({ removeDevtoolsInProd: true, injectReact: true })]
})