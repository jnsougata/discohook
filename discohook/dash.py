from fastapi import Request
from fastapi.responses import HTMLResponse


async def dashboard(request: Request):
    content = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <title>discohook | sync</title>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="icon" href="../assets/icon.png" type="image/x-icon">

        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
        <link href="https://fonts.googleapis.com/css2?family=Prompt:wght@100;400;900&display=swap" rel="stylesheet" />
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" />
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@48,400,1,0" />
        <style>
            * {
                margin: 0;
                padding: 0;
            }
            :root {
                --black-main: #1d1b22;
                --black-secondary: #26262e;
            }
            body {
                font-family: 'Prompt', sans-serif;
                overflow: hidden;
                height: 100vh;
                background-color: var(--black-main);
            }
            .container {
                width: 100%;
                height: 100%;
                background-color: var(--black-main);
                overflow: hidden;
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
                align-items: center;
            }
            .container > header {
                top: 0;
                position: fixed;
                background-color: var(--black-secondary);
                color: white;
                padding: 10px;
                width: 100%;
                height: 30px;
                display: flex;
                justify-content: space-between;
                align-items: center;
                z-index: 100 !important;
                box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.5);
            }
            .container > header > button {
                background-color: transparent;
                border: none;
                color: black;
                font-size: 20px;
                cursor: pointer;
                border-radius: 5px;
                transition: 0.2s;
                margin-right: 5px;
            }
            .container > header > button > i {
                font-size: 15px;
                padding: 10px;
                border-radius: 5px;
                transition: 0.2s;
                background-color: whitesmoke;
            }
            .container > header > h1 {
                font-size: 20px;
                font-weight: 500;
                margin-left: 10px;
                background-color: whitesmoke;
                padding: 0 10px;
                border-radius: 5px;
                transition: 0.2s;
                color: rgb(116, 114, 114);
            }
            .container > .commands {
                width: 100%;
                height: 100%;
                display: flex;
                flex-direction: column;
                justify-content: flex-start;
                align-items: center;
                margin-top: 50px;
                background-color: var(--black-secondary);
            }
            .container > .commands > .command {
                width: 100%;
                height: 30px;
                display: flex;
                flex-direction: row;
                justify-content: flex-start;
                align-items: center;
                padding: 10px;
                margin-bottom: 10px;
                background-color: var(--black-main);
                box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.5);
            }
            .container > .commands > .command > span {
                max-width: 250px;
                text-align: center;
                font-size: 15px;
                font-weight: 500;
                color: white;
                margin-left: 10px;
                padding: 5px 10px;
                border-radius: 5px;
                background-color: rgba(0, 0, 255, 0.575);
                text-overflow: ellipsis;
                overflow: hidden;
                white-space: nowrap;
                flex-shrink: 0;
            }
            .container > .commands > .command > .options {
                width: 100%;
                display: flex;
                flex-direction: row;
                justify-content: flex-end;
                align-items: center;
                margin-left: 10px;
                margin-right: 10px;
            }
            .container > .commands > .command >.options > button {
                background-color: transparent;
                border: none;
                color: white;
                font-size: 15px;
                cursor: pointer;
                transition: 0.2s;
                margin-left: 10px;
                background-color: rgba(29, 172, 89, 0.753);
                padding: 8px 10px;
                border-radius: 5px;
                transition: 0.2s;
                outline: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>commands</h1>
                <button id="reload"><i class="fas fa-sync"></i></button>
            </header>
            <div class="commands">
            </div>
        </div>
        <script>
            let commands = document.querySelector(".commands");    
            let token = window.location.href.split("/").pop();
            let reload = document.getElementById("reload");
            reload.addEventListener("click", () => {
                window.location.reload();
            });
            window.onload = () => {
                fetch(`/dh/sync/${token}`)
                .then((res) => {
                    if (res.status == 200) {
                        return res.json();
                    } else {
                        alert(JSON.stringify(res.json()));
                        return {};
                    }
                })
                .then((data) => {
                    data.forEach(element => {
                        appendCommand(element);
                    });
                });
            }

            function appendCommand(data) {
                let command = document.createElement("div");
                command.classList.add("command");
                let idSpan = document.createElement("span");
                idSpan.innerText = data.id;
                let nameSpan = document.createElement("span");
                nameSpan.innerText = data.name;
                let descriptionSpan = document.createElement("span");
                descriptionSpan.innerText = data.description;
                let options = document.createElement("div");
                options.classList.add("options");
                let copyId = document.createElement("button");
                copyId.innerText = "Copy Id";
                copyId.addEventListener("click", () => {
                    navigator.clipboard.writeText(data.id);
                });
                let deleteCommand = document.createElement("button");
                deleteCommand.innerText = "Delete";
                deleteCommand.style.backgroundColor = "rgba(255, 0, 0, 0.514)";
                deleteCommand.addEventListener("click", () => {
                    fetch(`/dh/delete/${data.id}`)
                        .then((res) => {
                            if (res.status == 204) {
                                command.remove();
                            } else {
                                alert(JSON.stringify(res.json()));
                            }
                        });
                });
                options.appendChild(copyId);
                options.appendChild(deleteCommand);
                command.appendChild(idSpan);
                command.appendChild(nameSpan);
                if (data.description) {
                    command.appendChild(descriptionSpan);
                }
                command.appendChild(options);
                commands.appendChild(command);
            }
        </script>
    </body>
</html>
    """
    return HTMLResponse(content=content, status_code=200)