from starlette.responses import HTMLResponse


async def dashboard(_):
    return HTMLResponse(
       """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>discohook</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css" />
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        'inter': ['Inter', 'system-ui', 'sans-serif'],
                    },
                    colors: {
                        discord: {
                            dark: '#1e1f22',
                            darker: '#111214',
                            gray: '#2b2d31',
                            light: '#313338',
                            accent: '#5865f2',
                            green: '#23a55a',
                            red: '#f23f43',
                            yellow: '#fee75c'
                        }
                    },
                    animation: {
                        'fade-in': 'fadeIn 0.3s ease-in-out',
                        'slide-up': 'slideUp 0.3s ease-out',
                        'scale-in': 'scaleIn 0.2s ease-out',
                    }
                }
            }
        }
    </script>
    <style>
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        @keyframes slideUp {
            from { transform: translateY(20px); opacity: 0; }
            to { transform: translateY(0); opacity: 1; }
        }
        @keyframes scaleIn {
            from { transform: scale(0.95); opacity: 0; }
            to { transform: scale(1); opacity: 1; }
        }
        .glass-effect {
            backdrop-filter: blur(12px);
            background: rgba(30, 31, 34, 0.8);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .glow-effect {
            box-shadow: 0 0 20px rgba(88, 101, 242, 0.3);
        }
        pre code {
            font-family: 'JetBrains Mono', 'Fira Code', 'Monaco', 'Menlo', monospace !important;
            line-height: 1.5; /* Improve readability of code blocks */
        }
        /* Specific fix for icon alignment */
        .command-icon-wrapper {
            display: flex;
            align-items: center; /* Ensure vertical centering */
        }
        .command-icon-wrapper i {
             line-height: 1; /* Normalize line height for icons */
             font-size: 1.25rem; /* Slightly larger icons for better presence */
        }
        /* For two-line truncation, if needed. Add `line-clamp-2` to the description p tag */
        /* .line-clamp-2 {
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        } */
    </style>
</head>
<body class="font-inter bg-gradient-to-br from-discord-darker via-discord-dark to-discord-gray min-h-screen text-gray-200">
    <div id="loginModal" class="fixed inset-0 bg-black bg-opacity-70 backdrop-blur-md flex items-center justify-center z-50 animate-fade-in">
        <div class="glass-effect rounded-2xl p-10 max-w-xl w-full mx-6 animate-scale-in border border-discord-gray">
            <div class="text-center mb-8">
                <div class="w-20 h-20 bg-gradient-to-br from-discord-accent to-purple-600 rounded-full flex items-center justify-center mx-auto mb-5 glow-effect">
                    <i class="fab fa-discord text-white text-3xl"></i>
                </div>
                <h2 class="text-3xl font-bold text-white mb-2">Welcome Back</h2>
                <p class="text-gray-400 text-base">Enter your password to access the command manager</p>
            </div>
            
            <div class="space-y-5">
                <div class="relative">
                    <input 
                        id="password" 
                        type="password" 
                        placeholder="Enter your password"
                        class="w-full bg-discord-gray border border-gray-600 text-white rounded-xl px-5 py-3.5 pl-14 text-lg focus:outline-none focus:ring-2 focus:ring-discord-accent focus:border-transparent transition-all duration-200 placeholder-gray-500"
                    >
                    <i class="fas fa-lock absolute left-5 top-1/2 transform -translate-y-1/2 text-gray-400 text-lg"></i>
                </div>
                
                <button 
                    id="login"
                    class="w-full bg-gradient-to-r from-discord-accent to-purple-600 hover:from-discord-accent hover:to-purple-700 text-white font-semibold py-3.5 px-6 rounded-xl transition-all duration-200 transform hover:scale-103 active:scale-98 flex items-center justify-center space-x-3 text-lg"
                >
                    <span>Sign In</span>
                    <i class="fas fa-arrow-right text-base"></i>
                </button>
            </div>
        </div>
    </div>

    <div class="min-h-screen flex flex-col">
        <header class="glass-effect border-b border-gray-700 shadow-lg">
            <div class="max-w-7xl mx-auto px-6 sm:px-8 lg:px-10 py-3">
                <div class="flex items-center justify-between">
                    <div class="flex items-center space-x-5">
                        <div class="w-12 h-12 bg-gradient-to-br from-discord-accent to-purple-600 rounded-xl flex items-center justify-center shadow-md">
                            <i class="fab fa-discord text-white text-xl"></i>
                        </div>
                        <div>
                            <h1 class="text-2xl font-bold text-white">Discohook</h1>
                            <p class="text-sm text-gray-400">Command Manager</p>
                        </div>
                    </div>
                    
                    <div class="flex items-center space-x-4">
                        <div class="hidden sm:flex items-center space-x-2 text-sm text-gray-400 bg-discord-gray px-3 py-1.5 rounded-full">
                            <div class="w-2 h-2 bg-discord-green rounded-full animate-pulse"></div>
                            <span id="commandCount" class="font-medium">0 commands</span>
                        </div>
                        <a 
                            href="https://github.com/jnsougata/discohook" 
                            target="_blank"
                            class="p-2.5 text-gray-400 hover:text-white transition-colors duration-200 hover:bg-discord-gray rounded-lg"
                        >
                            <i class="fab fa-github text-xl"></i>
                        </a>
                    </div>
                </div>
            </div>
        </header>

        <main id="main" class="flex-1 max-w-7xl mx-auto px-6 sm:px-8 lg:px-10 py-10 w-full">
            <div id="loadingState" class="flex flex-col items-center justify-center py-20 text-center">
                <div class="inline-block animate-spin rounded-full h-16 w-16 border-4 border-discord-accent border-t-transparent mb-5"></div>
                <p class="text-gray-400 text-lg font-medium">Loading commands...</p>
            </div>

            <div id="emptyState" class="hidden flex-col items-center justify-center py-20 text-center">
                <div class="w-28 h-28 bg-discord-gray rounded-full flex items-center justify-center mx-auto mb-8">
                    <i class="fas fa-robot text-5xl text-gray-500"></i>
                </div>
                <h3 class="text-2xl font-semibold text-white mb-3">No Commands Found</h3>
                <p class="text-gray-400 max-w-md mx-auto text-base">Your Discord commands will appear here once they're synced with the bot.</p>
            </div>

            <div id="errorState" class="hidden flex-col items-center justify-center py-20 text-center">
                <div class="w-28 h-28 bg-discord-red bg-opacity-20 rounded-full flex items-center justify-center mx-auto mb-8">
                    <i class="fas fa-exclamation-triangle text-5xl text-discord-red"></i>
                </div>
                <h3 class="text-2xl font-semibold text-white mb-3">Error Loading Commands</h3>
                <p id="errorMessage" class="text-gray-400 max-w-md mx-auto mb-6 text-base">Something went wrong while loading your commands.</p>
                <button 
                    id="retryBtn"
                    class="px-8 py-3 bg-discord-accent hover:bg-discord-accent/80 text-white rounded-lg transition-colors font-semibold text-base"
                >
                    Try Again
                </button>
            </div>

            <div id="commandsGrid" class="flex flex-col space-y-4"></div>
        </main>
    </div>

    <div id="toast" class="fixed top-6 right-6 z-50 transform translate-x-full transition-transform duration-300">
        <div class="glass-effect rounded-lg px-7 py-4 text-white shadow-xl flex items-center space-x-4">
            <i id="toastIcon" class="fas fa-check-circle text-discord-green text-lg"></i>
            <span id="toastMessage" class="text-base font-medium">Command deleted successfully</span>
        </div>
    </div>

    <script>
        const loginModal = document.getElementById('loginModal');
        const loginBtn = document.getElementById('login');
        const passwordInput = document.getElementById('password');
        const main = document.getElementById('main');
        const loadingState = document.getElementById('loadingState');
        const emptyState = document.getElementById('emptyState');
        const errorState = document.getElementById('errorState');
        const errorMessage = document.getElementById('errorMessage');
        const retryBtn = document.getElementById('retryBtn');
        const commandsGrid = document.getElementById('commandsGrid');
        const commandCount = document.getElementById('commandCount');
        const toast = document.getElementById('toast');
        const toastIcon = document.getElementById('toastIcon');
        const toastMessage = document.getElementById('toastMessage');

        let currentPassword = null;

        async function hashPassword(input) {
            const encoder = new TextEncoder();
            const data = encoder.encode(input);
            const buffer = await crypto.subtle.digest("SHA-256", data);
            const hashArray = Array.from(new Uint8Array(buffer));
            return hashArray.map(b => b.toString(16).padStart(2, "0")).join("");
        }

        function showToast(message, isError = false) {
            toastMessage.textContent = message;
            toastIcon.className = isError ? 'fas fa-exclamation-circle text-discord-red text-lg' : 'fas fa-check-circle text-discord-green text-lg';
            toast.style.transform = 'translateX(0)';
            
            setTimeout(() => {
                toast.style.transform = 'translateX(100%)';
            }, 3000);
        }

        function showError(message) {
            loadingState.style.display = 'none';
            emptyState.style.display = 'none';
            commandsGrid.innerHTML = '';
            errorMessage.textContent = message;
            errorState.style.display = 'flex'; // Use flex for centered content
        }

        function hideAllStates() {
            loadingState.style.display = 'none';
            emptyState.style.display = 'none';
            errorState.style.display = 'none';
        }

        function getCommandTypeIcon(command) {
            if (command.guild_id) {
                return '<span class="command-icon-wrapper"><i class="fas fa-server text-discord-yellow"></i></span>';
            }
            return '<span class="command-icon-wrapper"><i class="fas fa-globe text-discord-green"></i></span>';
        }

        function getCommandScope(command) {
            return command.guild_id ? 'Guild' : 'Global';
        }

        function getCommandTypeLabel(type) {
            const types = {
                1: 'Slash',
                2: 'User',
                3: 'Message'
            };
            return types[type] || 'Unknown';
        }

        function getOptionTypeName(type) {
            const types = {
                1: 'SubCommand',
                2: 'SubCommandGroup',
                3: 'String',
                4: 'Integer',
                5: 'Boolean',
                6: 'User',
                7: 'Channel',
                8: 'Role',
                9: 'Mentionable',
                10: 'Number',
                11: 'Attachment'
            };
            return types[type] || 'Unknown';
        }

        function buildCommandListItem(command, password) {
            const listItem = document.createElement('div');
            // Changed hover effect for list item to be more subtle with a border change
            listItem.className = 'glass-effect rounded-xl p-5 hover:border-discord-accent hover:shadow-lg transition-all duration-300 animate-slide-up border border-transparent flex flex-col';
            
            listItem.innerHTML = `
                <div class="flex items-center justify-between w-full mb-3">
                    <div class="flex items-center space-x-4 flex-grow">
                        ${getCommandTypeIcon(command)}
                        <div>
                            <h3 class="text-xl font-bold text-white leading-tight">/${command.name}</h3>
                            <div class="flex items-center space-x-2 mt-1">
                                <span class="text-xs px-2 py-0.5 bg-discord-gray rounded-full text-gray-400 font-medium">${getCommandScope(command)}</span>
                                <span class="text-xs px-2 py-0.5 bg-discord-gray rounded-full text-gray-400 font-medium">${getCommandTypeLabel(command.type)} Command</span>
                            </div>
                        </div>
                    </div>
                    <button class="delete-btn flex-shrink-0 p-2 text-gray-400 hover:text-discord-red hover:bg-discord-red/10 rounded-lg transition-all duration-200">
                        <i class="fas fa-trash text-sm"></i>
                    </button>
                </div>
                
                <p class="text-gray-300 text-sm mb-4 leading-relaxed flex-grow pr-4">${command.description || '<span class="italic text-gray-500">No description provided for this command.</span>'}</p>
                
                ${command.options && command.options.length > 0 ? `
                    <details class="group mb-4">
                        <summary class="flex items-center justify-between cursor-pointer text-sm text-gray-400 hover:text-white transition-colors py-1">
                            <span class="font-medium">Options (${command.options.length})</span>
                            <i class="fas fa-chevron-down group-open:rotate-180 transition-transform text-xs"></i>
                        </summary>
                        <div class="mt-3 space-y-2">
                            ${command.options.map(option => `
                                <div class="bg-discord-darker rounded-lg p-3 border border-gray-700 flex flex-col sm:flex-row sm:items-center sm:justify-between text-sm">
                                    <div class="flex items-center space-x-2 mb-2 sm:mb-0">
                                        <span class="text-gray-200 font-medium">${option.name}</span>
                                        <span class="px-2 py-1 bg-discord-gray rounded text-gray-400 text-xs font-medium">
                                            ${getOptionTypeName(option.type)}
                                        </span>
                                    </div>
                                    <span class="px-2.5 py-1 ${option.required ? 'bg-discord-red' : 'bg-discord-green'} text-white rounded-full text-xs font-semibold self-start sm:self-auto">
                                        ${option.required ? 'REQUIRED' : 'OPTIONAL'}
                                    </span>
                                </div>
                                ${option.description ? `<p class="text-xs text-gray-400 ml-4 mt-2 leading-snug">${option.description}</p>` : ''}
                            `).join('')}
                        </div>
                    </details>
                ` : ''}
                
                ${command.guild_id ? `
                    <div class="text-xs mb-4">
                        <span class="text-gray-400 font-medium">GUILD ID: </span>
                        <span class="text-gray-300 font-mono select-all text-sm break-all">${command.guild_id}</span>
                    </div>
                ` : ''}
                
                <details class="group mt-auto"> <summary class="flex items-center justify-between cursor-pointer text-sm text-gray-400 hover:text-white transition-colors py-2 border-t border-gray-700 pt-4">
                        <span class="font-medium">View Raw JSON</span>
                        <i class="fas fa-chevron-down group-open:rotate-180 transition-transform text-xs"></i>
                    </summary>
                    <div class="mt-3">
                        <pre class="bg-discord-darker rounded-lg p-4 text-xs overflow-x-auto max-h-60 border border-gray-700"><code class="language-json">${JSON.stringify(command, null, 2)}</code></pre>
                    </div>
                </details>
            `;

            const deleteBtn = listItem.querySelector('.delete-btn');
            deleteBtn.addEventListener('click', async (event) => {
                event.stopPropagation(); // Prevent details from toggling if clicking delete button within details summary
                if (!confirm(`Are you sure you want to delete the command "/${command.name}"?\n\nThis action cannot be undone.`)) {
                    return;
                }

                const originalContent = deleteBtn.innerHTML;
                deleteBtn.innerHTML = '<i class="fas fa-spinner fa-spin text-sm"></i>';
                deleteBtn.disabled = true;

                try {
                    const resp = await fetch(`/api/commands`, {
                        method: "DELETE",
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            password: password,
                            id: command.id,
                            guild_id: command.guild_id || null
                        })
                    });

                    if (resp.status === 204) {
                        listItem.style.transform = 'scale(0.95)';
                        listItem.style.opacity = '0';
                        setTimeout(() => {
                            listItem.remove();
                            updateCommandCount();
                            checkIfEmpty();
                        }, 300);
                        showToast('Command deleted successfully');
                    } else {
                        const data = await resp.json();
                        showToast(data.error || 'Failed to delete command', true);
                        deleteBtn.innerHTML = originalContent;
                        deleteBtn.disabled = false;
                    }
                } catch (error) {
                    console.error('Delete error:', error);
                    showToast('Network error: Failed to delete command', true);
                    deleteBtn.innerHTML = originalContent;
                    deleteBtn.disabled = false;
                }
            });

            return listItem;
        }

        function updateCommandCount() {
            const count = commandsGrid.children.length;
            commandCount.textContent = `${count} command${count !== 1 ? 's' : ''}`;
        }

        function checkIfEmpty() {
            if (commandsGrid.children.length === 0) {
                hideAllStates();
                emptyState.style.display = 'flex';
            }
        }

        async function renderCommands(password) {
            hideAllStates();
            loadingState.style.display = 'flex';
            commandsGrid.innerHTML = '';

            try {
                const resp = await fetch(`/api/sync`, {
                    method: "POST",
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ password: password })
                });

                const data = await resp.json();

                if (resp.status === 200) {
                    hideAllStates();
                    
                    if (data.length === 0) {
                        emptyState.style.display = 'flex'; // Use flex for centered content
                    } else {
                        data.forEach((command, index) => {
                            setTimeout(() => {
                                const listItem = buildCommandListItem(command, password);
                                commandsGrid.appendChild(listItem);
                                updateCommandCount();
                            }, index * 100);
                        });
                        setTimeout(() => {
                            hljs.highlightAll();
                        }, data.length * 100 + 200);
                    }
                } else {
                    throw new Error(`Discord API Error: ${data.message || 'Unknown error'} ${data.code ? `(Code: ${data.code})` : ''}`);
                }
            } catch (error) {
                console.error('Render commands error:', error);
                showError(error.message || 'Failed to load commands');
            }
        }

        loginBtn.addEventListener('click', async () => {
            const password = passwordInput.value.trim();
            if (!password) {
                showToast('Please enter a password', true);
                passwordInput.focus();
                return;
            }

            const originalContent = loginBtn.innerHTML;
            loginBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> <span>Signing In...</span>';
            loginBtn.disabled = true;

            try {
                const hashedPassword = await hashPassword(password);
                
                const resp = await fetch(`/api/verify`, {
                    method: "POST",
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ password: hashedPassword })
                });

                const data = await resp.json();
                
                if (resp.status === 200) {
                    localStorage.setItem("password", hashedPassword);
                    currentPassword = hashedPassword;
                    loginModal.style.display = 'none';
                    await renderCommands(hashedPassword);
                } else {
                    throw new Error(data.error || 'Invalid password');
                }
            } catch (error) {
                console.error('Login error:', error);
                showToast(error.message || 'Login failed', true);
            } finally {
                loginBtn.innerHTML = originalContent;
                loginBtn.disabled = false;
            }
        });

        passwordInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                loginBtn.click();
            }
        });

        retryBtn.addEventListener('click', () => {
            if (currentPassword) {
                renderCommands(currentPassword);
            }
        });

        window.addEventListener('DOMContentLoaded', async () => {
            const savedPassword = localStorage.getItem("password");
            
            if (savedPassword) {
                try {
                    const resp = await fetch(`/api/verify`, {
                        method: "POST",
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ password: savedPassword })
                    });

                    if (resp.status === 200) {
                        currentPassword = savedPassword;
                        loginModal.style.display = 'none';
                        await renderCommands(savedPassword);
                    } else {
                        localStorage.removeItem("password");
                        loginModal.style.display = 'flex';
                    }
                } catch (error) {
                    console.error('Auto-login error:', error);
                    localStorage.removeItem("password");
                    loginModal.style.display = 'flex';
                }
            } else {
                loginModal.style.display = 'flex';
            }
        });
        
        window.addEventListener('storage', (e) => {
            if (e.key === 'password' && e.newValue === null) {
                location.reload();
            }
        });
    </script>
</body>
</html>
       """,
        status_code=200,
    )
