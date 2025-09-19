import { defineConfig } from "vitepress";

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base: "/",
  title: "Discohook",
  description: "A discord interaction API wrapper for serverless applications.",
  cleanUrls: true,
  head: [["link", { rel: "icon", href: "/favicon.png" }]],
  themeConfig: {
    logo: "/favicon.png",
    nav: [{ text: "Docs", link: "/content/getting-started" }],
    editLink: {
      pattern: "https://github.com/jnsougata/discohook/tree/vitepress/docs/:path",
    },
    sidebar: [
      {
        text: "Introduction",
        items: [{ text: "Getting Started", link: "/content/getting-started" }],
      },
      {
        text: "Concepts",
        items: [
          { text: "Client", link: "/content/client" }
        ],
      }
    ],
    search: {
      provider: "local",
      options: {
        _render: (src, env, md) => {
          if (env.relativePath.startsWith("docs")) {
            return "";
          }

          return md.render(src, env);
        },
      },
    },
    socialLinks: [
      { icon: "pypi", link: "https://pypi.org/project/discohook/" },
      { icon: "github", link: "https://github.com/jnsougata/discohook" },
    ],
  },
});