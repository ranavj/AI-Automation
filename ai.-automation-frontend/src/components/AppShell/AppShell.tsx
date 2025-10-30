import { Outlet } from "react-router-dom";
import { Sidebar } from "./Sidebar";
import { Header } from "./Header";


export function AppShell() {
    return (
        <div className="min-h-screen grid grid-cols-[240px_1fr] grid-rows-[56px_1fr]">
            <aside className="row-span-2 bg-slate-100 dark:bg-slate-900 border-r border-slate-200 dark:border-slate-800">
                <Sidebar />
            </aside>
            <header className="col-start-2 border-b border-slate-200 dark:border-slate-800">
                <Header />
            </header>
            <main className="col-start-2 p-4">
                <Outlet />
            </main>
        </div>
    );
}