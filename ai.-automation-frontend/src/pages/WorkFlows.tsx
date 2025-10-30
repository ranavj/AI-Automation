import { useMutation } from "@tanstack/react-query";
import { api } from "../lib/http";


export function Workflows() {
    const { mutate, data, isPending } = useMutation({
        mutationFn: (payload: any) => api("/api/workflows/parse", {
            method: "POST",
            body: JSON.stringify(payload),
        }),
    });


    const sample = {
        nodes: [{ id: "n1" }, { id: "n2" }],
        edges: [{ source: "n1", target: "n2" }],
    };


    return (
        <div className="space-y-4">
            <h1 className="text-2xl font-semibold">Workflows</h1>
            <button
                className="px-3 py-2 rounded border"
                onClick={() => mutate(sample)}
                disabled={isPending}
            >
                {isPending ? "Checking…" : "Parse sample pipeline"}
            </button>
            {data && (
                <pre className="p-3 bg-slate-100 dark:bg-slate-900 rounded text-sm overflow-auto">
                    {JSON.stringify(data, null, 2)}
                </pre>
            )}
        </div>
    );
}