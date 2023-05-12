from fastapi.responses import HTMLResponse


def dashboard():
    content = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>discohook | sync</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@100;400;900&display=swap" rel="stylesheet" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" />
        <link rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@48,400,1,0" />
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            :root {
                --blue-main: #537ff7;
                --black-main: #1d1b22;
                --black-secondary: #26262e;
            }
            body {
                width: 100vw;
                height: 100vh;
                height: 100dvh;
                overflow: hidden;
                font-family: 'Prompt', sans-serif;
                background-color: var(--black-main);
            }
            .container {
                padding: 10px;
                width: 100%;
                height: 100%;
                background-color: var(--black-main);
            }
            .container > header {
                top: 0;
                width: 100%;
                height: 50px;
                padding: 10px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                background-color: var(--black-secondary);
                border-bottom: 1px solid var(--black-main);
            }
            .container > header > button {
                border: none;
                font-size: 20px;
                cursor: pointer;
                border-radius: 50%;
                transition: 0.2s;
                color: white;
                background-color: rgb(39, 113, 245);
            }
            .container > header > button > i {
                font-size: 15px;
                padding: 10px;
                transition: 0.2s;
            }
            .container > header > h1 {
                font-size: 20px;
                font-weight: 500;
                color: white;
                padding: 0 10px;
                border-radius: 5px;
                transition: 0.2s;
            }
            .container > ul {
                width: 100%;
                height: 100%;
                display: flex;
                align-items: center;
                flex-direction: column;
                justify-content: flex-start;
                background-color: var(--black-main);
            }
            .container > ul > li {
                width: 100%;
                height: 50px;
                padding: 10px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                background-color: var(--black-secondary);
                border-bottom: 1px solid var(--black-main);
            }
            .container > ul > li > p {
                width: 100%;
                font-size: 15px;
                color: white;
                padding: 0 10px;
                border-radius: 5px;
                transition: 0.2s;
                text-align: left;
                white-space: nowrap;
            }
            .container > ul > li > p >  i {
                font-size: 12px;
                padding: 12px;
                transition: 0.2s;
                border-radius: 50%;
                color: var(--blue-main);
                cursor: pointer;
                background-color: var(--black-main);
            }
            @media screen and (max-width: 600px) {
                .container > ul {
                    overflow: auto;
                }
                .container > ul > li > p {
                    font-size: 10px;
                    width: 100px;
                    flex-shrink: 0;
                }
                .container > ul > li > p >  i {
                    font-size: 10px;
                    padding: 10px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>Commands</h1>
                <button id="reload"><i class="fas fa-sync"></i></button>
            </header>
            <ul id="commands">
                <li>
                    <p>Name</p>
                    <p>Id</p>
                    <p>Description</p>
                    <p>Type</p>
                    <p style="text-align: center">Options</p>
                </li>
            </ul>
        </div>
        <script>
            let commands = document.querySelector("#commands");
            let token = window.location.href.split("/").pop();

            let reload = document.getElementById("reload");
            reload.addEventListener("click", () => {
                window.location.reload();
            });

            window.addEventListener("DOMContentLoaded", async () => {
                resp = await fetch(`/api/sync/${token}`)
                if (resp.status === 200) {
                    data = await resp.json();
                    data.forEach(element => {
                        appendCommand(element);
                    });
                } else {
                    msg = await resp.json();
                    alert(msg.error);
                }
            });

            function appendCommand(data) {
                let li = document.createElement("li");
                li.id = data.id;
                if (!data.description) {
                    data.description = "null";
                }
                let name = document.createElement("p");
                name.innerText = data.name;
                let id = document.createElement("p");
                id.innerText = data.id;
                let description = document.createElement("p");
                description.innerText = data.description;
                let type = document.createElement("p");
                type.innerText = data.type;
                let options = document.createElement("p");
                options.style.textAlign = "center";
                let del = document.createElement("i");
                del.className = "fas fa-trash";
                del.style.marginLeft = "2px";
                del.addEventListener("click", async () => {
                    resp = await fetch(`/api/commands/${data.id}/${token}`, {method: "DELETE"})
                    if (resp.status === 204) {
                        document.getElementById(data.id).remove();
                    } else {
                        msg = await resp.json();
                        alert(msg.error);
                    }
                });
                options.appendChild(del);
                li.appendChild(name);
                li.appendChild(id);
                li.appendChild(description);
                li.appendChild(type);
                li.appendChild(options);
                commands.appendChild(li);
            }
        </script>
    </body>
</html>
    """
    return HTMLResponse(content=content, status_code=200)
