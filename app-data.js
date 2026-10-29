/* Shared browser-side data for the VTO Recovery admin workspace. */
window.VTOData = (() => {
    const keys = {
        accounts: 'vtoImportedAccounts',
        reviewedAccounts: 'vtoReviewedAccounts',
        assignments: 'vtoAccountAssignments',
        collectors: 'vtoCollectors',
        calls: 'vtoCallLogs',
        arrangements: 'vtoArrangements'
    };
    const defaultCollectors = ['Vura Mokoena', 'Thandiwe Dlamini', 'Kabelo Nkosi', 'Nomsa Khumalo', 'Sipho Mthembu', 'Ayesha Patel'];
    const read = (key, fallback) => { try { return JSON.parse(localStorage.getItem(key) || 'null') ?? fallback; } catch { return fallback; } };
    const write = (key, value) => localStorage.setItem(key, JSON.stringify(value));
    const clean = value => value === undefined || value === null || value === '' || value === '0' ? '' : String(value).trim();
    const normalizeAccount = row => row.contract_number !== undefined ? row : ({
        contract_number: row.id || '', loan_id: '', target_date: '', days_overdue: row.daysOverdue || '', calculated_debt: row.balance || '',
        'Cell Phone 1': row.number || '', 'Date of Default': row.defaultDate || '', 'Debtor Firstname': row.name || ''
    });
    const imported = () => [...read(keys.accounts, []), ...read(keys.reviewedAccounts, [])].map(normalizeAccount);
    const accountId = row => clean(row.contract_number) || clean(row['Jabulani Account No OR Reference']) || clean(row.loan_id);
    const name = row => [row['Debtor Firstname'], row['Debtor Second Name'], row['Debtor Surname']].map(clean).filter(Boolean).join(' ') || 'Name unavailable';
    const phone = row => clean(row['Cell Phone 1']) || clean(row['Cell Phone 2']) || clean(row['Home Phone 1']) || clean(row['Work Phone 1']);
    const balance = row => {
        const value = clean(row.calculated_debt);
        if (!value) return '';
        const number = Number(value.replace(/[R,\s]/g, ''));
        return Number.isFinite(number) ? number : value;
    };
    const assignments = () => read(keys.assignments, {});
    const accounts = () => { const assigned = assignments(); return imported().filter(row => accountId(row)).map(row => ({
        ...row, id: accountId(row), name: name(row), phone: phone(row), balance: balance(row), days: Number(row.days_overdue) || 0,
        status: clean(row.status) || 'New', defaultDate: clean(row['Date of Default']), assignedTo: assigned[accountId(row)] || ''
    })); };
    const assign = (id, collector) => { const all = assignments(); if (collector) all[id] = collector; else delete all[id]; write(keys.assignments, all); };
    const assignMany = (ids, collector) => { const all = assignments(); ids.forEach(id => { if (collector) all[id] = collector; else delete all[id]; }); write(keys.assignments, all); };
    const collectors = () => read(keys.collectors, defaultCollectors);
    const calls = () => read(keys.calls, []);
    const saveCalls = rows => write(keys.calls, rows);
    const arrangements = () => read(keys.arrangements, []);
    const saveArrangements = rows => write(keys.arrangements, rows);
    const money = value => value === '' || value === null || value === undefined || !Number.isFinite(Number(value)) ? '—' : `R ${Number(value).toLocaleString('en-ZA', {minimumFractionDigits: 2, maximumFractionDigits: 2})}`;
    const safe = value => String(value ?? '').replace(/[&<>"']/g, char => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[char]));
    return {keys, read, write, imported, accountId, accounts, name, phone, balance, assignments, assign, assignMany, collectors, calls, saveCalls, arrangements, saveArrangements, money, safe, clean};
})();
