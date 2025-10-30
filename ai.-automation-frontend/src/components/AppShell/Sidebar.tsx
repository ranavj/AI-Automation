import { NavLink } from "react-router-dom";


const link = "block px-3 py-2 rounded hover:bg-slate-200 dark:hover:bg-slate-800";


export function Sidebar() {
    return (
        <div className="p-3 space-y-2">
            <div className="text-xl font-semibold mb-4">AI + Automation</div>
            <nav className="space-y-1">
                <NavLink to="/" end className={({ isActive }) => isActive ? `${link} bg-slate-200 dark:bg-slate-800` : link}>Dashboard</NavLink>
                <NavLink to="/workflows" className={({ isActive }) => isActive ? `${link} bg-slate-200 dark:bg-slate-800` : link}>Workflows</NavLink>
                <NavLink to="/integrations" className={({ isActive }) => isActive ? `${link} bg-slate-200 dark:bg-slate-800` : link}>Integrations</NavLink>
                <NavLink to="/settings" className={({ isActive }) => isActive ? `${link} bg-slate-200 dark:bg-slate-800` : link}>Settings</NavLink>
            </nav>
        </div>
    );
}