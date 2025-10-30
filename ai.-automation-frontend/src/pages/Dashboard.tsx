import { useQuery } from "@tanstack/react-query";
import { api } from "../lib/http";


type Health = { status: string; time: string };


export function Dashboard() {
    const { data, isLoading, isError } = useQuery({
        queryKey: ["health"],
        queryFn: () => api<Health>("/api/health"),
    });


    return (
        <div className="space-y-4">
            <h1 className="text-2xl font-semibold">Dashboard</h1>
            {isLoading && <p>Checking backend…</p>}
            {isError && <p className="text-red-600">Backend not reachable</p>}
            {data && (
                <div className="rounded border p-4">
                    <div>Status: <b>{data.status}</b></div>
                    <div>Time: {new Date(data.time).toLocaleString()}</div>
                </div>
            )}
        </div>
    );
}