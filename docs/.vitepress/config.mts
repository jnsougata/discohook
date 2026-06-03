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
            "href": "/favicon.png"
        }
    ]
],

    themeConfig: {
        logo: "/favicon.png",

        nav: [],

        editLink: {
            pattern: "",
        },

        sidebar: [
    {
        "text": "Introduction",
        "items": [
            {
                "text": "discohook",
                "link": "/content/discohook"
            }
        ]
    },
    {
        "text": "Reference",
        "items": [
            {
                "text": "Adapter",
                "link": "/content/adapter"
            },
            {
                "text": "Asset",
                "link": "/content/asset"
            },
            {
                "text": "Attachment",
                "link": "/content/attachment"
            },
            {
                "text": "Button",
                "link": "/content/button"
            },
            {
                "text": "Channel",
                "link": "/content/channel"
            },
            {
                "text": "Client",
                "link": "/content/client"
            },
            {
                "text": "Command",
                "link": "/content/command"
            },
            {
                "text": "Common",
                "link": "/content/common"
            },
            {
                "text": "Components",
                "link": "/content/components"
            },
            {
                "text": "Dashboard",
                "link": "/content/dashboard"
            },
            {
                "text": "Emoji",
                "link": "/content/emoji"
            },
            {
                "text": "Engine",
                "link": "/content/engine"
            },
            {
                "text": "Enums",
                "link": "/content/enums"
            },
            {
                "text": "Errors",
                "link": "/content/errors"
            },
            {
                "text": "File",
                "link": "/content/file"
            },
            {
                "text": "Guild",
                "link": "/content/guild"
            },
            {
                "text": "Handler",
                "link": "/content/handler"
            },
            {
                "text": "Help",
                "link": "/content/help"
            },
            {
                "text": "Https",
                "link": "/content/https"
            },
            {
                "text": "Interaction",
                "link": "/content/interaction"
            },
            {
                "text": "Member",
                "link": "/content/member"
            },
            {
                "text": "Message",
                "link": "/content/message"
            },
            {
                "text": "Middleware",
                "link": "/content/middleware"
            },
            {
                "text": "Modal",
                "link": "/content/modal"
            },
            {
                "text": "Models",
                "link": "/content/models"
            },
            {
                "text": "Option",
                "link": "/content/option"
            },
            {
                "text": "Params",
                "link": "/content/params"
            },
            {
                "text": "Permission",
                "link": "/content/permission"
            },
            {
                "text": "Poll",
                "link": "/content/poll"
            },
            {
                "text": "Ratelimit",
                "link": "/content/ratelimit"
            },
            {
                "text": "Resolver",
                "link": "/content/resolver"
            },
            {
                "text": "Role",
                "link": "/content/role"
            },
            {
                "text": "Select",
                "link": "/content/select"
            },
            {
                "text": "Thread",
                "link": "/content/thread"
            },
            {
                "text": "User",
                "link": "/content/user"
            },
            {
                "text": "Utils",
                "link": "/content/utils"
            },
            {
                "text": "View",
                "link": "/content/view"
            },
            {
                "text": "Webhook",
                "link": "/content/webhook"
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
