import { defineConfig } from "vitepress";

export default defineConfig({
    base: "/discohook/",
    title: "discohook",
    description: "A discord interaction API wrapper for serverless applications.",
    cleanUrls: true,

    head: [
    [
        "link",
        {
            "rel": "icon",
            "href": "/logo.png"
        }
    ]
],

    themeConfig: {
        logo: "/logo.png",

        nav: [],

        editLink: {
            pattern: "",
        },

        sidebar: [
    {
        "text": "Introduction",
        "link": "/guide/0.1.dev0/introduction"
    },
    {
        "text": "Reference",
        "items": [
            {
                "text": "Adapter",
                "link": "/guide/0.1.dev0/adapter"
            },
            {
                "text": "Asset",
                "link": "/guide/0.1.dev0/asset"
            },
            {
                "text": "Attachment",
                "link": "/guide/0.1.dev0/attachment"
            },
            {
                "text": "Button",
                "link": "/guide/0.1.dev0/button"
            },
            {
                "text": "Channel",
                "link": "/guide/0.1.dev0/channel"
            },
            {
                "text": "Client",
                "link": "/guide/0.1.dev0/client"
            },
            {
                "text": "Command",
                "link": "/guide/0.1.dev0/command"
            },
            {
                "text": "Common",
                "link": "/guide/0.1.dev0/common"
            },
            {
                "text": "Components",
                "link": "/guide/0.1.dev0/components"
            },
            {
                "text": "Dashboard",
                "link": "/guide/0.1.dev0/dashboard"
            },
            {
                "text": "Emoji",
                "link": "/guide/0.1.dev0/emoji"
            },
            {
                "text": "Engine",
                "link": "/guide/0.1.dev0/engine"
            },
            {
                "text": "Enums",
                "link": "/guide/0.1.dev0/enums"
            },
            {
                "text": "Errors",
                "link": "/guide/0.1.dev0/errors"
            },
            {
                "text": "File",
                "link": "/guide/0.1.dev0/file"
            },
            {
                "text": "Guild",
                "link": "/guide/0.1.dev0/guild"
            },
            {
                "text": "Handler",
                "link": "/guide/0.1.dev0/handler"
            },
            {
                "text": "Help",
                "link": "/guide/0.1.dev0/help"
            },
            {
                "text": "Https",
                "link": "/guide/0.1.dev0/https"
            },
            {
                "text": "Interaction",
                "link": "/guide/0.1.dev0/interaction"
            },
            {
                "text": "Member",
                "link": "/guide/0.1.dev0/member"
            },
            {
                "text": "Message",
                "link": "/guide/0.1.dev0/message"
            },
            {
                "text": "Middleware",
                "link": "/guide/0.1.dev0/middleware"
            },
            {
                "text": "Modal",
                "link": "/guide/0.1.dev0/modal"
            },
            {
                "text": "Models",
                "link": "/guide/0.1.dev0/models"
            },
            {
                "text": "Option",
                "link": "/guide/0.1.dev0/option"
            },
            {
                "text": "Params",
                "link": "/guide/0.1.dev0/params"
            },
            {
                "text": "Permission",
                "link": "/guide/0.1.dev0/permission"
            },
            {
                "text": "Poll",
                "link": "/guide/0.1.dev0/poll"
            },
            {
                "text": "Ratelimit",
                "link": "/guide/0.1.dev0/ratelimit"
            },
            {
                "text": "Resolver",
                "link": "/guide/0.1.dev0/resolver"
            },
            {
                "text": "Role",
                "link": "/guide/0.1.dev0/role"
            },
            {
                "text": "Select",
                "link": "/guide/0.1.dev0/select"
            },
            {
                "text": "Thread",
                "link": "/guide/0.1.dev0/thread"
            },
            {
                "text": "User",
                "link": "/guide/0.1.dev0/user"
            },
            {
                "text": "Utils",
                "link": "/guide/0.1.dev0/utils"
            },
            {
                "text": "View",
                "link": "/guide/0.1.dev0/view"
            },
            {
                "text": "Webhook",
                "link": "/guide/0.1.dev0/webhook"
            }
        ]
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

        socialLinks: [],
    },
});
