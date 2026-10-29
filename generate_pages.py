```python
# ============================================================
# VTO RECOVERY - FRONTEND PAGE GENERATOR
# ============================================================

# ------------------------------------------------------------
# GLOBAL SIDEBAR
# ------------------------------------------------------------

def get_sidebar(active_page):
    links = [
        ("index.html", "chart-pie", "Dashboard"),
        ("accounts.html", "folder-open", "Accounts"),
        ("assigned_accounts.html", "user-check", "Assigned Accounts"),
        ("call_log.html", "phone-volume", "Call Log"),
        ("arrangements.html", "calendar-days", "Arrangements"),
        ("follow_ups.html", "clock-rotate-left", "Follow-ups"),
        ("clients.html", "users", "Clients"),
        ("collectors.html", "user-group", "Collectors"),
        ("reports.html", "chart-column", "Reports"),
        ("notifications.html", "bell", "Notifications")
    ]

    nav_html = ""

    for href, icon, label in links:
        is_active = active_page == href

        if is_active:
            classes = (
                "flex items-center px-4 py-3 rounded-xl "
                "font-semibold text-emerald-700 bg-emerald-50/80 shadow-sm"
            )
            icon_color = "text-emerald-600"
        else:
            classes = (
                "flex items-center px-4 py-3 rounded-xl "
                "font-medium text-slate-600 "
                "hover:bg-slate-50 hover:text-slate-900 "
                "transition-colors"
            )
            icon_color = "text-slate-400"

        icon_classes = f"fa-solid fa-{icon} w-5 mr-3 {icon_color}"

        nav_html += f"""
            <a href="{href}" class="{classes}">
                <i class="{icon_classes}"></i>
                {label}
            </a>
        """

    return f"""
        <aside class="w-64 bg-white border-r border-slate-200
                      flex flex-col z-20 shadow-sm hidden md:flex">

            <!-- Logo -->
            <div class="p-6 border-b border-slate-100
                        flex items-center space-x-3">

                <div class="w-10 h-10 rounded-xl bg-emerald-500
                            flex items-center justify-center text-white
                            font-bold text-lg shadow-md
                            shadow-emerald-500/20">
                    VTO
                </div>

                <div>
                    <h1 class="font-bold text-slate-900
                               tracking-tight leading-none">
                        VTO Recovery
                    </h1>

                    <span class="text-xs text-slate-500 font-medium">
                        Collections Suite
                    </span>
                </div>
            </div>

            <!-- Navigation -->
            <nav class="flex-1 px-4 py-6 space-y-1.5
                        overflow-y-auto text-sm">

                {nav_html}

            </nav>

            <!-- Logged-in User -->
            <div class="p-4 border-t border-slate-100
                        flex items-center space-x-3">

                <div class="w-9 h-9 rounded-full bg-slate-900
                            text-white font-semibold
                            flex items-center justify-center
                            text-sm shadow">
                    V
                </div>

                <div>
                    <p class="text-sm font-semibold text-slate-800">
                        Vura
                    </p>

                    <p class="text-xs text-slate-500">
                        Active Session
                    </p>
                </div>

            </div>

        </aside>
    """


# ------------------------------------------------------------
# GLOBAL HEADER
# ------------------------------------------------------------

def get_header():
    return """
        <header class="bg-white border-b border-slate-200
                       px-6 py-4 flex items-center
                       justify-between z-10 shadow-sm">

            <!-- SEARCH -->
            <div class="flex items-center space-x-4
                        flex-1 max-w-lg">

                <div class="relative w-full">

                    <!-- Search icon -->
                    <span class="absolute inset-y-0 left-0
                                 flex items-center pl-3
                                 pointer-events-none
                                 text-slate-400">

                        <i class="fa-solid fa-magnifying-glass"></i>

                    </span>

                    <!-- Search input -->
                    <input
                        id="globalSearch"
                        type="text"
                        placeholder="Search accounts, clients..."
                        autocomplete="off"
                        onkeyup="globalSearchFunction()"
                        class="w-full pl-10 pr-10 py-2
                               bg-slate-50
                               border border-slate-200
                               rounded-xl text-sm
                               focus:outline-none
                               focus:ring-2
                               focus:ring-emerald-500">

                    <!-- Clear button -->
                    <button
                        id="clearSearch"
                        onclick="clearGlobalSearch()"
                        class="hidden absolute right-3
                               top-1/2 -translate-y-1/2
                               text-slate-400
                               hover:text-slate-700">

                        <i class="fa-solid fa-xmark"></i>

                    </button>

                </div>

            </div>


            <!-- HEADER ACTIONS -->
            <div class="flex items-center space-x-4 ml-4">

                <!-- New dropdown -->
                <div class="relative">

                    <button
                        onclick="toggleNewMenu()"
                        class="bg-blue-600
                               hover:bg-blue-700
                               text-white px-4 py-2
                               rounded-xl font-medium
                               text-sm flex items-center
                               shadow-md">

                        <i class="fa-solid fa-plus mr-2"></i>
                        New

                        <i class="fa-solid fa-chevron-down
                                  ml-2 text-xs"></i>

                    </button>


                    <!-- Dropdown menu -->
                    <div
                        id="newMenu"
                        class="hidden absolute right-0 mt-2
                               w-52 bg-white
                               border border-slate-200
                               rounded-xl shadow-xl
                               z-50 overflow-hidden">

                        <button
                            onclick="newAction('account')"
                            class="w-full text-left px-4 py-3
                                   text-sm hover:bg-slate-50
                                   flex items-center">

                            <i class="fa-solid fa-folder-plus
                                      w-5 text-emerald-600"></i>

                            New Account
                        </button>

                        <button
                            onclick="newAction('call')"
                            class="w-full text-left px-4 py-3
                                   text-sm hover:bg-slate-50
                                   flex items-center">

                            <i class="fa-solid fa-phone
                                      w-5 text-blue-600"></i>

                            Log Call
                        </button>

                        <button
                            onclick="newAction('arrangement')"
                            class="w-full text-left px-4 py-3
                                   text-sm hover:bg-slate-50
                                   flex items-center">

                            <i class="fa-solid fa-calendar-plus
                                      w-5 text-purple-600"></i>

                            Payment Arrangement
                        </button>

                        <button
                            onclick="newAction('followup')"
                            class="w-full text-left px-4 py-3
                                   text-sm hover:bg-slate-50
                                   flex items-center">

                            <i class="fa-solid fa-clock
                                      w-5 text-amber-600"></i>

                            Follow-up
                        </button>

                    </div>

                </div>


                <!-- User avatar -->
                <div
                    class="w-10 h-10 rounded-xl bg-slate-900
                           text-white font-bold
                           flex items-center justify-center
                           text-sm shadow">

                    V

                </div>

            </div>

        </header>
    """


# ------------------------------------------------------------
# JAVASCRIPT
# ------------------------------------------------------------

global_scripts = """
<script>

    // ========================================================
    // GLOBAL SEARCH
    // ========================================================

    function globalSearchFunction() {

        const input =
            document.getElementById("globalSearch");

        const clearButton =
            document.getElementById("clearSearch");

        if (!input) return;

        const searchValue =
            input.value.toLowerCase().trim();

        // Show / hide clear button
        if (searchValue.length > 0) {
            clearButton.classList.remove("hidden");
        } else {
            clearButton.classList.add("hidden");
        }

        // Find searchable rows/cards
        const searchableElements =
            document.querySelectorAll(
                "tbody tr, .searchable-item"
            );

        let visibleCount = 0;

        searchableElements.forEach(element => {

            const text =
                element.innerText.toLowerCase();

            if (
                searchValue === "" ||
                text.includes(searchValue)
            ) {

                element.style.display = "";

                visibleCount++;

            } else {

                element.style.display = "none";

            }

        });

        // Search result message
        const noResults =
            document.getElementById("noSearchResults");

        if (noResults) {

            if (
                searchValue !== "" &&
                visibleCount === 0
            ) {

                noResults.classList.remove("hidden");

            } else {

                noResults.classList.add("hidden");

            }

        }

    }


    // ========================================================
    // CLEAR SEARCH
    // ========================================================

    function clearGlobalSearch() {

        const input =
            document.getElementById("globalSearch");

        if (!input) return;

        input.value = "";

        globalSearchFunction();

        input.focus();

    }


    // ========================================================
    // NEW MENU
    // ========================================================

    function toggleNewMenu() {

        const menu =
            document.getElementById("newMenu");

        if (!menu) return;

        menu.classList.toggle("hidden");

    }


    // ========================================================
    // NEW ACTIONS
    // ========================================================

    function newAction(type) {

        const menu =
            document.getElementById("newMenu");

        if (menu) {
            menu.classList.add("hidden");
        }

        if (type === "account") {
            alert("New Account form will be connected to the backend.");
        }

        if (type === "call") {
            window.location.href = "call_log.html";
        }

        if (type === "arrangement") {
            window.location.href = "arrangements.html";
        }

        if (type === "followup") {
            window.location.href = "follow_ups.html";
        }

    }


    // ========================================================
    // DETAILS BUTTON
    // ========================================================

    function viewAccount(accountId) {

        alert(
            "Account details for " +
            accountId +
            " will be connected to the backend."
        );

    }


    // ========================================================
    // CLOSE NEW MENU WHEN CLICKING OUTSIDE
    // ========================================================

    document.addEventListener("click", function(event) {

        const menu =
            document.getElementById("newMenu");

        const button =
            event.target.closest("button");

        if (!menu) return;

        if (
            !menu.contains(event.target) &&
            !button
        ) {
            menu.classList.add("hidden");
        }

    });

</script>
"""


# ------------------------------------------------------------
# BASE HTML
# ------------------------------------------------------------

base_head = """<!DOCTYPE html>

<html lang="en" class="h-full">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width,
                   initial-scale=1.0">

    <title>
        VTO Recovery - Collections Suite
    </title>


    <!-- Tailwind -->
    <script src="https://cdn.tailwindcss.com"></script>


    <!-- Google Font -->
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap"
        rel="stylesheet">


    <!-- Font Awesome -->
    <link
        rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">


    <!-- Tailwind configuration -->
    <script>

        tailwind.config = {

            theme: {

                extend: {

                    fontFamily: {

                        sans: [
                            'Inter',
                            'sans-serif'
                        ]

                    }

                }

            }

        }

    </script>

</head>


<body
    class="h-full bg-slate-100
           font-sans text-slate-800
           antialiased overflow-hidden">

    <div
        class="flex h-screen w-screen
               overflow-hidden">
"""


# ============================================================
# 1. DASHBOARD
# ============================================================

dashboard_html = (
    base_head
    + get_sidebar("index.html")
    + f"""
        <main class="flex-1 flex flex-col
                     h-full overflow-hidden">

            {get_header()}

            <div
                class="flex-1 overflow-y-auto
                       p-6 lg:p-8 space-y-6">

                <div>

                    <h2
                        class="text-2xl font-bold
                               text-slate-900
                               tracking-tight">

                        Hi Vura, view your projects below

                    </h2>

                    <p
                        class="text-sm text-slate-500
                               mt-0.5">

                        Here is your operational
                        collections snapshot.

                    </p>

                </div>


                <!-- KPI CARDS -->

                <div
                    class="grid grid-cols-1
                           sm:grid-cols-2
                           lg:grid-cols-6 gap-4">


                    <!-- Accounts -->

                    <div
                        class="bg-white p-5 rounded-2xl
                               border border-slate-200
                               shadow-sm relative">

                        <p
                            class="text-xs font-semibold
                                   text-slate-500">

                            Accounts worked on today

                        </p>

                        <h3
                            class="text-2xl font-bold
                                   text-slate-900 mt-2">

                            25

                        </h3>

                        <div
                            class="absolute top-4 right-4
                                   w-9 h-9 rounded-xl
                                   bg-cyan-50
                                   flex items-center
                                   justify-center
                                   text-cyan-600">

                            <i class="fa-solid fa-user-check"></i>

                        </div>

                    </div>


                    <!-- Calls -->

                    <div
                        class="bg-white p-5 rounded-2xl
                               border border-slate-200
                               shadow-sm relative">

                        <p
                            class="text-xs font-semibold
                                   text-slate-500">

                            Calls made today

                        </p>

                        <h3
                            class="text-2xl font-bold
                                   text-slate-900 mt-2">

                            40

                        </h3>

                        <div
                            class="absolute top-4 right-4
                                   w-9 h-9 rounded-xl
                                   bg-purple-50
                                   flex items-center
                                   justify-center
                                   text-purple-600">

                            <i class="fa-solid fa-phone"></i>

                        </div>

                    </div>


                    <!-- Arrangements -->

                    <div
                        class="bg-white p-5 rounded-2xl
                               border border-slate-200
                               shadow-sm relative">

                        <p
                            class="text-xs font-semibold
                                   text-slate-500">

                            Arrangements today

                        </p>

                        <h3
                            class="text-2xl font-bold
                                   text-slate-900 mt-2">

                            50

                        </h3>

                        <div
                            class="absolute top-4 right-4
                                   w-9 h-9 rounded-xl
                                   bg-emerald-50
                                   flex items-center
                                   justify-center
                                   text-emerald-600">

                            <i class="fa-solid fa-circle-check"></i>

                        </div>

                    </div>


                    <!-- Follow ups -->

                    <div
                        class="bg-white p-5 rounded-2xl
                               border border-slate-200
                               shadow-sm relative">

                        <p
                            class="text-xs font-semibold
                                   text-slate-500">

                            Follow-ups due

                        </p>

                        <h3
                            class="text-2xl font-bold
                                   text-slate-900 mt-2">

                            30

                        </h3>

                        <div
                            class="absolute top-4 right-4
                                   w-9 h-9 rounded-xl
                                   bg-blue-50
                                   flex items-center
                                   justify-center
                                   text-blue-600">

                            <i class="fa-solid fa-clock"></i>

                        </div>

                    </div>


                    <!-- Outstanding -->

                    <div
                        class="bg-white p-5 rounded-2xl
                               border border-slate-200
                               shadow-sm relative">

                        <p
                            class="text-xs font-semibold
                                   text-slate-500">

                            Outstanding accounts

                        </p>

                        <h3
                            class="text-2xl font-bold
                                   text-slate-900 mt-2">

                            20

                        </h3>

                        <div
                            class="absolute top-4 right-4
                                   w-9 h-9 rounded-xl
                                   bg-amber-50
                                   flex items-center
                                   justify-center
                                   text-amber-600">

                            <i class="fa-solid fa-folder"></i>

                        </div>

                    </div>


                    <!-- Collections -->

                    <div
                        class="bg-white p-5 rounded-2xl
                               border border-slate-200
                               shadow-sm relative">

                        <p
                            class="text-xs font-semibold
                                   text-slate-500">

                            Collections this month

                        </p>

                        <h3
                            class="text-2xl font-bold
                                   text-slate-900 mt-2">

                            150

                        </h3>

                        <div
                            class="absolute top-4 right-4
                                   w-9 h-9 rounded-xl
                                   bg-teal-50
                                   flex items-center
                                   justify-center
                                   text-teal-600">

                            <i class="fa-solid fa-chart-line"></i>

                        </div>

                    </div>

                </div>

            </div>

        </main>

    </div>

    {global_scripts}

</body>
</html>
"""
)


# ============================================================
# 2. ACCOUNTS
# ============================================================

accounts_html = (
    base_head
    + get_sidebar("accounts.html")
    + f"""
        <main class="flex-1 flex flex-col
                     h-full overflow-hidden">

            {get_header()}

            <div
                class="flex-1 overflow-y-auto
                       p-6 lg:p-8 space-y-6">

                <div>

                    <h2
                        class="text-2xl font-bold
                               text-slate-900
                               tracking-tight">

                        Master Accounts Portfolio

                    </h2>

                    <p
                        class="text-sm text-slate-500
                               mt-0.5">

                        Complete system-wide list
                        of debtor accounts.

                    </p>

                </div>


                <div
                    class="bg-white rounded-2xl
                           border border-slate-200
                           shadow-sm p-6">


                    <div class="overflow-x-auto">

                        <table
                            class="w-full text-left
                                   text-sm">

                            <thead>

                                <tr
                                    class="border-b
                                           border-slate-200
                                           text-slate-400
                                           text-xs uppercase">

                                    <th class="py-3 px-4">
                                        Account ID
                                    </th>

                                    <th class="py-3 px-4">
                                        Debtor
                                    </th>

                                    <th class="py-3 px-4">
                                        Status
                                    </th>

                                    <th
                                        class="py-3 px-4
                                               text-right">

                                        Balance

                                    </th>

                                </tr>

                            </thead>


                            <tbody
                                class="divide-y
                                       divide-slate-100">


                                <tr>

                                    <td
                                        class="py-3 px-4
                                               font-mono
                                               font-bold">

                                        ACC-20218

                                    </td>

                                    <td
                                        class="py-3 px-4
                                               font-semibold">

                                        Jan du Plessis

                                    </td>

                                    <td
                                        class="py-3 px-4">

                                        <span
                                            class="px-2 py-0.5
                                                   bg-rose-100
                                                   text-rose-700
                                                   text-xs rounded">

                                            Legal

                                        </span>

                                    </td>

                                    <td
                                        class="py-3 px-4
                                               text-right
                                               font-mono
                                               font-bold">

                                        R 440,000

                                    </td>

                                </tr>


                                <tr>

                                    <td
                                        class="py-3 px-4
                                               font-mono
                                               font-bold">

                                        ACC-20213

                                    </td>

                                    <td
                                        class="py-3 px-4
                                               font-semibold">

                                        Francois van der Merwe

                                    </td>

                                    <td
                                        class="py-3 px-4">

                                        <span
                                            class="px-2 py-0.5
                                                   bg-amber-100
                                                   text-amber-700
                                                   text-xs rounded">

                                            Urgent

                                        </span>

                                    </td>

                                    <td
                                        class="py-3 px-4
                                               text-right
                                               font-mono
                                               font-bold">

                                        R 312,000

                                    </td>

                                </tr>


                            </tbody>

                        </table>

                    </div>


                    <!-- NO RESULTS -->

                    <div
                        id="noSearchResults"
                        class="hidden text-center
                               py-10 text-slate-500">

                        <i
                            class="fa-solid fa-magnifying-glass
                                   text-2xl mb-3 text-slate-300">
                        </i>

                        <p class="font-semibold">
                            No accounts found
                        </p>

                        <p class="text-sm">
                            Try another account ID,
                            name or status.
                        </p>

                    </div>

                </div>

            </div>

        </main>

    </div>

    {global_scripts}

</body>
</html>
"""
)


# ============================================================
# 3. ASSIGNED ACCOUNTS
# ============================================================

assigned_accounts_html = (
    base_head
    + get_sidebar("assigned_accounts.html")
    + f"""
        <main class="flex-1 flex flex-col
                     h-full overflow-hidden">

            {get_header()}

            <div
                class="flex-1 overflow-y-auto
                       p-6 lg:p-8 space-y-6">

                <div>

                    <h2
                        class="text-2xl font-bold
                               text-slate-900
                               tracking-tight">

                        My Work Queue

                    </h2>

                    <p
                        class="text-sm text-slate-500
                               mt-0.5">

                        Focused workspace —
                        only what's yours to collect.

                    </p>

                </div>


                <div
                    class="bg-white rounded-2xl
                           border border-slate-200
                           shadow-sm p-6 space-y-4">

                    <span
                        class="px-3 py-1
                               bg-emerald-100
                               text-emerald-800
                               rounded-full
                               text-xs font-bold">

                        ACTIVE RECORDS: 12 Accounts

                    </span>


                    <div
                        class="searchable-item
                               p-4 bg-slate-50
                               border border-slate-100
                               rounded-xl flex items-center
                               justify-between">

                        <div>

                            <span
                                class="font-bold
                                       text-slate-900">

                                ACC-20218

                            </span>

                            <h4
                                class="font-bold
                                       text-slate-800">

                                Jan du Plessis

                            </h4>

                            <p
                                class="text-xs
                                       text-slate-500">

                                082 119 5543

                            </p>

                        </div>


                        <div class="text-right">

                            <p
                                class="font-mono
                                       font-bold">

                                R 440,000

                            </p>

                            <button
                                onclick="viewAccount('ACC-20218')"
                                class="mt-2 px-3 py-1
                                       bg-amber-500
                                       hover:bg-amber-600
                                       text-white rounded-lg
                                       text-xs">

                                Details

                            </button>

                        </div>

                    </div>


                    <div
                        id="noSearchResults"
                        class="hidden text-center
                               py-8 text-slate-500">

                        No assigned accounts found.

                    </div>

                </div>

            </div>

        </main>

    </div>

    {global_scripts}

</body>
</html>
"""
)


# ============================================================
# 4. CALL LOG
# ============================================================

call_log_html = (
    base_head
    + get_sidebar("call_log.html")
    + f"""
        <main class="flex-1 flex flex-col
                     h-full overflow-hidden">

            {get_header()}

            <div
                class="flex-1 overflow-y-auto
                       p-6 lg:p-8 space-y-6">

                <div class="flex items-center justify-between gap-4">

                    <div>

                        <h2
                            class="text-2xl font-bold
                                   text-slate-900
                                   tracking-tight">

                            Call Log Activity

                        </h2>

                        <p
                            class="text-sm text-slate-500
                                   mt-0.5">

                            Recent outreach and outcome tracking
                            across assigned accounts.

                        </p>

                    </div>

                    <button
                        class="hidden md:inline-flex
                               items-center gap-2
                               bg-emerald-600 hover:bg-emerald-700
                               text-white px-4 py-2 rounded-xl
                               font-medium text-sm shadow-sm">

                        <i class="fa-solid fa-file-export"></i>
                        Export

                    </button>

                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 xl:grid-cols-4 gap-4">

                    <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-4">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-semibold uppercase tracking-wide text-slate-500">Calls today</span>
                            <span class="w-9 h-9 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center"><i class="fa-solid fa-phone"></i></span>
                        </div>
                        <p class="mt-4 text-3xl font-bold text-slate-900">42</p>
                        <p class="mt-1 text-xs text-emerald-600">+8% from yesterday</p>
                    </div>

                    <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-4">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-semibold uppercase tracking-wide text-slate-500">Connected</span>
                            <span class="w-9 h-9 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center"><i class="fa-solid fa-circle-check"></i></span>
                        </div>
                        <p class="mt-4 text-3xl font-bold text-slate-900">21</p>
                        <p class="mt-1 text-xs text-slate-500">Mid-call agreement rate</p>
                    </div>

                    <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-4">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-semibold uppercase tracking-wide text-slate-500">Follow-up needed</span>
                            <span class="w-9 h-9 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center"><i class="fa-solid fa-clock"></i></span>
                        </div>
                        <p class="mt-4 text-3xl font-bold text-slate-900">12</p>
                        <p class="mt-1 text-xs text-slate-500">Requires callback soon</p>
                    </div>

                    <div class="bg-white rounded-2xl border border-slate-200 shadow-sm p-4">
                        <div class="flex items-center justify-between">
                            <span class="text-xs font-semibold uppercase tracking-wide text-slate-500">Unavailable</span>
                            <span class="w-9 h-9 rounded-xl bg-purple-50 text-purple-600 flex items-center justify-center"><i class="fa-solid fa-volume-xmark"></i></span>
                        </div>
                        <p class="mt-4 text-3xl font-bold text-slate-900">9</p>
                        <p class="mt-1 text-xs text-slate-500">Voicemail / no answer</p>
                    </div>

                </div>


                <div
                    class="bg-white rounded-2xl
                           border border-slate-200
                           shadow-sm p-6">

                    <div class="flex items-center justify-between mb-5">
                        <div>
                            <h3 class="text-lg font-bold text-slate-900">Recent call timeline</h3>
                            <p class="text-xs text-slate-500">Latest outreach from your team</p>
                        </div>
                        <span class="px-3 py-1 bg-emerald-100 text-emerald-700 rounded-full text-xs font-semibold">Live updates</span>
                    </div>

                    <div class="space-y-4">

                        <div
                            class="searchable-item
                                   p-4 bg-slate-50
                                   border border-slate-200
                                   rounded-2xl
                                   flex items-center justify-between gap-4">

                            <div class="flex items-start gap-4">
                                <div class="w-11 h-11 rounded-xl bg-purple-100 text-purple-600 flex items-center justify-center font-bold">N</div>

                                <div>
                                    <div class="flex items-center flex-wrap gap-2">
                                        <span class="font-bold text-slate-900">Naledi van Wyk</span>
                                        <span class="px-2 py-0.5 bg-purple-100 text-purple-700 text-[10px] font-semibold rounded-full">Ringing</span>
                                        <span class="text-xs text-slate-400">ACC-20256</span>
                                    </div>

                                    <p class="text-sm text-slate-600 mt-1">
                                        No answer. Left voicemail and requested a callback before 4:00 PM.
                                    </p>
                                </div>
                            </div>

                            <div class="text-right shrink-0">
                                <p class="text-xs text-slate-400">2 min ago</p>
                                <button class="mt-2 px-3 py-1.5 bg-slate-900 text-white rounded-xl text-xs font-medium">View details</button>
                            </div>

                        </div>


                        <div
                            class="searchable-item
                                   p-4 bg-slate-50
                                   border border-slate-200
                                   rounded-2xl
                                   flex items-center justify-between gap-4">

                            <div class="flex items-start gap-4">
                                <div class="w-11 h-11 rounded-xl bg-emerald-100 text-emerald-600 flex items-center justify-center font-bold">T</div>

                                <div>
                                    <div class="flex items-center flex-wrap gap-2">
                                        <span class="font-bold text-slate-900">Thandiwe Mokoena</span>
                                        <span class="px-2 py-0.5 bg-emerald-100 text-emerald-700 text-[10px] font-semibold rounded-full">Connected</span>
                                        <span class="text-xs text-slate-400">ACC-20240</span>
                                    </div>

                                    <p class="text-sm text-slate-600 mt-1">
                                        Promised payment verification and agreed to send proof by 5:00 PM.
                                    </p>
                                </div>
                            </div>

                            <div class="text-right shrink-0">
                                <p class="text-xs text-slate-400">18 min ago</p>
                                <button class="mt-2 px-3 py-1.5 bg-emerald-50 text-emerald-700 border border-emerald-200 rounded-xl text-xs font-semibold">Follow up</button>
                            </div>

                        </div>


                        <div
                            class="searchable-item
                                   p-4 bg-slate-50
                                   border border-slate-200
                                   rounded-2xl
                                   flex items-center justify-between gap-4">

                            <div class="flex items-start gap-4">
                                <div class="w-11 h-11 rounded-xl bg-rose-100 text-rose-600 flex items-center justify-center font-bold">S</div>

                                <div>
                                    <div class="flex items-center flex-wrap gap-2">
                                        <span class="font-bold text-slate-900">Sipho Dlamini</span>
                                        <span class="px-2 py-0.5 bg-rose-100 text-rose-700 text-[10px] font-semibold rounded-full">Unreachable</span>
                                        <span class="text-xs text-slate-400">ACC-20213</span>
                                    </div>

                                    <p class="text-sm text-slate-600 mt-1">
                                        Number out of service. Escalated to branch verification and SMS reminder.
                                    </p>
                                </div>
                            </div>

                            <div class="text-right shrink-0">
                                <p class="text-xs text-slate-400">1 hr ago</p>
                                <button class="mt-2 px-3 py-1.5 bg-rose-50 text-rose-700 border border-rose-200 rounded-xl text-xs font-semibold">Action plan</button>
                            </div>

                        </div>

                    </div>

                    <div
                        id="noSearchResults"
                        class="hidden text-center
                               py-8 text-slate-500">

                        No call records found.

                    </div>

                </div>

            </div>

        </main>

    </div>

    {global_scripts}

</body>
</html>
"""
)

# ============================================================
# 5. ARRANGEMENTS
# ============================================================

arrangements_html = (
    base_head
    + get_sidebar("arrangements.html")
    + f"""
        <main class="flex-1 flex flex-col
                     h-full overflow-hidden">

            {get_header()}

            <div
                class="flex-1 overflow-y-auto
                       p-6 lg:p-8 space-y-6">

                <div>

                    <h2
                        class="text-2xl font-bold
                               text-slate-900
                               tracking-tight">

                        Payment Arrangements

                    </h2>

                    <p
                        class="text-sm text-slate-500
                               mt-0.5">

                        Track active payment plans
                        and promised installments.

                    </p>

                </div>


                <div
                    class="bg-white rounded-2xl
                           border border-slate-200
                           shadow-sm p-6">

                    <div class="overflow-x-auto">

                        <table
                            class="w-full text-left
                                   text-sm">

                            <thead>

                                <tr
                                    class="border-b
                                           border-slate-200
                                           text-slate-400
                                           text-xs uppercase">

                                    <th class="py-3 px-4">
                                        Arrangement ID
                                    </th>

                                    <th class="py-3 px-4">
                                        Debtor
                                    </th>

                                    <th class="py-3 px-4">
                                        Collector
                                    </th>

                                    <th
                                        class="py-3 px-4
                                               text-right">

                                        Installment

                                    </th>

                                </tr>

                            </thead>


                            <tbody
                                class="divide-y
                                       divide-slate-100">


                                <tr>

                                    <td
                                        class="py-3 px-4
                                               font-mono
                                               font-bold
                                               text-blue-600">

                                        PA-512

                                    </td>

                                    <td
                                        class="py-3 px-4
                                               font-semibold">

                                        Bongani Ndlovu

                                    </td>

                                    <td
                                        class="py-3 px-4">

                                        Thandiwe Mokoena

                                    </td>

                                    <td
                                        class="py-3 px-4
                                               text-right
                                               font-mono
                                               font-bold">

                                        R 1,500 /mo

                                    </td>

                                </tr>


                                <tr>

                                    <td
                                        class="py-3 px-4
                                               font-mono
                                               font-bold
                                               text-blue-600">

                                        PA-509

                                    </td>

                                    <td
                                        class="py-3 px-4
                                               font-semibold">

                                        Ayanda Khumalo

                                    </td>

                                    <td
                                        class="py-3 px-4">

                                        Sipho Dlamini

                                    </td>

                                    <td
                                        class="py-3 px-4
                                               text-right
                                               font-mono
                                               font-bold">

                                        R 2,000 /mo

                                    </td>

                                </tr>

                            </tbody>

                        </table>

                    </div>


                    <div
                        id="noSearchResults"
                        class="hidden text-center
                               py-8 text-slate-500">

                        No payment arrangements found.

                    </div>

                </div>

            </div>

        </main>

    </div>

    {global_scripts}

</body>
</html>
"""
)


# ============================================================
# 6. FOLLOW UPS
# ============================================================

follow_ups_html = (
    base_head
    + get_sidebar("follow_ups.html")
    + f"""
        <main class="flex-1 flex flex-col
                     h-full overflow-hidden">

            {get_header()}

            <div
                class="flex-1 overflow-y-auto
                       p-6 lg:p-8 space-y-6">

                <div>

                    <h2
                        class="text-2xl font-bold
                               text-slate-900
                               tracking-tight">

                        Follow-ups Schedule

                    </h2>

                    <p
                        class="text-sm text-slate-500
                               mt-0.5">

                        Manage daily tasks, reminders,
                        and scheduled account callbacks.

                    </p>

                </div>


                <div
                    class="bg-white rounded-2xl
                           border border-slate-200
                           shadow-sm p-6 space-y-4">

                    <h3
                        class="font-bold text-rose-600
                               text-base">

                        Today's follow-up

                    </h3>


                    <div
                        class="searchable-item
                               p-4 bg-slate-50
                               border border-slate-100
                               rounded-xl flex items-center
                               justify-between">

                        <div>

                            <div
                                class="flex items-center
                                       space-x-2">

                                <span
                                    class="font-bold
                                           text-slate-900">

                                    Bongani Ndlovu

                                </span>

                                <span
                                    class="text-xs
                                           text-slate-400">

                                    ACC-20240

                                </span>

                                <span
                                    class="px-2 py-0.5
                                           bg-rose-100
                                           text-rose-700
                                           text-[10px]
                                           font-bold rounded">

                                    High

                                </span>

                            </div>

                            <p
                                class="text-xs
                                       text-slate-500 mt-1">

                                Promise to pay verification ·
                                Thandiwe Mokoena

                            </p>

                        </div>


                        <button
                            onclick="window.location.href='call_log.html'"
                            class="px-3 py-1.5
                                   bg-emerald-50
                                   text-emerald-700
                                   border border-emerald-200
                                   rounded-xl text-xs
                                   font-semibold
                                   flex items-center">

                            <i
                                class="fa-solid fa-phone
                                       mr-1.5">
                            </i>

                            Call

                        </button>

                    </div>


                    <div
                        id="noSearchResults"
                        class="hidden text-center
                               py-8 text-slate-500">

                        No follow-ups found.

                    </div>

                </div>

            </div>

        </main>

    </div>

    {global_scripts}

</body>
</html>
"""
)


# ============================================================
# 7. CLIENTS
# ============================================================

clients_html = (
    base_head
    + get_sidebar("clients.html")
    + f"""
        <main class="flex-1 flex flex-col
                     h-full overflow-hidden">

            {get_header()}

            <div
                class="flex-1 overflow-y-auto
                       p-6 lg:p-8 space-y-6">

                <div>

                    <h2
                        class="text-2xl font-bold
                               text-slate-900
                               tracking-tight">

                        Clients Directory

                    </h2>

                    <p
                        class="text-sm text-slate-500
                               mt-0.5">

                        Directory of debtors with account,
                        contact and balance information.

                    </p>

                </div>


                <div
                    class="bg-white rounded-2xl
                           border border-slate-200
                           shadow-sm p-6">

                    <div class="overflow-x-auto">

                        <table
                            class="w-full text-left
                                   text-sm">

                            <thead>

                                <tr
                                    class="border-b
                                           border-slate-200
                                           text-slate-400
                                           text-xs uppercase">

                                    <th class="py-3 px-4">
                                        Client
                                    </th>

                                    <th class="py-3 px-4">
                                        Phone
                                    </th>

                                    <th
                                        class="py-3 px-4
                                               text-right">

                                        Balance

                                    </th>

                                    <th
                                        class="py-3 px-4
                                               text-center">

                                        Status

                                    </th>

                                </tr>

                            </thead>


                            <tbody
                                class="divide-y
                                       divide-slate-100">


                                <tr>

                                    <td
                                        class="py-3 px-4
                                               font-semibold">

                                        Bongani Ndlovu

                                        <br>

                                        <span
                                            class="text-xs
                                                   text-slate-400
                                                   font-normal">

                                            C-1000

                                        </span>

                                    </td>

                                    <td
                                        class="py-3 px-4
                                               font-mono
                                               text-xs">

                                        +27 81 100 2000

                                    </td>

                                    <td
                                        class="py-3 px-4
                                               text-right
                                               font-mono
                                               font-bold">

                                        R 12 000

                                    </td>

                                    <td
                                        class="py-3 px-4
                                               text-center">

                                        <span
                                            class="px-2 py-0.5
                                                   bg-emerald-50
                                                   text-emerald-700
                                                   rounded
                                                   text-xs
                                                   font-semibold">

                                            In Arrangement

                                        </span>

                                    </td>

                                </tr>


                                <tr>

                                    <td
                                        class="py-3 px-4
                                               font-semibold">

                                        Ayanda Khumalo

                                        <br>

                                        <span
                                            class="text-xs
                                                   text-slate-400
                                                   font-normal">

                                            C-1001

                                        </span>

                                    </td>

                                    <td
                                        class="py-3 px-4
                                               font-mono
                                               text-xs">

                                        +27 82 101 2007

                                    </td>

                                    <td
                                        class="py-3 px-4
                                               text-right
                                               font-mono
                                               font-bold">

                                        R 15 287

                                    </td>

                                    <td
                                        class="py-3 px-4
                                               text-center">

                                        <span
                                            class="px-2 py-0.5
                                                   bg-teal-50
                                                   text-teal-700
                                                   rounded
                                                   text-xs
                                                   font-semibold">

                                            Active

                                        </span>

                                    </td>

                                </tr>

                            </tbody>

                        </table>

                    </div>


                    <div
                        id="noSearchResults"
                        class="hidden text-center
                               py-8 text-slate-500">

                        No clients found.

                    </div>

                </div>

            </div>

        </main>

    </div>

    {global_scripts}

</body>
</html>
"""
)


# ============================================================
# 8. NOTIFICATIONS
# ============================================================

notifications_html = (
    base_head
    + get_sidebar("notifications.html")
    + f"""
        <main class="flex-1 flex flex-col
                     h-full overflow-hidden">

            {get_header()}

            <div
                class="flex-1 overflow-y-auto
                       p-6 lg:p-8 space-y-6">

                <div>

                    <h2
                        class="text-2xl font-bold
                               text-slate-900
                               tracking-tight">

                        System Notifications

                    </h2>

                    <p
                        class="text-sm text-slate-500
                               mt-0.5">

                        Recent automated alerts
                        and system activities.

                    </p>

                </div>


                <div
                    class="bg-white rounded-2xl
                           border border-slate-200
                           shadow-sm p-6 space-y-4">


                    <div
                        class="searchable-item
                               flex items-start space-x-3
                               pb-3
                               border-b border-slate-100">

                        <span
                            class="w-2 h-2 mt-1.5
                                   rounded-full
                                   bg-amber-500">
                        </span>

                        <div>

                            <p
                                class="font-medium
                                       text-slate-800
                                       text-sm">

                                Naledi van Wyk logged a call

                                <span
                                    class="text-blue-600
                                           font-semibold">

                                    ACC-20256

                                </span>

                            </p>

                            <span
                                class="text-xs
                                       text-slate-400">

                                2 min ago

                            </span>

                        </div>

                    </div>


                    <div
                        class="searchable-item
                               flex items-start space-x-3
                               pb-3
                               border-b border-slate-100">

                        <span
                            class="w-2 h-2 mt-1.5
                                   rounded-full
                                   bg-emerald-500">
                        </span>

                        <div>

                            <p
                                class="font-medium
                                       text-slate-800
                                       text-sm">

                                Thandiwe Mokoena
                                created arrangement

                                <span
                                    class="text-blue-600
                                           font-semibold">

                                    PA-512

                                </span>

                            </p>

                            <span
                                class="text-xs
                                       text-slate-400">

                                18 min ago

                            </span>

                        </div>

                    </div>


                    <div
                        class="searchable-item
                               flex items-start space-x-3
                               pb-3">

                        <span
                            class="w-2 h-2 mt-1.5
                                   rounded-full
                                   bg-blue-500">
                        </span>

                        <div>

                            <p
                                class="font-medium
                                       text-slate-800
                                       text-sm">

                                System imported
                                24 accounts batch-07-08

                            </p>

                            <span
                                class="text-xs
                                       text-slate-400">

                                1 hr ago

                            </span>

                        </div>

                    </div>


                    <div
                        id="noSearchResults"
                        class="hidden text-center
                               py-8 text-slate-500">

                        No notifications found.

                    </div>

                </div>

            </div>

        </main>

    </div>

    {global_scripts}

</body>
</html>
"""
)


# ============================================================
# GENERATE ALL HTML FILES
# ============================================================

pages = {

    "index.html": dashboard_html,

    "accounts.html": accounts_html,

    "assigned_accounts.html":
        assigned_accounts_html,

    "call_log.html":
        call_log_html,

    "arrangements.html":
        arrangements_html,

    "follow_ups.html":
        follow_ups_html,

    "clients.html":
        clients_html,

    "notifications.html":
        notifications_html
}


for filename, content in pages.items():

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(content)

    print(f"Generated: {filename}")


print("")
print("========================================")
print("VTO FRONTEND GENERATED SUCCESSFULLY")
print("========================================")
print("8 HTML pages created.")
print("")
