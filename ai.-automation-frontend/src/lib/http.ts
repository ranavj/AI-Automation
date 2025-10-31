const BASE = import.meta.env.VITE_API_BASE ?? "http://localhost:8001";


export async function api<T>(path: string, init?: RequestInit): Promise<T> {
    const res = await fetch(`${BASE}${path}`, (init?.body ? {
        ...init,
        headers: { "Content-Type": "application/json", ...(init?.headers || {}) },
    } : init));
    if (!res.ok) {
        const txt = await res.text();
        throw new Error(txt || `HTTP ${res.status}`);
    }
    return res.json() as Promise<T>;
}