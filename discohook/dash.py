from starlette.responses import HTMLResponse


async def dashboard(_):
    return HTMLResponse(
        """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>discohook</title>
    <link rel="icon" href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAEYUlEQVR4AexWTWwbVRD+ZteO1AtCBChSJcgBWpygNiiKTZEqoYbY5YjS9AAip4aUv1Q04pALBy45oLZqoNA04UIFh6SII7EDFRJS02wVlT/HpHCIqh6gEIS4oCbeHeZb/2SbuLJDhXrJar/deTPfzM57M37PDu7ytZXA1grUXYFkOj/ZKFKZ/PlkpvCJ4Xgqs/BSquuH7fV6vG4CItLbKADpEegLhmMAPkbMvZ5KL0x2pBcft3HNu24CNb0aV8Yg6HXF/+6p7gKT2uBZN4G5bKtEAZXRaBQFrqjIES2u7Cr+kWgiEGCnih6hjVwBmtTR46l04RTHUdRNIEoOZyE6GOoU/wQIXvayiQ5vOjHmfdV+dX5eVom5mdafvem2MdosiX4YN/Qx3zBGOCg9qgkku/O91jiatKYrmQDK1FXAWYQ2C2gzzFzOPjF++pnft5/uWj74XvdybxQfPvtXD21etnWC3EoSgaMjHenvqz1RTSAM3OBDBYNetu2b0eeW70E8NgsHUxZoMopA/PO0kUNuIMFRhmc5XLjvUCYcPkK4/nVVnQJkFtVLZkOdYqaisiW9Ykv7EcfOqrwLaAvl2tCWWMgBLmfbJtT6hTwRPP90+pcHKVcT8KZ3z3q5tkNervUkDQRlz3TWyec4DiE6Boi+n17uFtF+2GWBr9nMDgVACMrUmQlqHHJhPhAxX9glMV9WMibY4vFZBwppr1DElwtcVigmTCcGM+PwqzPNU2+UQRmCw6ENJhmXPuLrBZQvcwpjVlegrA9fyfTCm2zACmxj6QkN9ij+mVhyV2XYvvywDW1eMv56rrlaIuoI6lRlnDK59KEvxyUED/FdMwGr616J7IBGfMRwh7cVqEaE2yRQg1lWxe4rtPhxHVHgGlVarTFHa2Ddoz3ix2WEvmsM/Eq5ZgJsvFt2P6CPZEJd3T/4RfPfVtlbavxBZB+gvL5H6KOu7GcMQiDf8l0zARqicLUpa2UphjqVAZOlVGNUa2wrUt0HKAuwrkds91A1X0bRYikm0FACF3OP3lDF53QV4MnOTJ6zRxDHW4As4baXLBXjahyAPmK+pDIWY1JuKAESffhvK+QmZUedU8nM4j4uK1aLex11D1qLhXtA5U0dbeQkM/l9jvnQV4GbjEWZaDiB+dzunyzIMJ2s/ttE/WxnptD/2tcP/PbKl/d+VtkDKm/qaOvM/NgvKln6hL7qDjNWKNuj4QSMi0u5XSdROY4F2xzoWfv3M588UBhIdhV2dnRonEh1LzyWPJAfoM2Bc3bt4zLqMQaDlbGpBOgzl0sctRoe41JyzLqK6hmJ6WLs/sIKYZ111WZ9hjZyjLsigQzRl+MoNp0AnT07L3wttocHFbT066BhI4qwA864ey7NJE5sNMNyraVtQMc6enZQuVrcYfQ+hZxQ6Kdl8GN9rjbtmDMOucapef+nFYhGupjbc8M2rXNeNjFk5/6LZQxRV/mpRfnr5TtOYH3AzY63EvjfV6BeSf4FAAD///CCa9gAAAAGSURBVAMAqDwxXy5FDacAAAAASUVORK5CYII=" />
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@100;400;600;700;900&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css" />
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/styles/atom-one-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.4.0/highlight.min.js"></script>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; border-radius: 0 !important; }
        html, body { height: 100%; }
        body { font-family: 'Inter', system-ui, sans-serif; background: #000; color: #fff; display: flex; flex-direction: column; }
        main { flex: 1; }
        ::-webkit-scrollbar { width: 8px; height: 8px; }
        ::-webkit-scrollbar-track { background: #0b0b0b; }
        ::-webkit-scrollbar-thumb { background: #444; }
        ::-webkit-scrollbar-thumb:hover { background: #666; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
        .fade-in { animation: fadeIn 0.25s ease-out; }
        @keyframes slideDown { from { opacity: 0; transform: translateY(-12px); } to { opacity: 1; transform: translateY(0); } }
        .slide-down { animation: slideDown 0.3s ease-out; }
        .card-bg { background: #0d0d0d; border: 1px solid #222; color: #fff; }
        dialog[open] { background: #0a0a0a; border: 1px solid #222; box-shadow: none; position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); max-width: 80%; width: 500px;}
        dialog::backdrop { background: rgba(0,0,0,0.85); }
        .hljs, pre { background-color: transparent !important; }
        .btn-primary { background: #fff; color: #000; border: 1px solid #ddd; }
        .btn-primary:hover { filter: brightness(0.95); }
        .btn-ghost { background: transparent; color: #fff; border: 1px solid #222; }
        .gradient-text { color: #fff; }
        .btn-hover { transition: all 0.18s ease; }
        .btn-hover:hover { transform: translateY(-2px); }
        .card-hover { transition: all 0.18s ease; }
        .card-hover:hover { transform: translateY(-2px); box-shadow: 0 8px 20px rgba(0,0,0,0.5); }
        input { background: #0b0b0b; color: #fff; border: 1px solid #262626; padding: 0.75rem 1rem; outline: none; }
        input::placeholder { color: #8a8a8a; }
        input:focus { border-color: #444; }
        @keyframes fadeOut { from { opacity: 1; transform: scale(1); } to { opacity: 0; transform: scale(0.98); } }
    </style>
</head>
<body>
    <dialog class="p-8 fade-in">
        <div class="text-center">
            <div class="mb-6">
                <i class="fa-solid fa-lock text-4xl text-white mb-4 block"></i>
                <h2 class="text-2xl font-bold text-white mb-2">Welcome Back</h2>
                <p class="text-gray-400 text-sm">Enter your password to continue</p>
            </div>
            <input id="password" type="password" placeholder="Enter your password" class="w-full p-3 text-white" />
            <button id="login" class="mt-6 w-full py-3 btn-primary font-semibold btn-hover flex items-center justify-center gap-2">
                <i class="fa-solid fa-arrow-right"></i>
                <span>Login</span>
            </button>
        </div>
    </dialog>

    <main class="p-4 md:p-8">
        <div class="max-w-7xl mx-auto">
            <header class="mb-8 slide-down">
                <div class="card-bg p-6">
                    <div class="flex items-center justify-between">
                        <div class="flex items-center gap-3">
                            <div class="w-12 h-12 bg-black flex items-center justify-center">
                                <i class="fa-solid fa-compass text-white text-xl"></i>
                            </div>
                            <div>
                                <h1 class="text-2xl font-bold text-white">DISCOHOOK</h1>
                                <p class="text-xs text-gray-400">Command management dashboard</p>
                            </div>
                        </div>
                        <a href="https://github.com/jnsougata/discohook" target="_blank" class="group flex items-center gap-2 px-4 py-2 btn-ghost">
                            <i class="fa-brands fa-github text-gray-400 group-hover:text-white transition-colors"></i>
                            <span class="text-sm text-gray-400 group-hover:text-white transition-colors hidden sm:inline">View on GitHub</span>
                        </a>
                    </div>
                </div>
            </header>
            <div class="grid gap-4" id="commands-container"></div>
        </div>
    </main>

    <script>
        let main = document.querySelector("#commands-container");
        let dialog = document.querySelector("dialog");
        let login = document.querySelector("#login");
        let password = document.querySelector("#password");

        async function hashPassword(input) {
            const encoder = new TextEncoder();
            const data = encoder.encode(input);
            const buffer = await crypto.subtle.digest("SHA-256", data);
            return Array.from(new Uint8Array(buffer)).map(b => b.toString(16).padStart(2, "0")).join("");
        }

        function buildCommandElem(command, password) {
            let card = document.createElement("div");
            card.className = "card-bg p-0 border overflow-hidden card-hover fade-in group";
            let header = document.createElement("div");
            header.className = "flex items-center justify-between p-4";
            let title = document.createElement("div");
            title.className = "flex items-center gap-2";
            title.innerHTML = `<span class="text-white font-semibold">Command: ${command.name || 'Unnamed'}</span>`;
            let del = document.createElement("button");
            del.className = "px-3 py-1.5 btn-ghost text-sm font-medium flex items-center gap-2 color-red-500 hover:bg-red-600 hover:text-white transition-colors";
            del.innerHTML = `<i class="fas fa-trash"></i> Delete`;
            del.addEventListener("click", async () => {
                if (confirm("Are you sure you want to delete this command?")) {
                    const resp = await fetch(`/api/commands`, { method: "DELETE", body: JSON.stringify({ password: password, id: command.id, guild_id: command.guild_id || null }) });
                    if (resp.status === 204) { card.style.animation = "fadeOut 0.3s ease-out"; setTimeout(() => card.remove(), 300); }
                    else { let data = await resp.json(); alert(data.error); }
                }
            });
            header.appendChild(title);
            header.appendChild(del);
            let codeContainer = document.createElement("div");
            codeContainer.className = "p-4 bg-black";
            let pre = document.createElement("pre");
            pre.className = "overflow-x-auto";
            let code = document.createElement("code");
            code.className = "text-sm";
            code.style.color = '#fff';
            code.innerHTML = JSON.stringify(command, null, 4);
            pre.appendChild(code);
            codeContainer.appendChild(pre);
            card.appendChild(header);
            card.appendChild(codeContainer);
            return card;
        }

        async function renderCommands(password) {
            dialog.close();
            main.innerHTML = `<div class="flex items-center justify-center py-12"><div class="text-center"><i class="fa-solid fa-spinner fa-spin text-4xl text-white mb-4"></i><p class="text-gray-400">Loading commands...</p></div></div>`;
            const resp = await fetch(`/api/sync`, { method: "POST", body: JSON.stringify({ password: password }) });
            let data = await resp.json();
            main.innerHTML = '';
            if (resp.status === 200) {
                if (data.length === 0) { main.innerHTML = `<div class="card-bg p-12 text-center"><i class="fa-solid fa-inbox text-6xl text-gray-400 mb-4"></i><p class="text-gray-400 text-lg">No commands found</p></div>`; }
                else { data.forEach(command => { main.appendChild(buildCommandElem(command, password)); }); hljs.highlightAll(); }
            } else { main.innerHTML = `<div class="bg-white/5 border border-red-700 p-6"><p class="text-white">Discord Error: ${data.message} (code: ${data.code})</p></div>`; }
        }

        login.addEventListener("click", async () => {
            let hashedPassword = await hashPassword(password.value);
            const resp = await fetch(`/api/verify`, { method: "POST", body: JSON.stringify({ password: hashedPassword }) });
            let data = await resp.json();
            if (resp.status !== 200) {
                password.classList.add('border-red-500');
                password.placeholder = data.error || 'Invalid password';
                setTimeout(() => { password.classList.remove('border-red-500'); password.placeholder = 'Enter your password'; }, 3000);
            } else {
                localStorage.setItem("password", hashedPassword);
                await renderCommands(hashedPassword);
            }
        });

        password.addEventListener("keypress", (e) => { if (e.key === "Enter") { login.click(); } });

        window.addEventListener("DOMContentLoaded", async () => {
            const savedPassword = localStorage.getItem("password");
            if (!savedPassword) { dialog.showModal(); return; }
            const resp = await fetch(`/api/verify`, { method: "POST", body: JSON.stringify({ password: savedPassword }) });
            if (resp.status !== 200) { dialog.showModal(); }
            else { await renderCommands(savedPassword); }
        });
    </script>
</body>
</html>
        """,
        status_code=200,
    )
