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
                background-color: rgb(84, 84, 235);
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
                color: rgb(84, 84, 235);
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
                color: rgb(84, 84, 235);
            }
            table {
                width: 100%;
                height: auto;
                background-color: var(--black-main);
                margin-top: 50px;
            }
            table > thead > tr > th {
                background-color: var(--black-secondary);
                color: white;
                padding: 10px;
                font-size: 15px;
                font-weight: 500;
                text-align: left;
                top: 0;
                position: sticky;
            }
            table > tbody > tr > td {
                background-color: var(--black-secondary);
                color: white;
                padding: 10px;
                font-size: 15px;
                font-weight: 500;
                text-align: left;
            }

            td > button {
                background-color: red;
                border: none;
                color: white;
                font-size: 15px;
                cursor: pointer;
                border-radius: 5px;
                transition: 0.2s;
                margin-right: 5px;
                padding: 8px 10px;
            }
                      
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <h1>commands</h1>
                <button id="reload"><i class="fas fa-sync"></i></button>
            </header>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Description</th>
                        <th>Type</th>
                        <th>Options</th>
                    </tr>
                </thead>
                <tbody id="commands">
                </tbody> 
            </table>
        </div>
        <script>
            let commands = document.querySelector("#commands");    
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
                let command = document.createElement("tr");
                command.id = data.id;
                if (!data.description) {
                    data.description = "n/a";
                }
                command.innerHTML = `
                    <td>${data.id}</td>
                    <td>${data.name}</td>
                    <td>${data.description}</td>
                    <td>${data.type}</td>
                    <td>
                        <button id="copy-${data.id}" style="background-color: rgb(42, 155, 42);">Copy ID</button>
                        <button id="del-${data.id}">Delete</button>
                    </td>
                `;
                commands.appendChild(command);
                document.getElementById(`copy-${data.id}`).addEventListener("click", () => {
                    navigator.clipboard.writeText(data.id);
                });
                document.getElementById(`del-${data.id}`).addEventListener("click", () => {
                    fetch(`/dh/delete/${data.id}`)
                    .then((res) => {
                        if (res.status == 204) {
                            document.getElementById(data.id).remove();
                        } else {
                            alert(JSON.stringify(res.json()));
                        }
                    });
                });
            }
        </script>
    </body>
</html>
    """
    return HTMLResponse(content=content, status_code=200)