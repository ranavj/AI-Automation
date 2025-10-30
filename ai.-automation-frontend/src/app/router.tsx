import { createBrowserRouter } from "react-router-dom";
import { AppShell } from "../components/AppShell/AppShell";
import { Dashboard } from "../pages/Dashboard";
import { Workflows } from "../pages/Workflows";
import { Integrations } from "../pages/Integrations";
import { Settings } from "../pages/Settings";
import { NotFound } from "../pages/NotFound";


export const router = createBrowserRouter([
    {
        path: "/",
        element: <AppShell />,
        children: [
            { index: true, element: <Dashboard /> },
            { path: "workflows", element: <Workflows /> },
            { path: "integrations", element: <Integrations /> },
            { path: "settings", element: <Settings /> },
            { path: "*", element: <NotFound /> },
        ],
    },
]);