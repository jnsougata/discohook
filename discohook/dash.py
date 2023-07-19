from fastapi.responses import HTMLResponse


async def dashboard():
    return HTMLResponse(
        """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Discohook</title>
    <link rel="icon" href="https://filebox-1-q0603932.deta.app/embed/ffc197bb50206ac1" />
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@100;400;900&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@48,400,1,0" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/atom-one-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/highlight.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        :root {
            --black-main: #1d1b22;
            --black-secondary: #26262e;
        }
        body {
            font-family: system-ui, 'Prompt', sans-serif;
            background-color: var(--black-main);
        }
        main {
            width: 100vw;
            height: 100vh;
            height: 100dvh;
            color: white;
            padding: 10px;
            background-color: var(--black-main);
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
            overflow: auto;
        }
        main > header {
            width: 100%;
            height: max-content;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        main > header i {
            font-size: 20px;
            font-weight: 900;
            color: white;
            margin-left: 10px;
            cursor: pointer;
        }
        main > header > p {
            width: 100%;
            text-align: left;
        }
        main > .card {
            width: 100%;
            display: flex;
            color: white;
            padding: 0 20px;
            align-items: flex-end;
            justify-content: flex-end;
            height: max-content;
            margin-bottom: 40px;
            background-color: var(--black-secondary);
        }
        main > .card > pre {
            width: 100%;
            overflow: auto;
            height: max-content;
            background-color: transparent;
        }
        main > .card > pre > code {
            background-color: transparent;
        }
        main > .card > button {
            padding: 10px 15px;
            border: none;
            outline: none;
            color: white;
            cursor: pointer;
            font-size: 15px;
            background-color: rgb(247, 62, 62);
            margin-right: -20px;
        }
        dialog[open] {
            border: 0;
            width: 300px;
            height: max-content;
            background-color: var(--black-secondary);
            padding: 20px;
            border-radius: 10px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin: auto;
        }
        dialog::backdrop {
            background: rgba(0, 0, 0, 0.418);
        }
        dialog > input {
            width: 250px;
            border: none;
            outline: none;
            background-color: var(--black-main);
            color: white;
            font-size: 15px;
            text-align: center;
            padding: 10px;
            border-radius: 15px;
        }
        dialog > button {
            width: 30px;
            height: 30px;
            border: none;
            outline: none;
            background-color: rgb(36, 168, 87);
            color: white;
            font-size: 15px;
            border-radius: 50%;
            margin-top: 20px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <dialog>
        <p style="margin-bottom: 20px; color: #ccc">Login</p>
        <input id="password" type="password" placeholder="Enter your password" />
        <button id="login"><i class="fa-solid fa-check"></i></button>
    </dialog>
    <main>
        <header>
            <p>DISCOHOOK</p>
            <a href="https://github.com/jnsougata/discohook" target="_blank">
                <i class="fa-brands fa-github"></i>
            </a>
        </header>
    </main>
    <script>
        let main = document.querySelector("main");
        let dialog = document.querySelector("dialog");
        let login = document.querySelector("#login");
        let password = document.querySelector("#password");

        async function hashPassword(input) {
            const encoder = new TextEncoder();
            const data = encoder.encode(input);
            const buffer = await crypto.subtle.digest("SHA-256", data);
            const hashArray = Array.from(new Uint8Array(buffer));
            return hashArray.map(b => b.toString(16).padStart(2, "0")).join("");
        }

        function buildCommandElem(command, password) {
            let card = document.createElement("div");
            card.className = "card";
            let pre = document.createElement("pre");
            let code = document.createElement("code");
            code.innerHTML = JSON.stringify(command, null, 4);
            pre.appendChild(code);
            
            let del = document.createElement("button");
            del.innerHTML = `<i class="fas fa-trash"></i>`;
            del.addEventListener("click", async () => {
                const resp = await fetch(`/api/commands`, {
                    method: "DELETE",
                    body: JSON.stringify({
                        password: password,
                        id: command.id
                    })
                })
                if (resp.status === 204) {
                    card.remove();
                } else {
                    let data = await resp.json();
                    alert(data.error);
                }
            });
            card.appendChild(pre);
            card.appendChild(del);
            return card;
        }

        async function renderCommands(password) {
            dialog.close();
            const resp = await fetch(`/api/sync`, {
                    method: "POST",
                    body: JSON.stringify({
                        password: password
                    })
                }
            );
            let data = await resp.json();
            if (resp.status === 200) {
                data.forEach(command => {
                    main.appendChild(buildCommandElem(command, password));
                });
                hljs.highlightAll();
            } else {
                alert(`Discord Error: ${data.message} (code: ${data.code})`);
            }
        }

        login.addEventListener("click", async () => {
            let hashedPassword = await hashPassword(password.value);
            const resp = await fetch(`/api/verify`, {
                method: "POST",
                body: JSON.stringify({
                    password: hashedPassword
                })
            });
            let data = await resp.json();
            if (resp.status !== 200) {
                alert(data.error);
            } else {
                localStorage.setItem("password", hashedPassword);
                await renderCommands(hashedPassword);
            }
        });

        window.addEventListener("DOMContentLoaded", async () => {
            const savedPassword = localStorage.getItem("password");
            if (!savedPassword) {
                dialog.showModal();
                return;
            }
            const resp = await fetch(`/api/verify`, {
                method: "POST",
                body: JSON.stringify({
                    password: savedPassword
                })
            });
            if (resp.status !== 200) {
                dialog.showModal();
            } else {
                await renderCommands(savedPassword);
            }
        });
    </script>
</body>
</html>
        """,
        status_code=200
    )
