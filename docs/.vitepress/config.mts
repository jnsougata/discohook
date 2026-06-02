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
        "text": "API Reference",
        "items": [
            {
                "text": "Adapter",
                "link": "/content/discohook_adapter"
            },
            {
                "text": "Asset",
                "link": "/content/discohook_asset"
            },
            {
                "text": "Attachment",
                "link": "/content/discohook_attachment"
            },
            {
                "text": "Button",
                "link": "/content/discohook_button"
            },
            {
                "text": "Channel",
                "link": "/content/discohook_channel"
            },
            {
                "text": "Client",
                "link": "/content/discohook_client"
            },
            {
                "text": "Command",
                "link": "/content/discohook_command"
            },
            {
                "text": "Common",
                "link": "/content/discohook_common"
            },
            {
                "text": "Components",
                "link": "/content/discohook_components"
            },
            {
                "text": "Dashboard",
                "link": "/content/discohook_dashboard"
            },
            {
                "text": "Embed",
                "link": "/content/discohook_embed"
            },
            {
                "text": "Emoji",
                "link": "/content/discohook_emoji"
            },
            {
                "text": "Engine",
                "link": "/content/discohook_engine"
            },
            {
                "text": "Enums",
                "link": "/content/discohook_enums"
            },
            {
                "text": "Errors",
                "link": "/content/discohook_errors"
            },
            {
                "text": "File",
                "link": "/content/discohook_file"
            },
            {
                "text": "Guild",
                "link": "/content/discohook_guild"
            },
            {
                "text": "Handler",
                "link": "/content/discohook_handler"
            },
            {
                "text": "Help",
                "link": "/content/discohook_help"
            },
            {
                "text": "Https",
                "link": "/content/discohook_https"
            },
            {
                "text": "Interaction",
                "link": "/content/discohook_interaction"
            },
            {
                "text": "Member",
                "link": "/content/discohook_member"
            },
            {
                "text": "Message",
                "link": "/content/discohook_message"
            },
            {
                "text": "Middleware",
                "link": "/content/discohook_middleware"
            },
            {
                "text": "Modal",
                "link": "/content/discohook_modal"
            },
            {
                "text": "Models",
                "link": "/content/discohook_models"
            },
            {
                "text": "Option",
                "link": "/content/discohook_option"
            },
            {
                "text": "Params",
                "link": "/content/discohook_params"
            },
            {
                "text": "Permission",
                "link": "/content/discohook_permission"
            },
            {
                "text": "Poll",
                "link": "/content/discohook_poll"
            },
            {
                "text": "Ratelimit",
                "link": "/content/discohook_ratelimit"
            },
            {
                "text": "Resolver",
                "link": "/content/discohook_resolver"
            },
            {
                "text": "Role",
                "link": "/content/discohook_role"
            },
            {
                "text": "Select",
                "link": "/content/discohook_select"
            },
            {
                "text": "Thread",
                "link": "/content/discohook_thread"
            },
            {
                "text": "User",
                "link": "/content/discohook_user"
            },
            {
                "text": "Utils",
                "link": "/content/discohook_utils"
            },
            {
                "text": "View",
                "link": "/content/discohook_view"
            },
            {
                "text": "Webhook",
                "link": "/content/discohook_webhook"
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
